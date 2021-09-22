from pandorinha.search import search, search_song, search_station, \
    search_artist, get_playlist
from pandorinha.auth import get_client


class Pandora:
    def __init__(self):
        self.client = None

    def login(self, email=None, password=None):
        self.client = get_client(email, password)

    def discover(self):
        for station in self.client.get_station_list():
            for track in get_playlist(station):
                yield track

    def similar(self, query):
        return search(query, self.client)

    def similar_to_artist(self, query):
        return search_artist(query, self.client)

    def similar_to_song(self, query):
        return search_song(query, self.client)

    def similar_to_station(self, query):
        return search_station(query, self.client)
