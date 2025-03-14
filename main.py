import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = "https://example.com"

date = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

try:
    response = requests.get(url)

except:
    print("Invalid date or format")

else:
    billboard_webpage = response.text

    soup = BeautifulSoup(billboard_webpage, "html.parser")
    songs_not_formatted = [item.getText() for item in soup.select(selector="li .o-chart-results-list__item h3")]
    songs = [song.strip() for song in songs_not_formatted]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=SPOTIPY_REDIRECT_URI,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    # To create a token.txt file, you will be redirected to a webpage.
    # Click accept and then copy the URL and paste it in the console.

    user_id = sp.current_user()["id"]

    song_uris = []
    year = date.split("-")[0]
    for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


