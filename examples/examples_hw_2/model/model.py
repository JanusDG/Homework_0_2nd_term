import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("tracks.csv", sep=";")
# tracks.csv is a file made from the Deezer API data 
# the modules for achieving this file format is one time use
# so i did not put them on git

data = data[["duration", "artist_albums", "album_release_date", "explicit", "rank", "album_fans", "artist_fans"]]
predict = "rank"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.5)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
predictions = linear.predict(x_test)

rez = []
for i in range(len(predictions)):
    mistake = ((abs(predictions[i]-y_test[i])/y_test[i])*100)//1
    if mistake <= 100:
        # not taking anomalies into consideration
        rez.append(mistake)
        print(predictions[i], y_test[i])
        print(f"The mistake is {mistake}%")
        print()

print()
print("the average mistake is",sum(rez)/len(rez))

# as the example i present a graph of dependancy between rank and release date
p = "album_release_date"
style.use("ggplot")
pyplot.scatter(data[p], data["rank"])
pyplot.xlabel(p)
pyplot.ylabel("Rank")
pyplot.show()
