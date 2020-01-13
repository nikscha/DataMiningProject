# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 23:21:40 2020

@author: Ben
"""

def attributeRankedByCount(attris, counts):  
    bestAttris = []
    bestCounts = []
    for i in range(0,len(attris)):
        bestAttri = None
        bestCount = 0
        x = 0
        for count in counts:
            if (not bestAttris.__contains__(attris[x])):
                if (count>bestCount):
                    bestCount=count
                    bestAttri=attris[x]
            x+=1
        bestAttris.append(bestAttri)
        bestCounts.append(bestCount)
    return bestAttris, bestCounts

def countRankedByAttribute(values, counts):  
    bestAttris = []
    bestCounts = []
    for i in range(0,len(values)):
        bestAttri = float('inf')
        bestCount = 0
        x = 0
        for count in counts:
            if (not bestAttris.__contains__(values[x])):
                if (values[x]<bestAttri):
                    bestCount=count
                    bestAttri=values[x]
            x+=1
        bestAttris.append(bestAttri)
        bestCounts.append(bestCount)
    return bestAttris, bestCounts
        
def median(attris):
    X = sorted(attris)
    print("Median = " + str(X[int(len(X)/2)]))
    
def average(attris):
    total = 0
    for value in attris:
        total += value
    print("Average = " + str(total/len(attris)))
    
def valuesAndCounts(vals):
    values = []
    counts = []
    for val in vals:
        if not values.__contains__(val):
            values.append(val)
            counts.append(1)
        else:
            counts[values.index(val)] +=1
    return values,counts

def filteredByValue(values, value):
    X=[]
    for v in values:
        if not v==value:
            X.append(v)
    return X

def highestValue(values):
    highest = 0
    for value in values:
        if value > highest:
            highest = value
    print(highest)
    
def lowestValue(values):
    lowest = 0
    for value in values:
        if value < lowest:
            lowest = value
    print(lowest)










