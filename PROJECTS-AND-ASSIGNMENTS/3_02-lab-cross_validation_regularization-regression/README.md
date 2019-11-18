# Evaluating and Tuning Regression

This lab is a two-parter.

1. [Part 1](./part_1-train-test-cross-validation.ipynb) will guide you through various evaluations of a linear regression model developed for the Boston housing dataset.  You will explore train-test splitting for various split ratios, then compare and contrast that with cross validation.
2. [Part 2](./part_2-kobe-shots-made.ipynb) will take you through an examination of Kobe Bryant's shooting performance!  You will have tons of data that will lead to overfitting... unless you can stop it!  You will use regularization to tame the data hoard.  If successful, you will turn an overwhelming mountain of data into an insightful model.

The datasets are different between parts 1 and 2, but you will leverage what you practice in part 1 (effectively evaluating model performance) in part 2.  The goal of regularization is to reduce _variance_ in your model.  How do you know if you have been successful at this task?  You need to evaluate how your model will _generalize_, and that, my friends, can be estimated using train/test splits or cross validation.

Finally, in both parts, you will be practicing the data science workflow.  Loading data; exploring and cleaning your data; then building and evaluating a model.
