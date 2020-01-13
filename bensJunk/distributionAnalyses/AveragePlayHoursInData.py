# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:37:46 2020

@author: Ben
"""

import pandas as pd
import tools
import matplotlib.pyplot as plt
import numpy as np

def withoutZeroFilter(data):    
    hours,counts = tools.valuesAndCounts(data["average_playtime"])
    hoursByDuration,countsByDuration = tools.countRankedByAttribute(hours, counts)  
    hoursByCount, countsByCount = tools.attributeRankedByCount(hours, counts)  
    tools.median(hoursByDuration)
    tools.average(data["average_playtime"])
    
    
    plt.title("Average playhours and their occurences")
    plt.xlabel("Avg hours")
    plt.ylabel("occurences")
    plt.plot(hoursByDuration,countsByDuration)
    plt.show()
        
    objects = hoursByCount[:10]
    y_pos = np.arange(len(objects))
    performance = countsByCount[:10]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xlabel("playhours")
    plt.ylabel('Occurences')
    plt.title('Top 10 common playtimes')
    plt.show()

def withZeroFilter(data):
    hourData = tools.filteredByValue(data["average_playtime"],0)
    
    hours,counts = tools.valuesAndCounts(hourData)
    hoursByDuration,countsByDuration = tools.countRankedByAttribute(hours, counts)  
    hoursByCount, countsByCount = tools.attributeRankedByCount(hours, counts)  
    tools.median(hoursByDuration)
    tools.average(hourData)
    
    
    plt.title("Average playhours and their occurences, 0 filtered")
    plt.xlabel("Avg hours")
    plt.ylabel("occurences")
    plt.plot(hoursByDuration,countsByDuration)
    plt.show()
        
    objects = hoursByCount[:10]
    y_pos = np.arange(len(objects))
    performance = countsByCount[:10]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xlabel("playhours")
    plt.ylabel('Occurences')
    plt.title('Top 10 common playtimes, 0 filtered')
    plt.show()
    
    
def zeroOccurences(data):
    occurs = [0]
    steps = [""]
    i = 0
    for hours in data["average_playtime"]:
        if i>=500:
            occurs.append(0)
            steps.append(str(500*len(occurs)))
            i=0

        if hours==0:
            occurs[len(occurs)-1]+=1
        i+=1
    
    y_pos = np.arange(len(occurs))
    performance = occurs
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xlabel("0 playhours occurences in data in 500 entry buckets")
    plt.ylabel('Occurences')
    plt.title('0 occurences')
    plt.show()
    
data = pd.read_csv('..\..\data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

zeroOccurences(data)
withoutZeroFilter(data)
withZeroFilter(data)
tools.highestValue(data["average_playtime"])





















