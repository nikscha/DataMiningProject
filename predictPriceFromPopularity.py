# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:36:45 2020

@author: nikscha
"""

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


import time
start_time = time.time()


perceptrons=1 
collum=[16] 


X = pd.read_csv('data/steam.csv', usecols= collum)
Y = pd.read_csv('data/steam.csv',  usecols= [17])

Y=pd.DataFrame(Y).to_numpy().flatten()
Y=Y.astype(int)
X=pd.DataFrame(X).to_numpy()    

for i in range(len(X)):
    X[i][0]=np.average(np.array(X[i][0].split('-')).astype(int))
   
X=X.astype(int)

kf=KFold(n_splits=(10))
for smoothing in range(3):
    avgErrTot=[]
    biggestError=0
    for train,test in kf.split(X):
            X_train, X_test, Y_train, Y_test = X[train],X[test],Y[train],Y[test]
    
            clf=MLPClassifier(hidden_layer_sizes=(perceptrons,))
            clf.fit(X_train,Y_train)
            res=clf.predict(X_test)
                    
            err=[]
           
            for i in range(len(Y_test)):
                err.append(abs(res[i]-Y_test[i]))
            error=np.average(np.array(err))
            avgErrTot.append(error)
            if error >biggestError:
                biggestError=error
            
            #print("avg error: "+str(np.average(np.array(err))))
            
    totalError=np.average(np.array(avgErrTot))
    print("smoothing: "+str(smoothing))
    print("Collum (attribute: "+ str(collum))
    print("nr of perceptrons: "+str(perceptrons))
    print("total avg Error: "+str(totalError))
    print("biggest error diviation: " +str(abs(totalError-biggestError)))
    print("")
    
print("--- %s seconds ---" % (time.time() - start_time))

