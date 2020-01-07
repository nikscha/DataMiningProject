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





X = pd.read_csv('steam-data-master/analysis/games-features-edit.csv',  usecols= [5,6,7,8,9,10,11,12,13,14,15,16,17,18])

X,Y=prepData(X)
#Y=Y.tolist()
print(type(Y[0]))
print(X)
#X.reshape((1, -1))

kf=KFold(n_splits=10)
for train,test in kf.split(X):
        X_train, X_test, y_train, y_test = X[train],X[test],Y[train],Y[test]
        clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(1,))
        best=0
        for i in range(5):
            clf.fit(X_train,y_train)
            j=clf.score(X_test,y_test)
            best=j if j>best else best
        print(best)
        
clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(1,))
clf.fit(X,y)
plotter = mp.MLPPlot(X,Y,clf)
plotter.plot_boundaries()








def test2(X,Y):
    kf=KFold(n_splits=10)
    for train,test in kf.split(X):
            X_train, X_test, y_train, y_test = X[train],X[test],y[train],y[test]
            clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(1,))
            best=0
            for i in range(5):
                clf.fit(X_train,y_train)
                j=clf.score(X_test,y_test)
                best=j if j>best else best
            print(best)
            
    clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(1,))
    clf.fit(X,y)
    plotter = mp.MLPPlot(X,Y,clf)
    plotter.plot_boundaries()





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