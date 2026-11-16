#imports
import requests



class SongMethods:
#Where all the logic for the process will be implemented such as choosing artist, administering each round, to choosing final song

    #Constructor method for the Song-Method Class
    def __init__ (self):
        self.artist = " "
        self.albums = {}
        self.EPs = {}
        self.singles = []
        self.favorite_song = " "

    #First step is to have the user choose an artist
    def choose_artist(self):
        self.artist = input("Choose an artist: ")
        self.search_artist()

    #Search MusicBrainz API for the artist
    def search_artist(self):
        url = 'https://musicbrainz.org/ws/2/artist/'
        parameters = {
            'query': self.artist,
            'fmt': 'json',
            'limit': 5}
        response = requests.get(
            url, 
            params=parameters,
            headers={"User-Agent": "ChooseFaveSong/0.1 (snabboud1@gmail.com)"},
            timeout = 10
            )
        print(response.status_code)

    #retrieve the artists albums (ALL)
    def choose_albums(self):
        url = https://musicbrainz.org/ws/2/release-group
        parameters = {
            "artist": self.artist_id,
            "type": "album",
            "fmt": "json",
            "limit": 100}
        response = requests.get(url, params=parameters)
        response.raise_for_status()
        albums = data["release-groups"]
        for album in albums:
            #store into album dict temporarily
            self.albums[album["title"]] = album["id"]
            print(album["title"])

