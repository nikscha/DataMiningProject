# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:01:06 2020

@author: Nikolais_Desktop
"""

import arff,numpy as np
from sklearn.model_selection import KFold 
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
#%matplotlib inline
import sklearn.model_selection as ss
from sklearn.metrics import roc_curve