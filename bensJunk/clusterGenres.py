# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:30:50 2020

@author: Ben
"""

from sklearn import cluster
import numpy as np
import pandas as pd


def getAllGenres(data):
    genres = []
    for game in data["genres"]:
        for genre in game.split(";"):
            if not genres.__contains__(genre):
                genres.append(genre)
    return genres

def prepareGamesGenres(data,genres):
    gamesGenres = []
    for game in data["genres"]:
        gameGenres = np.full((1,len(genres)), 0, dtype=int).ravel()
        for genre in game.split(";"):
            gameGenres[genres.index(genre)]=1
        gamesGenres.append(gameGenres)
    return gamesGenres

def genreClusterCentroids(data,centroidCount):
    X = prepareGamesGenres(data,getAllGenres(data))
    kmeans = cluster.KMeans(n_clusters=centroidCount, init="k-means++",n_init=10).fit(X)
    genres = getAllGenres(data)
    centroids = []
    for center in kmeans.cluster_centers_:
        i=0
        gameGenres = []
        for genre in center: 
            if(genre>0.5):
                gameGenres.append(genres[i])
            i+=1
        centroids.append(gameGenres)
    return genresAsBooleanList(data,centroids)

def genresAsBooleanList(data,centroids):
    genres = getAllGenres(data)
    gamesGenres = []
    for centroid in centroids:
        gameGenres = [False]*len(genres)
        for genre in centroid:
            gameGenres[genres.index(genre)]=True
        gamesGenres.append(gameGenres)
    return gamesGenres

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        