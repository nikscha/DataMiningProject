# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:53:15 2020

@author: nikscha
"""

print("hey ben")
import scipy as scipy
from scipy import stats
from scipy import io
import matplotlib.pyplot as plt
import numpy as numpy
import pandas as pd

#data=io.loadmat('steam-data-master\analysis\games-features-edit.csv')
from numpy import genfromtxt
gf = pd.read_csv('steam-data-master\analysis\games-features-edit.csv')
print(gf.columns)
gf.head()