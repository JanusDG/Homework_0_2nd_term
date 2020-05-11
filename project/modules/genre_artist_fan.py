import matplotlib.pyplot as pyplot
from matplotlib import style
from modules.dict_atd import Dictionary
from modules.dict_usage import in_file, get_data_from_URL

url = 'https://api.deezer.com/genre'

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
    results = Dictionary()

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
        results[genre["name"]] = [len(genre_data), nb_fan]

    return results

def visualize_data(data):
    """ (dict) -> NoneType
    Visualize this data as two bars:
        * x: genres; y: number of artists
        * x: genres; y: number of fans
    """
    style.use("ggplot")
    fig, axs = pyplot.subplots(1, 2, figsize=(20, 10))

    axs[0].bar(list(data.keys), [data[i][0] for i in data.keys])
    axs[0].set_ylabel('Number of artists')

    axs[1].bar(list(data.keys), [data[i][1] for i in data.keys])
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
    in_file('files\\genre_artist_fan.json', data)
    visualize_data(data)

if __name__ == "__main__":
    main()
