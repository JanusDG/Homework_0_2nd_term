import requests
import json
import matplotlib.pyplot as pyplot
from matplotlib import style

url = 'https://api.deezer.com/genre'


def get_data_from_URL(url):
    """(str) -> dict
    Function for getting data from URL (DEEZER)
    """
    querystring = {"q": "eminem"}
    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    received_file = json.loads(response.text)
    return received_file


def get_statistic():
    """ NoneType -> dict
    Makes requests and finds in received
    files necessary information.
    After it, creates dictionary about different genres:
        * name: (number of artists, number of fans)
        * uses requests:
            genres(-> id of genre),
            genre artists(-> number of artists, id of artists),
            artist(-> number of fans)
    """

    data = get_data_from_URL(url)["data"]
    results = dict()

    for genre in data:
        # get information about one genre
        genre_url = f"{url}/{genre['id']}/artists"
        genre_data = get_data_from_URL(genre_url)["data"]

        nb_fan = 0
        for artist in genre_data:
            # get information about one artist (number of fans)
            art_data = get_data_from_URL(
                f'https://api.deezer.com/artist/{artist["id"]}')
            nb_fan += art_data["nb_fan"]

        # add to dictionary received information
        results[genre["name"]] = (len(genre_data), nb_fan)

    return results

def write_in_json(data):
    """ (dict) -> NoneType
    Writes this data in file 'genre.json'
    """
    with open('genre.json', 'w') as data_file:
        json.dump(data, data_file, indent= 4)   


def visualize_data(data):
    """ (dict) -> NoneType
    Visualize this data as two bars:
        * x: genres; y: number of artists
        * x: genres; y: number of fans
    """
    style.use("ggplot")
    fig, axs = pyplot.subplots(1, 2, figsize=(20, 10))

    axs[0].bar(list(data.keys()), list(
        map(lambda x: data[x][0], data)))
    axs[0].set_ylabel('Number of artists')

    axs[1].bar(list(data.keys()), list(
        map(lambda x: data[x][1], data)))
    axs[1].set_ylabel('Number of fans')

    fig.suptitle('Distribution of artists and fans by genre')
    fig.autofmt_xdate(bottom=0.2, rotation=50)
    pyplot.show()

def main():
    """ NoneType -> NoneType
    Gets data about different genres:
        * name: (number of artists, number of fans)
        * uses requests:
            genres(-> id of genre),
            genre artists(-> number of artists, id of artists),
            artist(-> number of fans)
    Writes this data in json file
    Visualize this data with matplotlib
    """
    data = get_statistic()
    write_in_json(data)
    visualize_data(data)

if __name__ == "__main__":
    main()
