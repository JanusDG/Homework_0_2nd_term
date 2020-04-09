import urllib.request, urllib.parse, urllib.error
import json


base = 'https://api.deezer.com/'

search = 'eminem'
user_id = 2313380264
album_id = 8015602
url_search = base + \
f"/search/artist/?q={search}&index=0&limit=2&output=json"
url_user = f"https://api.deezer.com/user/{user_id}"
url_user_playlist = url_user + "/playlists" 
url_album = f"https://api.deezer.com/album/{album_id}"

def into_json(url):
    file = urllib.request.urlopen(url)
    data = json.load(file)
    real_data = {}
    for key, value in data.items():
        if key[:7] == "picture" or key == "link":
            continue
        real_data[key] = value

    with open("data.json", 'w') as f:
        json.dump(real_data, f, indent=4,ensure_ascii=False)

    return real_data

into_json(url_user_playlist)


