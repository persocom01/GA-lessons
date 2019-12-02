# Part 4

## Overview 

Data science requires clean data, logical study design, and reproducible results. The best way to do this (and build your portfolio) is to get in the habit of fully documenting your work for your peers and colleagues.

In Part 4 you'll assemble a GitHub repo with your full analysis, results and reporting.  Your notebook(s) should be written in a straightforward manner, with concisely commented code, documented procedures and reasoning, and logical analysis. Where applicable, include clearly labeled plots, graphs, and other visualizations, explaining any outliers and relationships between features and data.  Walk us through each portion of your notebook, step by step. 

You should also include a brief "executive summary" that includes your problems statement, a description of your analysis and your key takeaways and results.  Data science reporting is technical, but don’t forget that your approach should tell us a compelling story about your data.

> Your problem statement is critical! Do not leave this out! Also, make sure your key-metrics are tied to every milestone within your findings.

Include any additional code, data, or other materials as appendices in your notebook or separate files, as needed. Above all, your process descriptions should be concise and relevant to your goals.

_Goal_: A fully documented repository for technical stakeholders.

---

## Requirements

1. An executive summary:
  - What is your goal?
  - Where did you get your data?
  - What are your metrics?
  - What were your findings?
  - What risks/limitations/assumptions affect these findings?
2. Summarize your statistical analysis, including:
  - implementation
  - evaluation
  - inference
3. Clearly document and label each section of your notebook(s)
  - Logically organize your information in a persuasive, informative manner.
  - Include notebook headers and subheaders, as well as clearly formatted markdown for all written components.
  - Include graphs/plots/visualizations with clear labels.
  - Comment and explain the purpose of each major section/subsection of your code.
  - Document your code for your future self, as if another person needed to replicate your approach.
4. Clearly document all of your decision points in the relevant sections
  - How did you acquire your data?
  - How did you transform or engineer your data?  Why?
  - How did you select your model?
  - How did you optimize hyperparameters?
5. Host your notebook and any other materials in your own public Github Repository.
  - You repo should have README file that guides us through the repository and links to important files.
  - Include links and explanations to any outside libraries or source code used.
  - Host a copy of your dataset or include a link to a remotely hosted version.

**BONUS**

Create a blog post of at least 1000 words summarizing your approach in a tutorial format and link to it in your notebook.  In your tutorial, address a slightly less technical audience; think back to Day 1 of the program - how would you explain and walk through your capstone project to your earlier self?

### Best Practices

1. The README
  - The README is the landing page of your repo.  
  - It should start with a summary of what the repo contains and provide links to important files.
  - Think of it as a table of contents for your repo.
  - You should list the external libraries/packages that you use, especially if they are not standard (i.e., not part of the base Anaconda distribution.)
  - If you wrote a blog about this project, link to it from your README.
  - Include your website, twitter handle, etc., if you would like.
2. Organizing your repo
  - If you have multiple notebooks, start each filename with a number to assist in organization.
  - Give you notebooks descriptive filenames.  For example,
    - `1_Scraping.ipynb`
    - `2_EDA.ipynb`
    - `3_Model_Development.ipynb`
  - Keep data files in a single folder off the "root" of the repo.
  - Keep documentation/reports in a dedicated folder (like data).
  - If you have any other resources (images or PDFs), keep them in a dedicated folder (called `assets`, for example.)
3. Jupyter Notebooks
  - Data science is a non-linear, iterative process, but your final notebook should contain a linear "narrative."
  - Notebooks should be reproducible, which means that I will get the _same results_ as you did if I clone your repo and run your notebook.  Consider the following:
    - Is your data stored in the repo or available via a link?
    - If you use _any_ (_ANY_) random numbers anywhere, do you have a random seed so that you **always** get the same result?
    - Is your notebook 100% free of runtime errors?
    - In short, if I open your notebook and click "Cell -> Run All", will your notebook run completely, without errors and give me the same result _every_ time?

## Necessary Deliverables / Submission

Your code and technical notebook should be posted to your **personal GitHub** (not **git.generalassemb.ly**) and linked to us no later than  _end of day, August 21, 2019_.

## Useful Resources

- [How to Report Statistics to Technical Audiences](http://abacus.bates.edu/~ganderso/biology/resources/writing/HTWstats.html)
- [What is a good way for a data scientist to construct an online portfolio?](https://www.quora.com/What-is-a-good-way-for-a-data-scientist-to-construct-an-online-portfolio)
