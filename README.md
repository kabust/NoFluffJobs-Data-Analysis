# NoFluffJobs Python Data Analysis

## Introduction
Project consists of two parts: [Scraping](#scraping-process) and [Data Analysis](#data-analysis). 
I've analyzed Polish region of NoFluffJobs and all information is related to Python vacancies in Poland.
If you want to try it yourself and get the most up-to-date analysis, go to the [instructions](#how-to-run-locally).

## Used technologies
* Scrapy Framework
* Selenium
* NumPy
* Pandas
* MatPlotLib

<hr>

## Scraping process
![demo.gif](demo%2Fdemo.gif)

## Scraped fields
* Title
* Company
* Category
* Remote
* Seniority
* Salary Range
* Must Have Requirements
* Nice to Have Requirements

<hr>

## Data Analysis
Overall, those demos were based on 213 entries after cleaning.

### Navigation:
* [Categories by popularity](#categories-by-popularity)
* [Possibilities to work remotely](#possibilities-to-work-remotely)
* [Mean salary by category](#mean-salary-by-category)
* [Mean salary by seniority](#mean-salary-by-seniority)
* [Top 10 technologies required by category](#top-10-technologies-required-by-category-except-python-itself)

### Categories by popularity
![category_plot.png](analysis%2Fplots%2Fcategory_plot.png)

As we can see, in May 2024 the most demanded field was Data. 
After that goes Backend, DevOps, AI, Testing and Fullstack. 
Other fields doesn't show that significant demand (on NoFluffJobs).

### Possibilities to work remotely
![remote_non_remote_plot.png](analysis%2Fplots%2Fremote_non_remote_plot.png)

Here we can say that 62% of all vacancies offer possibility of the remote work.

### Mean salary by category
![salaries_by_category_plot.png](analysis%2Fplots%2Fsalaries_by_category_plot.png)

On this plot we can see the salary distribution between fields. 
Worth to mention: Project Manager category contains only 1 entry, so it's not that reliable.

### Mean salary by seniority
![salaries_by_seniority_plot.png](analysis%2Fplots%2Fsalaries_by_seniority_plot.png)

This plot tells us that market offers significantly bigger amount of higher seniority vacancies.
Overall, there's ~15 vacancies of Expert/Senior on 1 Mid/Jun/Trainee.

### Top 10 technologies required by category (except Python itself)
![top_technologies_by_categories_plot.png](analysis%2Fplots%2Ftop_technologies_by_categories_plot.png)
Each plot shows what are the most required technologies among different fields.

## How to run locally

Make sure you have Python 3.12 installed

```shell
cd python-technologies-data-analysis
pip install -r requirements.txt
scrapy crawl jobs -O analysis/jobs.csv
python -m analysis.jobs_analysis
```

<i>Note: if you have errors during scraping, just try again. Selenium isn't very reliable, unfortunately.</i>

#### Thank you for your time!
