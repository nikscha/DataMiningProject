# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:17:40 2020

@author: Ben
"""
import pandas as pd

def getAllGenres(data):
    genres = []
    for game in data["genres"]:
        for genre in game.split(";"):
            if not genres.__contains__(genre):
                genres.append(genre)
    return genres

def prepareGamesGenres(data):
    gamesGenres = []
    occurences = []
    
    for game in data["genres"]:
        if(not gamesGenres.__contains__(game)):
            gamesGenres.append(game)
            occurences.append(0)
        else:
            occurences[gamesGenres.index(game)] += 1
    
    return gamesGenres, occurences

def rankedGameGenres(data, topCount):
    gamesGenres, genreCount = prepareGamesGenres(data)
    
    bestGenres = []
    for i in range(0,topCount):
        bestGenre = None
        bestCount = 0
        x = 0
        for count in genreCount:
            if (not bestGenres.__contains__(gamesGenres[x])):
                if (count>bestCount):
                    bestCount=count
                    bestGenre=gamesGenres[x]
            x+=1
        bestGenres.append(bestGenre)
    return genresAsBooleanList(data,bestGenres)

def genresAsBooleanList(data,bestGenres):
    genres = getAllGenres(data)
    gamesGenres = []
    for bestRepr in bestGenres:
        gameGenres = [False]*len(genres)
        for genre in bestRepr.split(";"):
            gameGenres[genres.index(genre)]=True
        gamesGenres.append(gameGenres)
    return gamesGenres

#data = pd.read_csv('data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

#bestGenres = rankedGameGenres(data, 10)
#print(bestGenres)










    