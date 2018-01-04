from config import CLIENT_ID, CLIENT_SECRET, CLIENT_ACCESS_TOKEN
from requests_oauthlib import OAuth2Session
import requests


def get_lyrics():
    ''' Connects to the Genius API and gets song lyrics for one or more songs '''

    # Credentials from genius.com
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    token = CLIENT_ACCESS_TOKEN

    # Authorize request when using the API
    base_url = "http://api.genius.com"
    headers = {'Authorization': 'Bearer ' + token}
    search_url = base_url + "/search"
    song_title = "In the Midst of It All"
    params = {'q': song_title}

    try:
        response = requests.get(search_url, params=params, headers=headers)
        print(response)
    except Exception as e:
        response = None
        print(e)
    return response

get_lyrics()



