from config import CLIENT_ID, CLIENT_SECRET
import requests

def __init__():
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    try:
        song = requests.get(api.geniuscom/songs/378195)
    except:
        raise IOError("Couldn't connect to API.")
    return song

__init__()
