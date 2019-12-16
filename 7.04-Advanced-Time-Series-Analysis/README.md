# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Advanced Time Series Analysis

---

## Materials We Provide


| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Jupyter Notebook | [Link](./starter-code.ipynb)|

> **Dataset description:** Stock Price Data (2005-2013)

---

## Learning Objectives

*After this lesson, students will be able to:*

1. Create a proper train/test split on time series data.
2. Identify when seasonality exists in time series data.
3. Fit and tune a SARIMAX model.
4. Fit a multivariate time series model.
---

## Student Requirements

*Before this lesson(s), students should already be able to:*

1. Interpret autocorrelation and partial autocorrelation plots.
2. Execute and interpret the Augmented Dickey-Fuller test for stationarity.
3. Fit autoregressive, moving average, and ARIMA models.
4. Describe when AR, MA and ARIMA models are appropriate.

---

## Lesson Outline

> **Total Time: 100 mins**

I. **Train/Test Split** (20 minutes total)

II. **Tuning Parameters** (15 minutes total)

III. **Seasonal Models** (40 minutes total)

IV. **Multivariate Models** (20 minutes total)

---

## OPTIONAL: Resources for Practice and Learning

*For supplemental reading material on this topic, check out the following resources:*

- [NIST Documentation on Time Series Analysis](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm)
- [`statsmodels` Documentation for ARIMA Model](http://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_model.ARIMA.html#statsmodels.tsa.arima_model.ARIMA)
- [`statsmodels` Documenation for Exogenous/Endogenous](http://www.statsmodels.org/stable/endog_exog.html)
- [`statsmodels` Documentation for SARIMAX Model](http://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html#statsmodels.tsa.statespace.sarimax.SARIMAX)
- [`sklearn` Documentation for `TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
- [Blog Post on Train/Test Split with Time Series Data](https://machinelearningmastery.com/backtest-machine-learning-models-time-series-forecasting/)
- [Wikipedia Article for Augmented Dickey-Fuller Test](https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test)
- [Guidelines for Tuning Parameters `p`, `d`, `q`](https://people.duke.edu/~rnau/411arim3.htm)
- [Paper on Finding Parameters of Moving Average Models](https://www.it.uu.se/research/publications/reports/2006-022/2006-022-nc.pdf)
- [Table for Identifying Which Model and Method of Differencing to Use](http://people.duke.edu/~rnau/whatuse.htm)
---
