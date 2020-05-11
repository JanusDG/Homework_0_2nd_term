# from modules.genre_artist_fan import main as genre_art_fan
from modules.genre_artist_fan import visualize_data as vis_genre_art
# from modules.comments_genre import main as com_genre
from modules.comments_genre import choose_genre, get_statistic, visualize_data
from modules.chart_artist import main as chart_art
from modules.chart_album_genre import main as chart_alb
from modules.dict_atd import Dictionary
from modules.dict_usage import in_file, json_to_dict
import platform

class Editor:
    """ Clas for editor representation """
    if platform.system() == "Windows":
        SLESH = "\\"
    elif platform.system() == "Linux":
        SLESH = "/"

    def __init__(self):
        """ (Editor) -> NoneType
        Creates tne menu for commands """
        self.menu_map = Dictionary()
        self.menu_map["1"] = self.genre_art_fan_editor
        self.menu_map["2"] = self.com_genre_editor
        self.menu_map["3"] = self.chart_art_editor
        self.menu_map["4"] = self.chart_alb_editor
        self.menu_map["exit"] = self.system_exit

    def genre_art_fan_editor(self):
        """ function for realising the statistic:
            * Distribution of artists and fans by genre * """
        # genre_art_fan()
        path = 'files' + self.SLESH + 'genre_artist_fan.json'
        data = json_to_dict(path)
        print('Data is in file', path)
        vis_genre_art(data)
        self.system_exit()

    def com_genre_editor(self):
        """ function for realising the statistic:
            * The most popular words in comments in the same genre *
            Imortant: method can be realised for a long time.
            But if json file with statistic for the same genre already
            exist, the function will use this file.
            if you want to update the file, then comment all code
            before self.system_exit() and uncomment com_genre() """
        # com_genre()
        genre, name = choose_genre()
        if isinstance(genre, int):
            name = name.replace(' ', '_')
            try:
                path = 'files' + self.SLESH + 'comments_genre_' + name + '.json'
                data = json_to_dict(path)
                print('Data is in file', path)
            except Exception:
                data, name = get_statistic(genre, name)
                name = name.replace(' ', '_')
                in_file('files' + self.SLESH + 'comments_genre_' + name + '.json', data)
            if data:
                visualize_data(data)
            else:
                print("Enter the right number or comments doesn't exist yet")
        else:
            print("Enter the right number or comments doesn't exist yet")
        self.system_exit()

    def chart_art_editor(self):
        """ function for realising the statistic:
            * Numbers of albums and fans for artists of the chart * """
        chart_art()
        self.system_exit()

    def chart_alb_editor(self):
        """ function for realising the statistic:
            * Distribution of chart albums by genre and fans by albums * """
        chart_alb()
        self.system_exit()

    def system_exit(self):
        """
        Function for exiting from the system (stop program)
        """
        raise SystemExit()

    def menu(self):
        """ the main function
        Offer to user to choose one of the command.
        After it, realise command """
        answer = ""
        while True:
            print(
                """
Please choose the statistic (enter a number) or enter exit:
\t 1 \t Distribution of artists and fans by genre
\t 2 \t The most popular words in comments in the same genre
\t 3 \t Numbers of albums and fans for artists of the chart
\t 4 \t Distribution of chart albums by genre and fans by albums
\t   \t (the genre is specified before the album title)

\t exit \t Exit
"""
            )
            answer = input("enter a command: ").lower()
            func = self.menu_map[answer]
            if func:
                func()
            else:
                print("{} is not a valid option".format(answer))


if __name__ == "__main__":
    Editor().menu()
