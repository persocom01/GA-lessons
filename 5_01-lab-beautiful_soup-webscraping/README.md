<!---
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Web Scraping with Beautiful Soup Lab

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

In this lab, you will use Beautiful Soup to scrape [ChubbyGrub.com](http://chubbygrub.com) and create a DataFrame of food items from every restaurant. Your DataFrame should look something like this:

| restaurant | category | name    | calories | carbs | fat |
|------------|----------|---------|----------|-------|-----|
| McDonald's | Burgers  | Big Mac | 540      | 45    | 29  |
| Burger King | Burgers  | Whopper | 900      | 51    | 57  |
| ... | ...  | ... | ...      | ...    | ...  |
| Chili's | Ribs  | Shiner Bock® BBQ Ribs | 2310      | 168    | 123  |


**Note**: Your DataFrame should have just over 4,900 rows.

---

## Materials We Provide
<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab |  Web Scraping Jupyter Notebook | [Link](./BeautifulSoup.ipynb)|

---

## Prerequisites
<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:
- Understand basic HTML
- Use inspect to interpret a website's HTML
- Use the request and BeautifulSoup libraries
