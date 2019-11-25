# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

# Project 2 - Ames Housing Data Analysis

### Problem Statement

ABC Real Estate Agents needs a way to predict property sales prices so they may give potential customers a reliable estimate of the value of their property before they decide to engage them to find a buyer.

Currently, 50% of customers express dissatisfaction when the price potential buyers the company finds for their property to be much lower than the price estimates of the company's agents, sometimes resulting in wasted time for the company's agents when sellers change their minds about selling their properties. While such disappointments can be avoided by giving lower property price estimates, there is industry pressure to give a high valuation estimate as it gives sellers the impression that the agent is skilled.

Using data science to come up with a more reliable property price estimate, we can potentially increase customer satisfaction while quoting prices that are competitive in the industry.

---

## Executive Summary

### Contents:

- [Data Cleaning](#Data Cleaning)
- [Exploratory Data Analysis (EDA)](#EDA)
- [Data Dictionary](#Data-Dictionary)
- [Modelling Results](#Modelling-Results)
- [Interpretation of Results](#Interpretation-of-Results)
- [Business Recommendations](#Business-Recommendations)
- [Model Evaluation](#Model-Evaluation)
- [Sources](#Sources)

---

### Data Cleaning

1) Columns were renamed to turn them all to lowercase and replace spaces with underscore.

2) The null values in column 'Lot Frontage' were replaced with mean to retain their correlation to the target and minimize impact on the total number of row in the dataset.

3) Columns deemed useless to the model were dropped.

4) The remaining data was cleaned of null values by dropping the null columns.

### EDA

1) **Ordinal data** was replaced with numbers in ascending order starting from 0 for the worst values.

2) **Categorical data** was converted to numbers via one hot encoding.

3) The distributions were visualized using seaborn.

4) Continuous and ordinal variables that were highly correlated to each other were removed based on their Variance Inflation Factor (VIF) scores.

---

### Data Dictionary:

No new features were added, as such, the original data dictionary may be used. It is found here: http://jse.amstat.org/v19n3/decock/DataDocumentation.txt

---

### Modelling Results

The modelling coefficients may be found here: http://localhost:8888/edit/GA-lessons-clone/PROJECTS-AND-ASSIGNMENTS/project_2/datasets/model_coefficients.csv

---

### Interpretation of Results:

As is expected, the above ground living area made the most impact on the selling prices of the houses, followed by the overall quality. It also appears that the neighborhood the house is in may give it a premium in terms of sales price. Other less significant but still important factors include the quality of the houses' external material and the quality of the kitchen.

Overall, the factors that the models says have an impact on its sales price are within expectations of observable reality. The model though, does give us a better sense of how important each factor is with respect to another.

### Business Recommendations:

While real estate agents no doubt have an idea what may impact a house's sale price, the model is useful in helping give them a rough estimate which they can give to their clients. I recommend it be used so that when making housing price estimates to clients, the real estate agent may be able to claim that the estimate is based on past data and not just the agent's individual intution of market prices.
