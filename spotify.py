import requests, json 
from secrets import spotify_token


class Spotify:
    def __init__(self):
        self.library = {}
        self.spotify_token = spotify_token
    
    def get_artists_albums(self, artist):
        base_url = 'https://api.spotify.com/v1/search?q=' + artist
        url = base_url + '&type=artist&market=US&limit=11&offset=5'
        
        response = requests.get(
            url,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
                }
            )
        return response.json

        
        