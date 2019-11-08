import pandas as pd
# Needed to set axis labels.
import matplotlib.pyplot as plt
import numpy as np
# You need to be explicit when importing modules from scipy.
# scipy.stats does not work.
# Alternatively use: from scipy import stats
import scipy.stats as stats

# Set dataframe.
import_path = r'.\DSI_kickstarterscrape_dataset.xlsx'
data = pd.read_excel(import_path)
df = pd.DataFrame(data, columns=['backers'])

# Set up figure and axes. Even if you don't use the figure, you still need to
# set up the variables this way so axes becomes the correct object.
fig, ax = plt.subplots()

# bins adjusts the number of blocks, range gives the max range of the blocks.
df[(np.abs(stats.zscore(df))) < 3].hist(
    'backers', bins=10, range=(0, 250), ax=ax)

# Set labels.
ax.set_xlabel('Number of backers')
ax.set_ylabel('Number of campaigns')

# Skew is a measure of how frequently the values in a data set reside either
# in the high end or low end of the curve. If most of the values reside in the
# low end, it is called a positive skew, and vice versa.
print(df.skew())
