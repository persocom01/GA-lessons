import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mod1

import_path = r'.\DSI_kickstarterscrape_dataset.xlsx'
data = pd.read_excel(import_path)
# Due to inconsistency in how one category is written, it needs to be cleaned.
clean_category = data['category'].replace('Film &amp; Video', 'Film & Video')
data['category'] = clean_category
df = data[data.status != 'live']

# Code used to extract all category types.
# categories = []
# for index, row in data.iterrows():
#     if row['category'] not in categories:
#         categories.append(row['category'])
#
# categories.sort()
# print(categories)

categories = ['Art', 'Comics', 'Dance', 'Design', 'Fashion', 'Film & Video', 'Food',
              'Games', 'Music', 'Photography', 'Publishing', 'Technology', 'Theater']

# Find the number of successful and failed campaigns in all categories.
cat_success = {x: 0 for x in categories}
cat_failure = {x: 0 for x in categories}
for index, row in df.iterrows():
    if row['status'] == 'successful':
        cat_success[row['category']] = cat_success[row['category']] + 1
    else:
        cat_failure[row['category']] = cat_failure[row['category']] + 1

# Generate a list of success percentages for each campaign category.
success_percent = mod1.p_list(cat_success, cat_failure)

categories_renamed = ['Art', 'Comics', 'Dance', 'Design', 'Fashion', 'Film', 'Food',
                      'Games', 'Music', 'Photo', 'Publish', 'Tech', 'Theater']

# Returns evenly spaced intervals for use in the bar chart.
y_pos = np.arange(len(categories_renamed))
plt.bar(y_pos, success_percent, align='center', alpha=0.5)
plt.xticks(y_pos, categories_renamed, fontsize=10)
plt.xlabel('Project type')
plt.ylabel('Success rate (%)')
plt.title('Success rate by Project type')
plt.show()
