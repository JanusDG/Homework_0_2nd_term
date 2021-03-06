import matplotlib.pyplot as pyplot
import numpy as np
from modules.dict_atd import Dictionary
from modules.dict_usage import in_file, get_data_from_URL


def get_statistic():
    """ () -> (Dictionary)
    Makes requests and finds in received
    files necessary information.
    Create the statistic and return
    this statistic in format Dictionary where:
        * keys: string -> (rating place + artist name)
        * values: list( number of albums, number of fans ) """
    data = get_data_from_URL(
        'https://api.deezer.com/chart/0/artists')['data']
    results = Dictionary()
    counter = 1
    for artist in data:
        art_data = get_data_from_URL(
            f'https://api.deezer.com/artist/{artist["id"]}')
        results[str(counter) + ' ' + art_data['name']
                ] = [art_data["nb_album"], art_data["nb_fan"]]
        counter += 1
    return results


def visualize_data(data):
    """ (Dictionary) -> NoneType
    Takes data in the form of a Dictionary
    and build a graph from this data using matplotlib
    The view of graph:
        * x: artists; y: number of albums | number of fans """
    artists = data.keys
    nb_album = [data[i][0] for i in data.keys]
    nb_fan = [data[i][1] for i in data.keys]

    x = np.arange(len(artists))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax_f = pyplot.subplots()
    ax_c = ax_f.twinx()
    ax_f.bar(x - width/2, nb_album[::-1], width,
             label='albums', color='blue')
    ax_c.bar(x + width/2, nb_fan[::-1], width, label='fans')

    ax_f.set_xticks(x)
    ax_f.set_xticklabels(artists[::-1])
    fig.suptitle('The number of albums and fans for the top artists')
    fig.autofmt_xdate(bottom=0.3, rotation=50)
    ax_f.legend(loc = 'upper left')
    ax_c.legend(loc = 'upper right')
    pyplot.show()


def main():
    """ () -> ()
    The main function which:
        * create data with statistic
        * write received data in json file
            'files\\chart_artist.json'
            and save this file in the folder
            'files'
        * visualize data with matplotlib """
    data = get_statistic()
    in_file('files\\chart_artist.json', data)
    visualize_data(data)


if __name__ == "__main__":
    main()
