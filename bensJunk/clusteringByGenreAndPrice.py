# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:58:07 2020

@author: Ben
"""
from sklearn import cluster
import numpy as np

def getAllGenres(data):
    genres = []
    for game in data["genres"]:
        for genre in game.split(";"):
            if not genres.__contains__(genre):
                genres.append(genre)
    return genres

def prepareGamesGenresAndPrice(data,genres):
    gamesGenres = []
    gameIndex = 0
    for game in data["genres"]:
        gameGenres = np.full((1,len(genres)+1), 0, dtype=float).ravel()
        for genre in game.split(";"):
            gameGenres[genres.index(genre)]=1
        gameGenres[len(genres)] = data["price"].values[gameIndex]
        gamesGenres.append(gameGenres)
        gameIndex+1
    return gamesGenres

def genreAndPriceClusterCentroids(data,centroidCount):
    X = prepareGamesGenresAndPrice(data,getAllGenres(data))
    
    kmeans = cluster.KMeans(n_clusters=centroidCount, init="k-means++",n_init=10).fit(X)
    genres = getAllGenres(data)
    centroids = []
    for center in kmeans.cluster_centers_:
        i=0
        gameGenres = []
        for attribute in center: 
            if(attribute>0.5) and i<len(genres):
                gameGenres.append(genres[i])
            if i==len(genres):
                gameGenres.append(attribute)
            i+=1
        centroids.append(gameGenres)
    return centroids

data = pd.read_csv('..\data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

results = genreAndPriceClusterCentroids(data,1000)

for result in results:
    if not (result[len(result)-1]==7.19):
        print(result)
        print(" ")