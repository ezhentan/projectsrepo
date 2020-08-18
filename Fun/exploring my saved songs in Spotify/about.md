# Exploring my saved songs in Spotify

Confidential variables:
1. Credentials (client id, client secret)
2. Spotify username

```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

import time
from time import time

import json
import pandas as pd
```

```python
scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope, client_id=client_id, 
                                   client_secret=client_secret, 
                                   redirect_url='http://localhost:4000/callback')
```

For my purposes, I wanted to explore the audio features of my saved music. As such, I saved all the features that could be gathered from `sp.audio_features()`, but this can be adjusted according to different needs. 

In a future project, I will be attempting to create a randomised workout playlist (BPM 160-180) using the data gathered here.

```python
# Extract all details of each track by passing its id
def get_track_data(track_id):
    meta = sp.track(track_id)
    audio = sp.audio_features(track_id)
    
    track_details = {'name': meta['name'], 'album': meta['album']['name'],
                     'artist': meta['album']['artists'][0]['name'],
                     'release_date': meta['album']['release_date'],
                     'duration_in_min': round((meta['duration_ms'] * 0.001) / 60.0, 2),
                     'danceability': audio[0]['danceability'], 'energy': audio[0]['energy'],
                     'loudness': audio[0]['loudness'], 'mode': audio[0]['mode'],
                     'speechiness': audio[0]['speechiness'], 'instrumentalness': audio[0]['instrumentalness'],
                     'liveness': audio[0]['liveness'], 'valence': audio[0]['valence'], 'tempo': audio[0]['tempo'],
                     'time_signature': audio[0]['time_signature']}

    return track_details
```

```python
if token:
    sp = spotipy.Spotify(auth=token)
    
    id_start = time()
    
    # Appending all track ids in my saved songs to a list
    track_id = []
    for i in range(0, 10000, 50):
        results = sp.current_user_saved_tracks(limit=50, offset=i)
        for item in enumerate(results['item']):
            music_track = item['track']
            track_id.append(music_track['id'])
            
    id_end = time()
    print(f'Track ids took {(id_end - id_start) / 60} minutes to append.')
    
    data_start = time()
    
    tracks = []
    for i in range(len(track_id)):
        track = get_track_data(track_id[i])
        tracks.append(track)
        
        if i % 100 == 0:
            print(f'{i+1} / {len(track_id)} track data appended.')
            
    data_end = time()
    print(f'Track data took {(data_end - data_start) / 60} minutes to append.')
    
# Export to file
with open('spotify_saved_songs_data.json', 'w') as outfile:
    json.dump(tracks, outfile, indent=2)
    
# Import to DataFrame
saved_songs_df = pd.read_json('spotify_saved_songs_data.json')
print(saved_songs_df.head())
```

# References

https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

https://towardsdatascience.com/how-to-create-large-music-datasets-using-spotipy-40e7242cc6a6

https://www.promptcloud.com/blog/extracting-song-data-from-your-spotify-playlist/
