# adapted from:
#  + https://github.com/plamere/spotipy#quick-start
#  + http://spotipy.readthedocs.io/en/latest/#client-credentials-flow

from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() # load environment variables
print("CLIENT ID:", os.environ.get("SPOTIPY_CLIENT_ID"))
print("CLIENT SECRET:", os.environ.get("SPOTIPY_CLIENT_SECRET"))


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#sp = spotipy.Spotify()

results = sp.search(q='Chelsea Cutler', limit=20)
for i, track in enumerate(results['tracks']['items']):
    print(' ', i, track['name'])
