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
# loading stage, we now decide what to dow ith the remaining null values. It is
# observed that garage_yr_blt is null for houses with no garage.
print('invalid garage yr values:')
print(df[(df['garage_type'] != 'NA') & (df['garage_yr_blt'].isnull())]
      [['garage_type', 'garage_yr_blt']])
print()
# df = df.dropna()

# Check for incorrect datatypes.
for k, v in df.dtypes.iteritems():
    print(k, v)

# All datatypes confirmed to be correct.
print(df.shape)
