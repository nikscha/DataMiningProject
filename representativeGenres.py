# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:46:28 2020

@author: Ben
"""

import clusterGenres as gClust
import allGenreCombinations as gComb
import numpy as np
import pandas as pd

def getAllGenres(data):
    genres = []
    for game in data["genres"]:
        for genre in game.split(";"):
            if not genres.__contains__(genre):
                genres.append(genre)
    return genres

def genresAsBooleanList(data):
    genres = getAllGenres(data)
    gamesGenres = []
    for game in data["genres"]:
        gameGenres = np.full((1,len(genres)), False, dtype=bool).ravel()
        for genre in game.split(";"):
            gameGenres[genres.index(genre)]=True
        gamesGenres.append(gameGenres)
    return gamesGenres

def error(data,reprGenres):
    gameGenres = genresAsBooleanList(data)
    
    totalError = 0
    for game in gameGenres:
        totalError += lowestError(game,reprGenres)
        
    totalGenres = len(gameGenres)*len(gameGenres[0])
    return totalError/totalGenres

def lowestError(gameG, reprList):
    lowestError = len(gameG)
    for rep in reprList:
        i = 0
        errors = 0
        for genre in rep:
            if not (genre==gameG[i]):
                errors+=1
            i+=1
        if (errors<lowestError):
            lowestError = errors
    return lowestError

data = pd.read_csv('data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

print(str(error(data,gClust.genreClusterCentroids(data,20))) + " average error of the closest aproximator with centroids")
print(str(error(data,gComb.rankedGameGenres(data,20))) + " average error of the closest aproximator with top 10 occuring genre combinations")






















