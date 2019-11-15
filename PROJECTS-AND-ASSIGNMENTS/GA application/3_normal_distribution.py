import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

import_path = r'.\PROJECTS-AND-ASSIGNMENTS\GA application\DSI_kickstarterscrape_dataset.xlsx'
data = pd.read_excel(import_path)
df = pd.DataFrame(data, columns=['duration'])
# Necessary as the original structure of a series of arrays could not be
# accepted by the probplot function.
unraveled_df = np.ravel(df.values)

# Use a probability-probability plot to determine is the dataframe is close to
# a normal distribution, represented by the red line.
stats.probplot(unraveled_df, dist="norm", plot=plt)
plt.show()
