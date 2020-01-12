# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:20:12 2020

@author: Ben
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('..\data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

def pricesRankedByCount(prices, counts):  
    bestPrices = []
    bestCounts = []
    for i in range(0,len(prices)):
        bestPrice = None
        bestCount = 0
        x = 0
        for count in counts:
            if (not bestPrices.__contains__(prices[x])):
                if (count>bestCount):
                    bestCount=count
                    bestPrice=prices[x]
            x+=1
        bestPrices.append(bestPrice)
        bestCounts.append(bestCount)
    return bestPrices, bestCounts

def pricesRankedByPrice(prices, counts):  
    bestPrices = []
    bestCounts = []
    for i in range(0,len(prices)):
        bestPrice = 1000000
        bestCount = 0
        x = 0
        for count in counts:
            if (not bestPrices.__contains__(prices[x])):
                if (prices[x]<bestPrice):
                    bestCount=count
                    bestPrice=prices[x]
            x+=1
        bestPrices.append(bestPrice)
        bestCounts.append(bestCount)
    return bestPrices, bestCounts
        
def medianPrice(prices,counts):
    X = []
    for i in range(0,len(prices)):
        bestPrice=1000000
        for price in data["price"]:
            if not (X.__contains__(price) and price<bestPrice):
                bestPrice = price
        X.append(price)
    return X[int(len(X)/2)]
    
def pricesAndCounts(data):
    prices = []
    counts = []
    avg = 0
    for price in data["price"]:
        if not prices.__contains__(price):
            prices.append(price)
            counts.append(1)
        else:
            counts[prices.index(price)] +=1
    return prices,counts

def averagePrice(data):
    total = 0
    for price in data["price"]:
        total += price
    return total/len(data["price"])

data = pd.read_csv('..\data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

prices,counts = pricesAndCounts(data)
#averagePrice = averagePrice(data)
pricesByPrices,countsByPrices = pricesRankedByPrice(prices, counts)  
pricesByCount, countsByCount = pricesRankedByCount(prices, counts)  
#medianPrice = medianPrice(orderedPrices,orderedCounts)

plt.title("Prices and their occurences")
plt.xlabel("price")
plt.ylabel("occurences")
plt.plot(pricesByPrices,countsByPrices)
plt.show()
print("Average = " + str(averagePrice))
print("Median = " + str(medianPrice))
print("Capped average = " + str(cappedAverage))

print(pricesByCount[:10])
objects = pricesByCount[:10]
y_pos = np.arange(len(objects))
performance = countsByCount[:10]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Occurences')
plt.title('Top 10 common prices')

plt.show()











