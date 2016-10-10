# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:14:19 2016

@author: jan-felix
"""
import numpy as np
from sklearn import datasets
from sklearn import linear_model
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
import random
import subprocess


####### Creating a Base-Dataset #######

featurenumber = 473     # features (number according to the unterlying paper)
featureinf = 200        # features that provide information

###### Divide into 3 Sets: initial train, new train, test

(X, y) = datasets.make_classification(20000, featurenumber, featureinf )
(X, X_new, y, y_new) = cross_validation.train_test_split(X, y, test_size=0.9, random_state=42)
(X_new, X_test, y_new, y_test) = cross_validation.train_test_split(X_new, y_new, test_size=0.1, random_state=42)


###### Model Set Up ####### 

clf = linear_model.LogisticRegressionCV(max_iter = 200)

###### Training the model with an initial Data-Set #######

clf.fit(X, y)

##### Evaluation of the initial model

y_predtest = clf.predict(X_test)
beg_acc = "Beginning Model Accuracy: " + str(accuracy_score(y_predtest, y_test))


##### MAKING A PREDICTION for new instances ###### 

# 2 for loops to simulate new instances and evaluate model after every 100 new instances
acc = []

for t in range(0,20):

    tp = 0 
    fp = 0 
    new = 0

    for i in range (0,100):
        
        # create a new instance (pick from the model)
        
        s = random.randint(0, len(y_new - 1))
        X_add = X_new[s].reshape(1, -1)
        y_add = np.array(y_new[s]).reshape(1, -1)

        # make prediction for new instance
        
        prediction = clf.predict_proba(X_add)
        pred = clf.predict(X_add)
              
        # evaluate prediction for new instance
        
        if y_add == 0:
            ev = 1 - prediction[0][0]
            #print str(prediction) + " | " + str(y_add) + " | " + str(ev)
            acc.append(ev)
        if y_add == 1:
            ev = 1 - prediction[0][1]
            #print str(prediction) + " | " + str(y_add) + " | " + str(ev)
            acc.append(ev)
            new += 1 
        
        # make A Call if the probability exceeds a threshold value of 0.7
    
        if prediction[0][1] > 0.7:
            
           #print "Detected" 
            if pred == y_add:
                tp += 1 
                subprocess.call(['php /root/rest/call-request.php +4917648314104'])
                break
            else:
                fp += 1
            
            
        # update dataset
            X = np.append(X, X_add)
            X = X.reshape(len(X)/featurenumber, featurenumber)
            y = np.append(y, y_add)
            y = y.ravel()
            
        # update model with new data
            
            clf.fit(X, y)
        # break command for presentation of the mode
        

    ####### Evaluation of new model ######
    
    print "true positives: " + str(tp)
    print "false positives: " + str(fp)
    print "recall: " + str(float(tp)/float(new))
    
    print beg_acc
    y_predtest = clf.predict(X_test)
    print "New Data Model Accuracy: " + str(accuracy_score(y_predtest, y_test))

    


    
