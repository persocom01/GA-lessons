from python_imports import *

import_path = r'.\datasets\test.csv'
data = pd.read_csv(import_path)
df = pd.DataFrame(data)
print(df.head())
