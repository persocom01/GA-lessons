# Spark DataFrames

## Uploading a csv
For today's lecture, you'll need to upload [train.csv](https://www.kaggle.com/c/titanic/data) from Kaggle's Titanic Competition:

1. Download [train.csv](https://www.kaggle.com/c/titanic/data) to your laptop
2. Log into your [DataBricks](https://community.cloud.databricks.com/) account
3. Choose Data > default > Tables "+" (See image below)
4. On the following page, click the "browse" link and upload the csv from your laptop
5. Copy the file path (`/FileStore/tables/train.csv`), we'll use this in the notebook

![](assets/upload.png)

## Importing a Notebook

To get started, you'll need to import the `DataFrames.html` notebook into your [DataBricks](https://community.cloud.databricks.com/) account:

1. Clone this repo to your laptop
2. Log into your [DataBricks](https://community.cloud.databricks.com/) account
3. Choose Workspace > Users > **YOURUSERACCOUNT** > Dropdown > Import (See below)
4. Navigate to and upload the `DataFrames.html` file in this repository

![](assets/import.png)

**NOTE**: When you first run a cell, you'll see the modal window below. Click `Attach and Run`. Since you're on the free plan, it will probably take a while for your cluster to run that first cell.
![](assets/attach.png)
