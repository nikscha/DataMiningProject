# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:59:25 2020

@author: nikscha
"""
perceptrons=100
collum=14


X = pd.read_csv('data/steam.csv', usecols= [collum])
Y = pd.read_csv('data/steam.csv',  usecols= [17])

Y=pd.DataFrame(Y).to_numpy().flatten()
Y=Y.astype(int)
X=pd.DataFrame(X).to_numpy()    



kf=KFold(n_splits=(10))
for smoothing in range(3):
    avgErrTot=[]
    biggestError=0
    for train,test in kf.split(X):
            X_train, X_test, Y_train, Y_test = X[train],X[test],Y[train],Y[test]
    
            clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(perceptrons,perceptrons))
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
