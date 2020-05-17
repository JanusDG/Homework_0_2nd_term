import matplotlib.pyplot as pyplot
from matplotlib import style
from modules.dict_atd import Dictionary
from modules.dict_usage import in_file, get_data_from_URL

url = 'https://api.deezer.com/genre'

def add_to_dict(d, text):
    """ (Dictionary, str) -> NoneType
    Add to the dictionary all words of this text (comment)
    """
    for word in text.split():
        if d[word]:
            d[word] += 1
        else:
            d[word] = 1

def dict_to_sorted_list_max_tree(d):
    """ (Dictionary) -> list
    Sort the data (with number of repeats) and
    return the list with the most popular words
    and numbers of repeats for every word
    """
    lst = [(i, d[i]) for i in d.keys]
    lst.sort(key= lambda x: x[1], reverse= True)
    i = 0
    for _ in range(5):
        if i >= len(lst):
            break
        min = lst[i][1]
        memory = i
        i += 1
        while i < len(lst) and lst[i][1] == min:
            i += 1
        if i > 25:
            i = memory
            break
    return lst[:i]
    
def list_to_dict(lst):
    """ (list) -> Dictionary
    Return the Dictionary which created of this list
    """
    result = Dictionary()
    for key, number in lst:
        result[key] = number
    return result

def get_statistic(genre, name):
    """ (str, str) -> (Dictionary, str)
    Makes requests and finds in received
    files necessary information.
    Create the statistic and return
    this statistic in format Dictionary where:
        * keys: words
        * values: number of repeats """
    if isinstance(genre, int):
        genre_url = f"{url}/{genre}/artists"
        genre_data = get_data_from_URL(genre_url)["data"]

        comments = Dictionary()
        for artist in genre_data:
            art_data = get_data_from_URL(
                f'https://api.deezer.com/artist/{artist["id"]}/comments')
            for com in art_data['data']:
                add_to_dict(comments, com["text"])
            while art_data['next']:
                art_data = get_data_from_URL(art_data['next'])
                for com in art_data['data']:
                    add_to_dict(comments, com["text"])

        maximum = dict_to_sorted_list_max_tree(comments)
        return (list_to_dict(maximum), name)
    else:
        return (False, False)

def choose_genre():
    """ () -> (str, str)/bool
    Give the opportunity for user to choose
    the genre. If the input number doesn't exist,
    return False, else return the id of genre and genre name
    """
    data = get_data_from_URL(url)["data"]
    ids = []
    counter = 1
    for item in data:
        ids.append(item['id'])
        print(str(counter) + '  --->  \t'+ item['name'])
        counter += 1
    genre_id = input("Choose the genre of(enter the number): ")
    try:
        num = int(genre_id) - 1
        return (ids[num], data[num]['name'])
    except:
        return False

def visualize_data(data):
    """ (Dictionary) -> NoneType
    Takes data in the form of a Dictionary
    and build a graph from this data using matplotlib
    The view of graph:
        * x: words; y: number of repeats """
    style.use("ggplot")
    fig, axs = pyplot.subplots()
    axs.bar(list(data.keys), [data[i] for i in data.keys])
    axs.set_ylabel('Number of repeats')
    axs.set_xlabel('words')
    fig.suptitle('The most repeatable comments for genre')
    fig.autofmt_xdate(bottom=0.2, rotation=50)
    pyplot.show()

def main():
    """ () -> ()
    The main function which:
        * create data with statistic
        * write received data in json file
            'files\\comments_genre_ + name + .json'
            and save this file in the folder
            'files'
        * visualize data with matplotlib """
    genre, name = choose_genre()
    data, name = get_statistic(genre, name)
    if data:
        name = name.replace(' ', '_')
        name = name.replace('/', '_')
        in_file('files\\comments_genre_' + name + '.json', data)
        visualize_data(data)
    else:
        print("Enter the right number or comments doesn't exist yet")

if __name__ == "__main__":
    main()
