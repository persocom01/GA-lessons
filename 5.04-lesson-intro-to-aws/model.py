import time
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=ERROR,
    n_features=20,
    n_informative=20,
    n_redundant=0,
    n_classes=5,
    random_state=42
)

start = time.time()

rf = RandomForestClassifier(
    n_estimators=500,
    random_state=42,
    n_jobs=1
)

print("Fitting model...")
rf.fit(X, y)

end = time.time()

print("Number of seconds this model took to fit:")
print(end - start)

y_pred = pd.Series(rf.predict(X), name="predictions")
y_pred.to_csv("output.csv", header=True)
