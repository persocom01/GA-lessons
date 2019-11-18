# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Optimization and Gridsearching Hyperparameters

---

## Materials We Provide


| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Optimization and Gridsearching Hyperparameters | [Link](./introduction-to-gridsearching-hyperparameters.ipynb)|

---

## Learning Objectives

*After this lesson, students will be able to:*

1. Describe what the terms gridsearch and hyperparameter mean
2. Build a gridsearching procedure from scratch
3. Apply sklearn's GridSearchCV object with basketball data to optimize a KNN model
4. Use and evaluate attributes of the gridsearch object
5. Describe the pitfalls of searching large hyperparameter spaces


---

## Student Requirements

*Before this lesson(s), students should already be able to:*

1. Have basic command of python data science libraries

---

## Lesson Outline

> **Total Time: 90 mins**

I. **Optimization and Gridsearching Hyperparameters** (90 minutes total)
- What is grid searching? What are hyperparameters?
- Cover basketball dataset  
- Fit a default KNN
- Searching for the best hyperparameters
  - Grid search pseudocode
  - Use `GridSearchCV()`
- A caution on gridsearching
- Independent practice 

---
> **Dataset description:**

To explore the process of gridsearching over sets of hyperparameters, we will use some basketball data. The data below has statistics for 4 different seasons of NBA basketball: 2013-2016.
- This data includes aggregate statistical data for each game.
- The data of each game is aggregated by match for all players.
- Scraped from http://www.basketball-reference.com

*We are interested in predicting whether the home team will win the game or not.* This is a classification problem.


---

## OPTIONAL: Resources for Practice and Learning
