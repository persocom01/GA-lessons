# Data might have to be further cleaned if impossible values are found.
from python_imports import *

# Load data.
import_path = r'.\PROJECTS-AND-ASSIGNMENTS\project_2\datasets\clean_train.csv'
# Dataset contains NA strings that should not be considered null values.
data = pd.read_csv(import_path, keep_default_na=False, na_values=[''])
df = pd.DataFrame(data)
print(df)


def subplot_dist(df, kind='dist', cols=None, titles=None, xlabels=None, ylabels=None, meanline=False, medianline=False, **kwargs):
    # Accepts all columns if they can be converted to numbers if cols argument
    # is not given.
    if not cols:
        cols = []
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
                cols.append(col)
            except ValueError:
                pass


subplot_dist(df)
