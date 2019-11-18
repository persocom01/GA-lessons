# -*- coding: utf-8 -*-

"""
Created on Wed Apr 27 19:43:17 2016; most recently updated 11/26/16
@author: JosephNelson
"""
'''
Introduction
We've discussed overfitting in the context of bias and variance, and we've seen some techniques like regularization that are used to avoid overfitting. In this lesson we'll discuss another method for avoid overfitting that is commonly referred to a the train/test split. The idea is very similar to cross-validation (indeed it is a type of cross-validation) in that we split the dataset into two subsets:
a subset to train our model on, and
a subset to test our model's predictions on
This serves two useful purposes:
We prevent overfitting by not using all the data, and
We have some remaining data to evaluate our model.
While it may seem like a relatively simple idea, there are some caveats to putting it into practice. For example, if you are not careful it is easy to take a non-random split. Suppose we have salary data on technical professionals that is composed 80% of data from California and 20% elsewhere and is sorted by state. If we split our data into 80% training data and 20% testing data we ight inadvertantly select all the California data to train and all the non-California data to test. In this case we've still overfit on our data set because we did not sufficiently randomize the data.
In a situation like this we can use k-fold cross validation, which is the same idea applied to more than two subsets. In particular, we partition our data into k subsets and train on k−1 one of them. holding the last slice for testing. We can do this for each of the possible k−1 subsets.
Demo
Let's explore test-training split with some sample datasets.
'''

% matplotlib inline

from matplotlib import pyplot as plt
# Make the plots bigger
plt.rcParams['figure.figsize'] = 10, 10

import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split

# Load the Boston Housing dataset
columns = "age sex bmi map tc ldl hdl tch ltg glu".split()
diabetes = datasets.load_diabetes()
df = pd.DataFrame(diabetes.data, columns=columns)
y = diabetes.target
# Take a look at the data again
df.head()
df.shape


'''
Scikit-learn has a nice function to split a dataset for testing and training called train_test_split. The test_size keyword argument indicates the proportion of the data that should be held over for testing.
'''

# create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print X_train.shape, y_train.shape
print X_test.shape, y_test.shape


# fit a model
lm = linear_model.LinearRegression()

model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

## The line / model
plt.scatter(y_test, predictions)
plt.xlabel("True Values")
plt.ylabel("Predictions")

print "Score:", model.score(X_test, y_test)     

'''
Now let's try out k-fold cross-validation. Again scikit-learn provides useful functions to do the heavy lifting. The function cross_val_predict returns the predicted values for each data point when it's in the testing slice.
'''

from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics

# Perform 6-fold cross validation
scores = cross_val_score(model, df, y, cv=6)
print "Cross-validated scores:", scores
# Make cross validated predictions
predictions = cross_val_predict(model, df, y, cv=6)
plt.scatter(y, predictions)
accuracy = metrics.r2_score(y, predictions)
print "Cross-Predicted Accuracy:", accuracy