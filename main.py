from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel ? \n"
              "Type the date in this format YYY-MM-DD:\n")

url = "https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=url)
data = response.text

page = BeautifulSoup(data, features='html.parser')
ranking_data = page.find_all('span', attrs={'class', 'chart-element_rank_number'})
artist_data = page.find_all('class', attrs={'class', 'chart-element_information_artist'})
title_data = page.find_all('span', attrs={'class', 'chart-element_information_song'})

rankings, artists, titles = [], [], []
[rankings.append(ranking.string) for ranking in ranking_data]
[artists.append(artist.string) for artist in artist_data]
[titles.append(title.string) for title in title_data]

playlist = list(zip(rankings, artists, titles))


SPOTIFY_CLIENT_ID = "******************" #You have to add own ID and Client Secret
SPOTIFY_CLIENT_SECRET = "**********"
SPOTIFY_REDIRECT_URL = "https://example.com/"
PLAYLIST_URL = f"https://api.spotify.com/v1/users/{SPOTIFY_CLIENT_ID}/playlists"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URL,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
uri_list = []
for song in playlist:
    search_results = sp.search(q=f"track:{song[2]} year:{date[:4]}", type="track")
    try:
        uri = search_results['tracks']['items'][0]['uri']
        uri_list.append(uri)
    except IndexError:
        print(f"{song[2]} by {song[1]} doesn't exist on Spotify. Skipped.")
        with open("songs_skipped.txt", mode="a") as file:
            file.write(f"{song[2]} by {song[1]}\n")

with open("uri_results.txt", mode="w") as file:
    for uri in uri_list:
        file.write(f"{uri}\n")


new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard Hot-100 ({date})",
    public=False
)


sp.playlist_add_items(playlist_id=new_playlist["id"], items=uri_list)


