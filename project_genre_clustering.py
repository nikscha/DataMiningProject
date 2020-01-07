# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:53:15 2020

@author: nikscha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

gf = pd.read_csv('steam-data-master/analysis/games-features-edit.csv',  usecols= [5,6,7,8,9,10,11,12,13,14,15,16,17])

records = []
for i in range(0,12624):
    aSet = []
    for j in range(0, 13):
        if gf.values[i,j]==True:
            aSet.append(gf.columns[j])
    records.append(aSet)
        
association_rules = apriori(records, min_support=0.0045, min_confidence=0.95, min_length=2)
association_results = list(association_rules)

print(len(association_results))   
#for d in association_results:
#        print(d)
for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    bought = ""
    for d in items:
        bought = bought + " " + d

    print("Rule: " + items[0] + " -> " + bought[len(items[0])+2:])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")