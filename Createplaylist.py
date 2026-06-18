import spotify
import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ["SPOTIFY_CLIENT_ID"]
client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]

#TODO: Create functionality that allows the creation of a playlist
def do():
    response = requests.post(
         "https://accounts.spotify.com/api/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
        "grant_type": "client_credentials",
        "client_id": "",
        "client_secret": "",
        },
    )
    print(response.json())
    
    data = response.json()

    with open("response.json","w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def attempt():
    response = requests.get(
        "https://api.spotify.com/v1/artists/6LuN9FCkKOj5PcnpouEgny?si=jZe9v-y0T5OsM0m30hJdAg",
        headers={"Authorization": "Bearer REMOVED"},
    )

    print(response.json())
    print("===================")
    print(response.url)
    print("===================")
    print(response.history)
    print("===================")

    data = response.json()
    with open("kahlid.json","w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def test():
    print(os.environ.get("SPOTIFY_CLIENT_ID"))