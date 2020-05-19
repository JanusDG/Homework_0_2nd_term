from main1 import * 
from main2 import *

def run_project():
    clean_screene()
    print("Welcome to Deezer Music research")
    print("This reaserch is made of 2 parts ")
    print("The first one will show you different")
    print("statistics about music on Deezer")
    print("The second one using a learning model")
    print("will allow you to see how different stats")
    print("of the song influence its popularity")
    print()
    answer = input("Enter 1 for first part "+\
                   "to run and 2 for the second ")

    while answer not in ["1","2"]:
        answer = input("Please enter a valid option ")

    if answer == "1":
        clean_screene()
        editor = Editor()
        editor.menu()
    else:
        run()

if __name__ == "__main__":
    run_project()