# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:53:15 2020

@author: nikscha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Toolbox import apyori as ap

def printRules(association_results):
    for item in association_results:
    
        # first index of the inner list
        # Contains base item and add item
        pair = item[0] 
        items = [x for x in pair]
        
        bought = ""
        for d in items:
            if(d!=items[0]):
                bought = bought + " " + d
        
        print("Rule: " + items[0] + " -> " + bought)
        
        #second index of the inner list
        print("Support: " + str(item[1]))
        
        #third index of the list located at 0th
        #of the third index of the inner list
        
        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))
        print("=====================================")
            
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
        gameGenres = []
        for genre in game.split(";"):
            gameGenres.append(genre)
        gamesGenres.append(gameGenres)
    return gamesGenres
        
def rankedRules(rules):
    rankedRules = []
    for i in range(0,10):
        bestRule = None
        bestVal = 0
        for rule in rules:
            if (not rankedRules.__contains__(rule)):
                if ((item[1]*item[2][0][2])>bestVal):
                    bestRule = rule
                    bestVal = item[1]*item[2][0][2]
        rankedRules.append(bestRule)
    return rankedRules
    
    
data = pd.read_csv('data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

records = prepareGamesGenres(data,getAllGenres(data))
    
association_rules = ap.apriori(records, min_support=0.001, min_confidence=0.001, min_length=2, min_lift = 1.000001)
association_results = list(association_rules)

print(len(association_results)) 
 
for d in rankedRules(association_results):
       print(d)
       print(" ")