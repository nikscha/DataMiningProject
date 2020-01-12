# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:41:58 2020

@author: Nikolais_Desktop
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
import xlsxwriter 
import time
start_time = time.time()

workbook = xlsxwriter.Workbook('results.xlsx')
worksheet = workbook.add_worksheet() 
worksheet.write('A1', 'Results of overnight computing') 
worksheet.write('B1', "smoothing itterations: ")
worksheet.write('C1',"Collum (attributes): ")
worksheet.write('D1',"nr of perceptrons: ")
worksheet.write('E1', "total avg Error: ")
worksheet.write('F1',"biggest error diviation: ")
#workbook.close()
#workbook = xlsxwriter.Workbook('results.xlsx')


X = pd.read_csv('data/steam.csv', usecols= [12,13,14,15,16])
Y = pd.read_csv('data/steam.csv',  usecols= [17])

Y=pd.DataFrame(Y).to_numpy().flatten()
Y=Y.astype(int)
X=pd.DataFrame(X).to_numpy()

#X=X[:500]

#transform the string nrOfDownloads to an int
for i in range(len(X)):
        X[i][4]=np.average(np.array(X[i][4].split('-')).astype(int))
X=X.astype(int)
data=X


arguments=[([4],'downloads'),([2,4],'average hours played and downloads'),([0,1],'user ratings'),([0], 'positive user ratings'),([1], 'negative user ratings')]
#neurons=[(1,),(2,),(3,),(1,1),]
neurons=powerset((10,10,20))
print(neurons)
row=1

for argument in arguments:
    print(str(argument)+"---------------------")
    for nrOfNeurons in neurons:
        row+=1
        print(str(nrOfNeurons)+"**************")
        worksheet.write('A'+str(row),argument[1])
        
        
        perceptrons=nrOfNeurons 
        collum=argument[0] 
        
        #taking the right attributes from the dataset
        X=data
        X2=[]
        for x in range(len(X)):
            temp=[]
            for c in collum:
                temp.append(X[x][c])
            X2.append(temp)
        X=np.array(X2)
        avgErrSm=[]
        biggestError=0
        for smoothing in range(1):
            kf=KFold(n_splits=(10))
            avgErrTot=[]
    
            for train,test in kf.split(X):
                    X_train, X_test, Y_train, Y_test = X[train],X[test],Y[train],Y[test]
            
                    clf=MLPClassifier(hidden_layer_sizes=perceptrons)
                    clf.fit(X_train,Y_train)
                    res=clf.predict(X_test)
                            
                    err=[]
                   
                    for i in range(len(Y_test)):
                        err.append(abs(res[i]-Y_test[i]))
                    error=np.average(np.array(err))
                    avgErrTot.append(error)
                    if error >biggestError:
                        biggestError=error
            avgErrSm.append(np.average(np.array(avgErrTot)))
                  
                    
        totalError=np.average(np.array(avgErrSm))
        print("smoothing: "+str(smoothing))
        print("Collum (attribute: "+ str(collum))
        print("nr of perceptrons: "+str(perceptrons))
        print("total avg Error: "+str(totalError))
        print("biggest error diviation: " +str(abs(totalError-biggestError)))
        print("")
        worksheet.write('B'+str(row),str(smoothing))
        worksheet.write('C'+str(row),str(collum))
        worksheet.write('D'+str(row),str(perceptrons))
        worksheet.write('E'+str(row),str(totalError))
        worksheet.write('F'+str(row),str(abs(totalError-biggestError)))
        worksheet.write('G'+str(row),"")
        


   
    
 
    
    
    
    
workbook.close()