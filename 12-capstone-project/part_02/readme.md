# Part 2: Problem Statement, EDA and Dataset

## Overview

In this section you will update us on your project, including the project you have chosen, your problem statement, an extensive outline of EDA and modeling to date, the goal of your predictive model, and the data you will use to explore that model. 

**Your data must be fully in hand by this point OR you must have a solid, achievable plan to do so that has been communicated to your local instructor.**

## Requirements

We expect a formatted and complete Jupyter Notebook by end of class on Wednesday July 31st, 2019, which accomplishes the following:

- Identifies which of the three proposals you outlined in your lightning talk you have chosen
- Articulates the main goal of your project (your problem statement)
- Outlines your proposed methods and models
- Defines the risks & assumptions of your data 
- Revises initial goals & success criteria, as needed
- Documents your data source
- Performs & summarizes preliminary EDA of your data

## Formulating your Problem Statement

Your problem statement should the guiding principle for your project.  You can think about this as a "SMART" goal.

- Specific: 
  - What precisely do you plan to do?
  - What type of model will you need to develop?
- Measurable: 
  - What metrics will you be using to assess performance? 
  - MSE? Accuracy? Precision? AUC?
- Achievable: 
  - Is your project appropriately scoped?
  - Is it too aggressive?  Too easy?
  - *Note:* If your project is too big, break it up into smaller pieces.  Sometimes a good project is the simply one part of a larger, longer-term agenda.
- Relevant:
  - Does anyone care about this?
  - Why should people be interested in your results?
  - What value will the completion of your project be adding?
- Time-bound
  - What's your deadline?

---

- **BAD**: I will model emergency room visits.
- **GOOD**: I will build a regression model to predict the number of daily emergency room visits for St. Someone's Hospital.  Model performance will be guided by RMSE, and the model should at least improve upon baseline by 10%.  Baseline is defined as the monthly average of visits over the last 10 years.

---

- **BAD**: I will investigate the aftermarket pricing of sneakers.
- **GOOD**: Specific image and text features of sports sneakers are predictive of determinding wether they will sell for more or less in the aftermarket.  The guiding metric will be area under the ROC curve.

---

- **BAD**: I will explore the link between obesity and blood pressure.
- **GOOD**: I will quantify the association between obesity and blood pressure through regression modeling.
- **BETTER**: As obesity increases, how does blood pressure change?
---

- **BAD**: I will predict that sources of news are liberal or conservative.
- **GOOD**:  I will look at text features to undersatnd how news can be classified as liberal or conservative.
- **BETTER**: Specific text feature frequencies can determine the broader category of news sources using classification.  I will describe what makes each class charactitaristically unique, describe what is both certain and uncertain using precision and recall as success metrics.  Then I will conclude with a description of "why" my model describes potential to predict these two categories.

---

## Data Guidelines

What should you thinking about and looking for as you collect your capstone data?

- Source and format your data
  - Have a way to save data locally (e.g., SQL or CSV), especially if scraping from the web or collecting from an API.
  - Create a data dictionary to accompany your data.
- Perform initial cleaning and munging.
  - Organize your data relevant to your project goals.
  - Write functions to automatically clean and munge data as necessary.
  - Take copious notes, for both others and yourself, describing your assumptions and approach.


## EDA Guidelines

Think about the following as you perform your initial EDA.

- Identify the data types you are working with.
- Examine the distributions of your data, numerically and/or visually.
- Identify outliers.
- Identify missing data and look for patterns of missing data.
- Describe how your EDA will inform your modeling decisions and process.

## Necessary Deliverables / Submission

 Materials must be presented in a Jupyter Notebook stored within a repository on your personal (*not* GA) GitHub. Please submit a link to this repository by the due date ([submission link](https://forms.gle/P8VK1kGDYS8FLdUD8)).
 
### BONUS

- Create roadmap of your project with milestones.
- Write a blog post on what you learned from your EDA.
 
## Useful Resources
 
- [Best practices for data documentation](https://www.dataone.org/all-best-practices) 
- [Describing data visually](http://www.statisticsviews.com/details/feature/6314441/Visualising-Statistics-The-importance-of-seeing-not-just-describing-data.html)
- [WSJ Guide to Information Graphics (book)](https://www.amazon.com/Street-Journal-Guide-Information-Graphics/dp/0393347281)
- [Storytelling with Data (book)](https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257/)
