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

scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_url='http://localhost:4000/callback')
```

# References

https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

https://towardsdatascience.com/how-to-create-large-music-datasets-using-spotipy-40e7242cc6a6

https://www.promptcloud.com/blog/extracting-song-data-from-your-spotify-playlist/
