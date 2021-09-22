# Pandorinha

Discover music with [Pandora](https://www.pandora.com)

If you are not in the US you need to use a VPN or equivalent

# Install

`pip install pandorinha==0.0.1a2`

# Setup

you need to setup pandora credentials, edit or create `~/.config/pandorinha/pandora.json`

```json
{
  "email": "mypandora@mail.com",
  "password": "SuperSecret"
}
```

# Usage

This is in very early stage, expect examples to get outdated and api to break!

```python
from pandorinha import Pandora

pandora = Pandora()
pandora.login()

for song in pandora.discover():
    print(song)
    
for song in pandora.similar("quiet riot"):
    print(song)

"""
{'album': 'Open Up And Say . . . Ahh!',
 'artist': 'Poison',
 'bg_image': 'http://mediaserver-cont-sv5-2-v4v6.pandora.com/images/ac/c2/ca/2c/1c8c4f38b5deb6ebd20fb753/1080W_1080H.jpg',
 'duration': 223,
 'image': 'http://mediaserver-cont-sv5-2-v4v6.pandora.com/images/ac/c2/ca/2c/1c8c4f38b5deb6ebd20fb753/1080W_1080H.jpg',
 'match_confidence': 0.8002946127946128,
 'station': 'Quiet Riot Radio',
 'title': "Nothin' But A Good Time",
 'uri': 'http://audio-usc-mp1-t1-2-v4v6.pandora.com/access/5409138788479642529.mp4?version=5&lid=1824884349&token=%2BXTl%2B2PCnb2bZrYOZ3ug0z60sKbIz%2FZnUoxRmqEGW3pekgtyBP5BeD%2F6qA9fggDBaEXPj54W0qKld1%2BgPkaIxSYzCt%2FKtLTaTUGIwe4S4GqikJtKYu2rw701g5%2BuMEU6K4KEBrEkvrHaOy%2F7UGjYuqGD4cMNi%2BOosNRmEwx4y2kOh3T%2Fmm6nBnfLLizArpj1SK0jarOAFwEryQtofPVBBGBzsUv7AWLGbMegWOJJcTAPunBxpB%2BXXk80loL4i5yQbzLjFqN5H%2BR6QqVxbYJphrtu1GTIu7wD11Q4tNmeEeAWrH%2FmPlsbVA1h696zHGYIO3ZWqhvGJ1CG4Wnor5SKqA%3D%3D'}
"""
```
