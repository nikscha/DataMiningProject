# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:06:48 2020

@author: nikscha
"""
import pandas as pd

def prepData(X):
    Y=X["PriceInitial"]
    Y=pd.DataFrame(Y).to_numpy().flatten()
    X=pd.DataFrame(X).to_numpy()    
    X=X[:,2:-1]
    for x in X:
        for e in x:
            if e=='FALSE':
                e=0
            elif e=='TRUE':
                e=1
            
    print(X)
    return (X,Y)




#        x=x[type(x) in ['int','float','list']]
