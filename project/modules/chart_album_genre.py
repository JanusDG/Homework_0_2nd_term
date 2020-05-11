import matplotlib.pyplot as pyplot
from matplotlib import style
from modules.dict_atd import Dictionary
from modules.dict_usage import in_file, get_data_from_URL


def get_statistic():
    data = get_data_from_URL(
        'https://api.deezer.com/chart/0/albums')['data']
    results = Dictionary()
    for album in data:
        alb_data = get_data_from_URL(
            f'https://api.deezer.com/album/{album["id"]}')
        
        nb_fan = alb_data["fans"]
        for genre in alb_data["genres"]["data"]:
            if not results[genre["name"]]:
                results[genre["name"]] = Dictionary()
            results[genre["name"]][album['title']] = nb_fan
    return results


def visualize_data(data):
    genres = data.keys
    numbers = [len(data[i]) for i in data.keys]
    nb_fans = [[], []]
    for i in data.keys:
        for j in data[i].keys:
            nb_fans[0].append(i + ':\n' + j)
            nb_fans[1].append(data[i][j])
    style.use("ggplot")
    fig, (ax0, ax1) = pyplot.subplots(nrows=1, ncols=2)
    
    ax0.bar(genres, numbers, color = 'blue')
    ax0.set_ylabel('Number of albums')
    
    ax1.bar(nb_fans[0], nb_fans[1], color = 'purple')
    ax1.set_ylabel('Number of fans')
    fig.suptitle('Distribution of chart albums by genre and fans by albums')
    fig.autofmt_xdate(bottom=0.4, rotation=50)
    fig.set_figwidth(10)
    fig.set_figheight(6)
    pyplot.show()


def main():
    data = get_statistic()
    in_file('files\\chart_album_genre.json', data)
    visualize_data(data)


if __name__ == "__main__":
    main()
