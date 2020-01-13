# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 01:06:02 2020

@author: Ben
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tools

def owners(data):
    owners = []
    for approxOwners in data:
        avgOwners=0
        for value in approxOwners.split("-"):
            avgOwners+=int(value)
        owners.append(avgOwners/len(approxOwners.split("-")))
    return owners
    
def divideAll(data,div):
    x = []
    for each in data:
        x.append(each/div)
    return x

data = pd.read_csv('..\..\data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

avgOwners = owners(data["owners"])
tools.lowestValue(avgOwners)
tools.highestValue(avgOwners)
owners,counts = tools.valuesAndCounts(avgOwners)
pricesByPrices,countsByPrices = tools.countRankedByAttribute(owners, counts)  
pricesByCount, countsByCount = tools.attributeRankedByCount(owners, counts)  
tools.median(avgOwners)
tools.average(avgOwners)

plt.title("Ownercounts and their occurences")
plt.xlabel("Ownercount")
plt.ylabel("occurences")
plt.plot(pricesByPrices,countsByPrices)
plt.show()

objects = divideAll(pricesByCount[:9],1000)
y_pos = np.arange(len(objects))
performance = countsByCount[:9]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Occurences')
plt.xlabel("Owners in thousands")
plt.title('Top 9 common Ownercounts')
plt.show()

