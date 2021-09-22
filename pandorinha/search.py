from pandorinha.util import fuzzy_match, MatchStrategy
from pandorinha.auth import get_client


def get_playlist(station):
    for track in station.get_playlist():
        if not track.audio_url:
            continue
        yield {
            "artist": track.artist_name,
            "uri": track.audio_url,
            "album": track.album_name,
            "title": track.song_name,
            "duration": track.track_length,
            "image": track.album_art_url,
            "station": station.name,
            "bg_image": station.art_url or track.album_art_url
        }


def _score_track(track, query, base_score, match_func):
    track_score = match_func(query, track["title"])
    album_score = match_func(query, track["album"])
    artist_score = match_func(query, track["artist"])
    score2 = (track_score + album_score + artist_score) / 3
    return 0.75 * base_score + 0.25 * score2


def _match_query(query, station_name, strategy=MatchStrategy.SIMPLE_RATIO):
    ignored_words = [" explicit", "remastered", "re-recorded", "/", "(", ")",
                     " feat.", " deluxe", " edition", " edit"]
    clean_query = query.lower()
    clean_station = station_name.lower()
    for w in ignored_words:
        clean_query = clean_query.replace(w, "").strip()
        clean_station = clean_station.replace(w, "").strip()
    return fuzzy_match(clean_query, clean_station, strategy)


def search_station(query, client=None, match_func=_match_query):
    client = client or get_client()
    scores = []

    for station in client.get_station_list():
        score = match_func(query, station.name)
        if station.name == 'QuickMix':
            score = score / 2
        scores.append((station, score))

    for station, score in sorted(scores, key=lambda k: k[1], reverse=True):
        for track in get_playlist(station):
            track["match_confidence"] = _score_track(track, query,
                                                     score, match_func)
            yield track


def search_song(query, client=None, match_func=_match_query):
    client = client or get_client()

    res = client.search(query)

    scores = []
    for song in res.songs:
        try:
            station = song.create_station()
        except Exception as e:
            # track_token kwarg sometimes errors out
            station = song._api_client.create_station(song_token=song.token)
        score = match_func(query, song.song_name)
        scores.append((station, score))

    for station, score in sorted(scores, key=lambda k: k[1], reverse=True):
        for track in get_playlist(station):
            track["match_confidence"] = _score_track(track, query,
                                                     score, match_func)
            yield track


def search_artist(query, client=None, match_func=_match_query):
    client = client or get_client()

    res = client.search(query)

    scores = []

    for artist in res.artists:
        station = artist.create_station()
        score = match_func(query, artist.artist)
        scores.append((station, score))

    for station, score in sorted(scores, key=lambda k: k[1], reverse=True):
        for track in get_playlist(station):
            track["match_confidence"] = _score_track(track, query,
                                                     score, match_func)
            yield track


def search(query, client=None, match_func=_match_query):
    client = client or get_client()

    for track in search_song(query, client, match_func):
        yield track

    for track in search_artist(query, client, match_func):
        yield track

    for track in search_station(query, client, match_func):
        yield track


