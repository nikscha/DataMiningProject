# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:06:48 2020

@author: nikscha
"""
import pandas as pd
import seaborn as sn
import numpy as np
from scipy import io
import scipy as scipy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import NearestNeighbors as skmd
from sklearn.model_selection import LeaveOneOut
import pandas as pd
from sklearn.model_selection import *
from sklearn.neural_network import MLPClassifier
from Toolbox import MLPPlot as mp
from tools import *

def prepData(X):
   
   
    X=pd.DataFrame(X).to_numpy()    
    X=X[:,13:15]
    for x in range(len(X)):
        for e in range(len(X[x])):
            if X[x,e]==False:
                X[x,e]=0
            elif X[x,e]==True:
                X[x,e]=1
            
    #print(X)
    return X


def test(X,Y):
   
    clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(100,100,100,100))
    clf.fit(X,Y)
    return clf




#        x=x[type(x) in ['int','float','list']]
