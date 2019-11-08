import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import_path = r'.\DSI_kickstarterscrape_dataset.xlsx'
data = pd.read_excel(import_path)
# Divide campaigns into success and failures.
df_success = data[data.status == 'successful']
df_fail = data[data.status == 'failed']

fig, ax = plt.subplots()

a_heights, a_bins = np.histogram(df_success['duration'], range=(0, 100))
b_heights, b_bins = np.histogram(df_fail['duration'], bins=a_bins)

# Sets width of bars.
width = (a_bins[1] - a_bins[0])/5 * 2

ax.bar(a_bins[:-1], a_heights, width=width, facecolor='#77dd77')
ax.bar(b_bins[:-1]+width, b_heights, width=width, facecolor='#ff6961')
plt.title('Durations of successful and unsuccessful campaigns')
ax.set_xlabel('Duration (days)')
ax.set_ylabel('Number of campaigns')
# Set color legend.
ax.legend(labels=['Success', 'Failure'])
plt.show()
