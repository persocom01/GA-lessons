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
print('initial data shape:', df.shape)
print()

# Print all null values.
print('training set null values:')
for k, v in df.isnull().sum().iteritems():
    if v != 0:
        print(k, v)
print()

# Since the false positive null values have already been screened at the data
# loading stage, we now decide what to do ith the remaining null values.

# lot_frontage:
# If lot_frontage is too weakly correlated to the saleprice, drop it.
print('correlation between lot frontage and saleprice:')
print(df[['lot_frontage', 'saleprice']].corr())
print()
# The correlation between lot_frontage and saleprice is not weak enough.

# If lot_frontage is too strongly correlated to lot_area, drop it.
print('correlation between lot frontage and lot area:')
print(df[['lot_frontage', 'lot_area']].corr())
print()
# The correlation between lot_frontage and saleprice is not strong enough.

df2 = df
df2['lot_frontage'] = df2['lot_frontage'].fillna(0)
print('correlation between lot frontage and saleprice if null values were replaced by 0s')
print(df2[['lot_frontage', 'saleprice']].corr())
print()
# Replacing null values in lot_frontage decreases the correlation between it
# and the target. It is observed that the test data also contains a lot of null
# values for this variable. I decided that the best approach is to replace the
# null values in the train and test data with the mean.
lot_f_mean = df['lot_frontage'].mean()
df['lot_frontage'] = df['lot_frontage'].fillna(lot_f_mean)

# It is observed that most of the null values in the 'garage_yr_blt' variable
# are due to not having a garage in the first place. These values are valid.
# Drop the invalid values, where a garage exists but there is no built year.
invalid_garage_yr_values = df[(df['garage_type'] != 'NA') & (df['garage_yr_blt'].isnull())]
print('number of invalid garage_yr_values:', len(invalid_garage_yr_values.index))
df = df.drop(invalid_garage_yr_values.index)

# The other null valies are confirmed invalid and their rows will be dropped.
other_null_columns = features = [col for col in df.columns if col != 'garage_yr_blt']
df = df.dropna(subset=other_null_columns)

# Confirm remaining null values.
for k, v in df.isnull().sum().iteritems():
    if v != 0:
        print(k, v)
print()

# Check for incorrect datatypes.
for k, v in df.dtypes.iteritems():
    print(k, v)
print()
# All datatypes confirmed to be correct.

for x, v in df.describe(include='object').items():
    print(x, v)
# print())

print('cleaned data shape:', df.shape)
print()

export_path = r'.\PROJECTS-AND-ASSIGNMENTS\project_2\datasets\clean_train.csv'
df.to_csv(export_path)

# ------------------------------------------------------------------------------

# Load data.
import_path = r'.\PROJECTS-AND-ASSIGNMENTS\project_2\datasets\test.csv'
# Dataset contains NA strings that should not be considered null values.
data = pd.read_csv(import_path, keep_default_na=False, na_values=[''])
df2 = pd.DataFrame(data)
# Simplify column names.
df2.columns = [x.lower().replace(' ', '_') for x in df2.columns]

# Print all null values.
print('test set null values:')
for k, v in df2.isnull().sum().iteritems():
    if v != 0:
        print(k, v)
print()

# Since we can't drop any of the test dataset rows, we will have to replace
# them with a representative value if possible.
# Fill continuous variables with the train mean.
df2['lot_frontage'] = df2['lot_frontage'].fillna(lot_f_mean)
df2['mas_vnr_area'] = df2['mas_vnr_area'].fillna(df['mas_vnr_area'].mean())
# Fill norminal variables with the most common type.
df2['mas_vnr_type'] = df2['mas_vnr_type'].fillna(df['mas_vnr_type'].value_counts().keys()[0])
# There is probably a better way to fill nulls in ordinal variables, however,
# for the purpose of this dataset, they will be filled with the most common
# type.
df2['electrical'] = df2['electrical'].fillna(df['electrical'].value_counts().keys()[0])
df2['garage_finish'] = df2['garage_finish'].fillna(df['garage_finish'].value_counts().keys()[0])

export_path = r'.\PROJECTS-AND-ASSIGNMENTS\project_2\datasets\clean_test.csv'
df2.to_csv(export_path)
