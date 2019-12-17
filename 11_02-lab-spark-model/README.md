# Apache Spark: Model building

Now that we've had some practice building models in Apache Spark, it's time to put your skills to the test!

Using the `datasets/Heart.csv` dataset (credit: ISLR), you will build a binary classification model to predict whether or not the patient has heart disease (`AHD`) given the following features:

- `Age`
- `Sex`
- `ChestPain`
- `RestBP`
- `Chol`
- `Fbs`
- `RestECG`
- `MaxHR`
- `ExAng`
- `Oldpeak`
- `Slope`
- `Ca`
- `Thal`

## Data cleaning
1. Your target column (`AHD`) needs to be run through a `StringIndexer`.
2. `ChestPain` and `Thal` need to be run through a `StringIndexer` **and** a [`OneHotEncoderEstimator`](http://spark.apache.org/docs/latest/ml-features.html#onehotencoderestimator). NOTE: You only need one instance of `OneHotEncoderEstimator` to do both columns


## Train/Test split
1. Split the data into an 80/20 train/test split. Use **42** for your random seed so we can have consistent scores across the board.
2. Paste your best accuracy score from the test set below

**REPLACE THIS WITH YOUR ACCURACY SCORE**

## Publish your notebook
You're going to publish your notebook rather than submitting it in this rep. In DataBricks, select File > Publish and paste your URL below:

**REPLACE THIS WITH YOUR NOTEBOOK URL**
