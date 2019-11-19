# ask about scaling, f test.
from python_imports import *

# import os
# print(os.getcwd())
# Change working directory.
# To go back up, use os.chdir('..').
# os.chdir(os.getcwd() + r'\files')

import_path = r'.\PROJECTS-AND-ASSIGNMENTS\project_2\datasets\train.csv'
data = pd.read_csv(import_path)
df = pd.DataFrame(data)
print(df.shape)
print(df.isnull().sum())
