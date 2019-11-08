import pandas as pd
import mod1

import_path = r'.\DSI_kickstarterscrape_dataset.xlsx'
data = pd.read_excel(import_path)
df = data[data.status != 'live']

# A list of all months, days and hours is needed to initialize the dictionaries.
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
hours = [x for x in range(0, 24)]

# Find the number of successful and failed campaigns for each month, day
# and hour.
month_success = {x: 0 for x in months}
month_failure = {x: 0 for x in months}
day_success = {x: 0 for x in days}
day_failure = {x: 0 for x in days}
hour_success = {x: 0 for x in hours}
hour_failure = {x: 0 for x in hours}
for index, row in df.iterrows():
    if row['status'] == 'successful':
        # Extracts month day and hour from data by string slicing.
        month = row['funded date'][8:11]
        day = row['funded date'][:3]
        # int() is needed to convert numbers like 05 to 5.
        hour = int(row['funded date'][17:19])
        month_success[month] = month_success[month] + 1
        day_success[day] = day_success[day] + 1
        hour_success[hour] = hour_success[hour] + 1
    else:
        month_failure[month] = month_failure[month] + 1
        day_failure[day] = day_failure[day] + 1
        hour_failure[hour] = hour_failure[hour] + 1

month_success_percent = mod1.p_list(month_success, month_failure)
day_success_percent = mod1.p_list(day_success, day_failure)
hour_success_percent = mod1.p_list(hour_success, hour_failure)

for element in [month_success_percent, day_success_percent, hour_success_percent]:
    df = pd.DataFrame(element)
    print(df.describe())
