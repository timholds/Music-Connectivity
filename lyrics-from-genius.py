from config import CLIENT_ID, CLIENT_SECRET, CLIENT_ACCESS_TOKEN
from requests_oauthlib import OAuth2Session
import requests
from bs4 import BeautifulSoup

# TODO - use the links from previously scraped data to scrape each song lyrics
# PSUEDOCODE
def get_one_song_lyrics(url):
    link = url
    # Data scrape the link

# TODO - For a given song, get the link to the song page, then scrape the lyrics

class Lyrics():

    ''' A class which gets song lyrics from genius.com '''

    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    token = CLIENT_ACCESS_TOKEN
    base_url = 'http://api.genius.com'
    headers = {'Authorization': 'Bearer ' + token}

    song_title = "Lake Song"
    artist_name = "The Decemberists"


    @classmethod
    def get_lyrics(cls):

        ''' Connects to the Genius API and gets song lyrics for one or more songs '''

        # Authorize request when using the API
        search_url = base_url + "/search"
        params = {'q': song_title}

        try:
            response = requests.get(search_url, params=params, headers=headers)
            print('The response is ' + str(response))
        except Exception as e:
            response = None
            print(e)
        return response

    @classmethod
    def lyrics_from_song_api_path(cls, song_api_path):

        ''' Method that gets song lyrics by scraping the song page returned by the Genius API '''

        song_url = base_url + song_api_path
        response = requests.get(song_url, headers=headers)
        json = response.json()
        path = json["response"]["song"]["path"]
        #gotta go regular html scraping... come on Genius
        page_url = "http://genius.com" + path
        page = requests.get(page_url)
        html = BeautifulSoup(page.text, "html.parser")
        #remove script tags that they put in the middle of the lyrics
        [h.extract() for h in html('script')]
        #at least Genius is nice and has a tag called 'lyrics'!
        lyrics = html.find('div', class_='lyrics').get_text() #updated css where the lyrics are based in HTML
        return lyrics

    if __name__ == "__main__":
        search_url = base_url + "/search"
        data = {'q': song_title}

        try:
            response = requests.get(search_url, data=data, headers=headers)
            json = response.json()
            print(json)
        except Exception as e:
            print(e)
            response = None
            json = None
        song_info = None
        for hit in json['response']['hits']:
            if hit['result']['primary_artist']['name'] == artist_name:
                song_info = hit
                break
        if song_info:
            song_api_path = song_info['result']['api_path']
            print(lyrics_from_song_api_path(song_api_path))

