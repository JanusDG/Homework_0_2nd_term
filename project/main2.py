import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
from matplotlib import style
from os import system
import platform

def clean_screene():
    if platform.system() == "Linux":
        system("clear")
    elif platform.system() == "Windows":
        system("cls")

def research_mode(data):
    all_possible = ["duration", "artist_albums", "album_release_date", "explicit", "album_fans", "artist_fans"]

    clean_screene()
    for item in all_possible:
        print(item, round(show(data, [item]),3))

def show(data, elements):
    columns = elements + ["rank"]
    data = data[columns]
    predict = "rank"

    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    acc = 0
    rate = {}
    for i in range(100):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        predictions = linear.predict(x_test)

        acc = linear.score(x_test, y_test)
        rate[str(acc)] = linear

    best = max([float(item) for item in rate.keys()])
    return best

def run():
    if platform.system() == "Windows":
        SLESH = "\\"
    elif platform.system() == "Linux":
        SLESH = "/"
    
    data = pd.read_csv("data" + SLESH + "tracks.csv", sep=";")
    clean_screene()
    
    all_possible = ["duration", "artist_albums", "album_release_date", "explicit", "album_fans", "artist_fans"]
    
    with open("data"+SLESH+"description.txt", "r") as file:
        lines = file.readlines()

    welcome_lines = lines[:5]
    chosing_lines = lines[6:11]
    description_for_user = lines[12:16]
    description_for_research = lines[17:22]
    conclusion = lines[23:37]

    for line in welcome_lines:
        print(line.strip())
    print()
    input("Press Enter to continue")

    clean_screene()

    for line in chosing_lines:
        print(line.strip())
    print()
    answer = input("Enter 1 for \'research mode\' and 2 for \'user mode\' ")
    while answer not in ["1", "2"]:
        answer = input("Please enter a valid option")
    
    if answer == "1":
        clean_screene()
        for item in description_for_research:
            print(item.strip())
        print()
        input("Press Enter to continue")
        clean_screene()
        research_mode(data)
        print()
        for item in conclusion:
            print(item.strip())
        print()
    else:
        clean_screene()

        for line in description_for_user:
            print(line.strip())
        print()
        for i, value in enumerate(all_possible):
            print(i+1, value)
        

        numbers = input("... ")
        while "," not in numbers and len(numbers) != 1:
            numbers = input("Please enter a valid option ")
        answer = [int(item) for item in numbers.replace(" ","").split(',')]
        elements = [item[1] for item in enumerate(all_possible) if item[0]+1 in answer]
        clean_screene()
        print("With this stats the accuracy of the model is")
        print(show(data, elements))

        for p in elements:
            style.use("ggplot")
            pyplot.scatter(data[p], data["rank"])
            pyplot.xlabel(p)
            pyplot.ylabel("Rank")
            pyplot.show()
