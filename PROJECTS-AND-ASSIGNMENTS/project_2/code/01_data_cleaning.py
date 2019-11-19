# ask about scaling, f test.
from python_imports import *

# import os
# print(os.getcwd())
# Change working directory.
# To go back up, use os.chdir('..').
# os.chdir(os.getcwd() + r'\files')

# Load data.
import_path = r'.\PROJECTS-AND-ASSIGNMENTS\project_2\datasets\train.csv'
# Dataset contains NA strings that should not be considered null values.
data = pd.read_csv(import_path, keep_default_na=False, na_values=[''])
df = pd.DataFrame(data)
# Simplify column names.
df.columns = [x.lower().replace(' ', '_') for x in df.columns]
print(df.shape)
print()

# Print all null values.
for k, v in df.isnull().sum().iteritems():
    if v != 0:
        print(k, v)
print()

# Since the false positive null values have already been screened at the data
# loading stage, we now decide what to do ith the remaining null values. It is
# observed that garage_yr_blt is null for houses with no garage.

# If lot_frontage is too weakly correlated to the saleprice, drop it.
print(df[['lot_frontage', 'saleprice']].corr())
# The correlation between lot_frontage and saleprice is not weak enough.

# If lot_frontage is too strongly correlated to lot_area, drop it.
print(df[['lot_frontage', 'lot_area']].corr())
# The correlation between lot_frontage and saleprice is not strong enough.

df2 = df
df2['lot_frontage'] = df2['lot_frontage'].fillna(0)
print(df2[['lot_frontage', 'saleprice']].corr())
# Replacing null values in lot_frontage decreases the correlation between it
# and the target. Thus I decided to drop the null rows.
df = df.dropna(subset=['lot_frontage'])

# print('invalid garage yr values:')
# print(df[(df['garage_type'] != 'NA') & (df['garage_yr_blt'].isnull())]
#       [['garage_type', 'garage_yr_blt']])
# print()
# # df = df.dropna()
#
# # Check for incorrect datatypes.
# for k, v in df.dtypes.iteritems():
#     print(k, v)
# # All datatypes confirmed to be correct.
#
# print(df.shape)
