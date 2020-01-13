# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:20:12 2020

@author: Ben
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tools

data = pd.read_csv('..\..\data\steam.csv',  usecols= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

prices,counts = tools.valuesAndCounts(data["price"])
pricesByPrices,countsByPrices = tools.countRankedByAttribute(prices, counts)  
pricesByCount, countsByCount = tools.attributeRankedByCount(prices, counts)  
tools.median(data["price"])
tools.average(data["price"])

plt.title("Prices and their occurences")
plt.xlabel("price")
plt.ylabel("occurences")
plt.plot(pricesByPrices,countsByPrices)
plt.show()

objects = pricesByCount[:10]
y_pos = np.arange(len(objects))
performance = countsByCount[:10]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Occurences')
plt.title('Top 10 common prices')
plt.show()











