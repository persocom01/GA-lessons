import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import_path = r'.\DSI_kickstarterscrape_dataset.xlsx'
data = pd.read_excel(import_path)
# Campaigns that are still live are discarded.
data_clean = data[data.status != 'live']
df = pd.DataFrame(data_clean, columns=['goal', 'pledged'])
# Remove unusually high goals.
q = df['goal'].quantile(0.95)
df = df[df['goal'] < q]

# The goal here, is having known the distribution of goals using describe(),
# to split the goals into 10 bins, and compare the mean amount of money each
# goal receives.
goal_bin = [i * 1000 for i in range(1, 11)]
sum = {x: 0 for x in goal_bin}
count = {x: 0 for x in goal_bin}
sum_mean = []
for i in range(1, 11):
    for index, row in df.iterrows():
        # Splits the dataset into 1000 size goal intervals, sums the amount
        # of money that interval receives, and counts the number of rows
        # falling into each interal.
        if row['goal'] > (i - 1) * 1000 and row['goal'] <= i * 1000:
            sum[i * 1000] = sum[i * 1000] + row['pledged']
            count[i * 1000] = count[i * 1000] + 1
    # Knowing the total amount of money each interval receives as well as the
    # number of rows falling into each interval, output a list of means.
    if count[i * 1000] != 0:
        sum_mean.append(sum[i * 1000] / count[i * 1000])
    else:
        sum_mean.append(0)

# Returns evenly spaced intervals for use in the bar chart.
y_pos = np.arange(len(goal_bin))
# Determines the hight and position of each bar.
plt.bar(y_pos, sum_mean, align='center', alpha=0.5)
# Determines the position of the names of each bar.
plt.xticks(y_pos, goal_bin)
plt.xlabel('Pledge goal')
plt.ylabel('Mean pledge')
plt.title('Mean pledge vs Pledge goal')
plt.show()
