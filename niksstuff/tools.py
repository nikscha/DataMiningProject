# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:06:48 2020

@author: nikscha
"""
import pandas as pd
import seaborn as sn
import numpy as np
from scipy import io
import scipy as scipy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import NearestNeighbors as skmd
from sklearn.model_selection import LeaveOneOut
import pandas as pd
from sklearn.model_selection import *
from sklearn.neural_network import MLPClassifier
from Toolbox import MLPPlot as mp
from tools import *

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1)))

print(powerset((1,2,3)))


def getAllGenres(data):
    genres = []
    for game in data['genres']:
        for genre in game.split(";"):
            if not genres.__contains__(genre):
                genres.append(genre)
    return genres

def prepareGamesGenresAndPrice(data,genres):
    gamesGenres = []
    gameIndex = 0
    for game in data['genres']:
        gameGenres = np.full((1,len(genres)+1), 0, dtype=float).ravel()
        for genre in game.split(";"):
            gameGenres[genres.index(genre)]=1
        gamesGenres.append(gameGenres)
        gameIndex+1
    return gamesGenres