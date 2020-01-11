# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:23:40 2020

@author: nikscha
"""

#price analysis
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





#X = pd.read_csv('steam-data-master/analysis/games-features-edit.csv',  usecols= [5,6,7,8,9,10,11,12,13,14,15,16,17,18])

X = pd.read_csv('data/steam.csv')
Y = pd.read_csv('data/steam.csv',  usecols= [17])
Y=pd.DataFrame(Y).to_numpy().flatten()
Y=Y.astype(int)
#X=prepData(X)
X=pd.DataFrame(X).to_numpy()    
X=X[:,12:17]
for i in range(len(X)):
    X[i][4]=np.average(np.array(X[i][4].split('-')).astype(int))
print(type(X[0][0]))
print(X)

clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(10))
clf.fit(X,Y)
res=clf.predict(X[:50])

for r in res:
    print(r)
print(np.average(res))
print(np.average(Y[:50]))

















def test(X,Y):

    for classo in range(0,4):
        x = X[Y[:,]==classo]
        plt.scatter(x[:,0],x[:,1], label=str(classo))
        plt.legend()
        plt.xlabel("Attribute 1")
        plt.ylabel("Attribute 2")
        plt.title("synth"+str(syntho))
    plt.show()
    neigh = KNeighborsClassifier(n_neighbors=10,metric="euclidean")
    neigh = neigh.fit(X,Y)
    x1 = X[neigh.predict(X)[:,]==0]
    plt.scatter(x1[:,0],x1[:,1])
    plt.xlabel("Attribute 1")
    plt.ylabel("Attribute 2")
    plt.title("synth"+str(syntho))
    plt.show()