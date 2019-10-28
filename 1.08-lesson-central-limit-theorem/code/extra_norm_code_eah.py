#This code is designed to give a working example of a gaussian fit with 1,2,3 sigma lines. This will provide a working example that will complement lesson 1.5.1
#Elaina A. Hyde
#24 March 2017

#To run: python3 151_extra_norm_code_eah.py
#------------------------------------------------

import numpy as np
import scipy.stats as stats
from scipy.stats import truncnorm
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

#generate points on the x axis:

#Set mean and standard deviation
mu, sigma = 100, 15

#Here is a set of points
xpoints=np.random.normal(mu, sigma, 1000)

avg=np.mean(xpoints)
std=np.std(xpoints)

#check your values
print(avg,std)

#Define variables for 1,2,3 sigma
std1= avg + std
std1_neg=avg - std
std2=avg + 2*std
std2_neg=avg - 2*std
std3=avg + 3*std
std3_neg=avg - 3*std

#Start Figure
#---------------------------------------
# initialize a matplotlib "figure"
fig = plt.figure(figsize=(8,5))

# get the current "axis" out of the figure
ax = fig.gca()

# 68%:
ax.axvline(std1_neg, ls='dashed', lw=3, color='#333333', alpha=0.7)
ax.axvline(std1, ls='dashed', lw=3, color='#333333', alpha=0.7)

ax.axvline(std2_neg, ls='dashed', lw=3, color='#666666', alpha=0.7)
ax.axvline(std2, ls='dashed', lw=3, color='#666666', alpha=0.7)

ax.axvline(std3, ls='dashed', lw=3, color='#999999', alpha=0.7)
ax.axvline(std3_neg, ls='dashed', lw=3, color='#999999', alpha=0.7)

# plot the lines using matplotlib's hist function:
ax.hist(xpoints,normed=True)
plt.show()
#End Figure
#---------------------------------------
