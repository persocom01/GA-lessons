# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Recurrent Neural Networks

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Intro to RNNs | Slide Deck | [Link](./RNNs.pdf)
| Coding Example | RNN walkthrough | [Link](./starter-code.ipynb)|

## Learning Objectives

*After this lesson, students will be able to:*

1. Preprocess sequence data for RNN modeling
2. Design, train and evaluate an RNN model
3. Create a model that (poorly) predicts the price of Apple's (AAPL) stock

## Lesson Outline

> **Total Time: 90 mins**

I. **Intro to RNNs** (30 minutes total)
- What types of datasets are ideal for RNN models
- How `TimeseriesGenerator` prepares your sequence data for modeling
- Overview of RNN architecture
- The shortcomings of early RNN models
- How LSTM/GRU networks solve the problem of vanishing gradients

II. **RNN walkthrough** (60 minutes total)
- Load in AAPL stock prices + SEC filings
- Train/test split for time series data
- Use `TimeseriesGenerator` to prep our data for modeling
- Design a basic RNN network using GRU layers
