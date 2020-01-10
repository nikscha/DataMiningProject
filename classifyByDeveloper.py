# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:53:52 2020

@author: Ben
"""

import scipy as scipy
from scipy import stats
from scipy import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from Toolbox import treeprint as tp


def treeClassifierPrediction(data):
    allGenres = prepareAllGenres(data)
    genres = np.asarray(prepareGamesGenres(data,allGenres))
    prices = preparePrices(data)
    
    clf = tree.DecisionTreeClassifier(criterion = 'gini',min_samples_split=10)
    clf = clf.fit(genres,prices)
    predictions=[]
    for i in range(0,100):
        if not predictions.__contains__(clf.predict([genres[i]])/100):
            predictions.append(clf.predict([genres[i]])/100)
    print(predictions)

def prepareAllGenres(data):
    genres = []
    for game in data["genres"]:
        for genre in game.split(";"):
            if not genres.__contains__(genre):
                genres.append(genre)
    return genres

def prepareGamesGenres(data,genres):
    gamesGenres = []
    for game in data["genres"]:
        gameGenres = np.full((1,len(genres)), False, dtype=bool).ravel()
        for genre in game.split(";"):
            gameGenres[genres.index(genre)]=True
        gamesGenres.append(gameGenres)
    return gamesGenres

def preparePrices(data):
    prices = []
    for price in data["price"]:
        prices.append(int(price*100))
    return prices
            
def errorRate(prediction)
data = pd.read_csv('data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

#print(data.head(0))
#print(data["genres"])
#print(data["price":"publisher"])
#classify(data)

classify(data)
