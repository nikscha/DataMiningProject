# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:53:15 2020

@author: nikscha
"""

import pandas as pd
gf = pd.read_csv('steam-data-master/analysis/games-features-edit.csv')
print(gf.columns)
gf.head()
print(gf[0])