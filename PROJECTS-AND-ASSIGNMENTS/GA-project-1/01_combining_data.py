# The objective here is to combine the SAT and ACT datasets so that they may be
# more easily compared.
import pandas as pd

# Read the 2017 SAT file into a DataFrame.
import_path = r'.\data\sat_2017.csv'
data = pd.read_csv(import_path)
df_sat_2017 = pd.DataFrame(data)

# Read the 2017 ACT file into a DataFrame.
import_path = r'.\data\act_2017.csv'
# Removes the "National" row.
data = pd.read_csv(import_path, skiprows=[1])
df_act_2017 = pd.DataFrame(data)

# Merge both DataFrames into one.
df_combined = pd.merge(df_sat_2017, df_act_2017, on='State')

# In order to reduce the number of candidate states, only take state with less
# than 80% participation rate.
df_combined = df_combined[df_combined['Participation_x'].str.strip('%').astype('float') < 80]

# Plot an overlapping bar chart of participation rates.

export_path = r'.\data\sat_act_2017.xlsx'
df_combined.to_excel(export_path)
print(df_combined)
