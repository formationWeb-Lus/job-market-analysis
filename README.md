# Job Market Data Analysis

## Overview

As a software engineer, I am developing my skills in data analysis by learning how to work with real-world datasets and extract useful information from raw data. This project focuses on analyzing job market data to better understand the technical skills required by employers and salary differences between different job families.

The dataset contains information about job postings, including job titles, companies, locations, job sources, job types, work-from-home information, salary information, technical skills, and job families.

The dataset used in this project is stored in the following file:


data/job_market.xlsx


The dataset was obtained from a publicly available job market dataset containing job posting information.

The purpose of this software is to analyze job market data using Python and identify useful patterns in the available job postings. The program loads and cleans the dataset, converts salary information into numerical values, analyzes technical skills, groups job postings by job family, calculates average salaries, and creates visualizations.

The project contains **32 job postings and 49 columns**. After cleaning the salary data, **31 job postings** were used for the salary analysis.

The analysis focuses on two main questions:

1. Which technical skills are most demanded in the job market?
2. What is the average salary for each job family?

The project also generates a graph showing the most demanded technical skills.

### Software Demo Video

The demonstration video will show the dataset, the two questions, the program running, the analysis results, the generated graph, and a walkthrough of the Python code.

[Software Demo Video](http://youtube.link.goes.here)



# Data Analysis Results

## Question 1: Which technical skills are most demanded in the job market?

To answer this question, the program analyzes the technical skill columns in the dataset. Each skill is represented by a column beginning with `skill_`.

The program converts the skill values into numeric values and counts how many job postings require each technical skill. The results are then sorted from the most demanded skill to the least demanded skill.

The analysis found that **Excel** is the most frequently requested technical skill in this dataset.

### Top 10 Most Demanded Technical Skills

| Rank  Technical Skill | Job Postings | Percentage 
    1  Excel                      31       96.9% 
    2  Kubernetes                 21       65.6% 
    3  Flutter                    21       65.6% 
    4   Node.js                    21      65.6% 
    5  Networking                 21       65.6% 
    6  Linux                      21       65.6% 
    7  JavaScript                 21       65.6% 
    8  HTML/CSS                   21       65.6% 
    9  Firebase                   21       65.6% 
    10  Docker                    21       65.6% 

### Answer to Question 1

**Excel is the most demanded technical skill in the dataset.**

It appears in **31 out of 32 job postings**, representing **96.9%** of the analyzed job postings.

This result was obtained using data aggregation and sorting. The program sums the occurrences of each skill and then sorts the results in descending order.

The result shows that Excel is highly represented among the job postings included in this dataset. However, this result only describes the 32 job postings in the dataset and should not be interpreted as a complete representation of the entire global job market.


## Question 2: What is the average salary for each job family?

To answer this question, the program first converts the salary values into numeric values.

The dataset initially contains **32 job postings**. One salary value was excluded from the salary analysis because it did not meet the minimum annual salary threshold used to remove unrealistic salary values.

Therefore:

* Job postings before salary filtering: **32**
* Job postings used for salary analysis: **31**

The program then groups the job postings by `job_family` and calculates the average salary for each group.

### Average Salary by Job Family

 Job Family                 Average Salary 

 Management                    $125,000.00 
 Data & Analytics             $113,937.50 
 Software Development          $102,916.67 
 IT & Infrastructure           $100,500.00 
 Marketing & Sales              $79,166.67 
 Operations & Supply Chain      $78,750.00 
 Accounting & Finance           $75,625.00 
 Human Resources                $70,000.00 

### Answer to Question 2

The analysis shows different average salaries across the job families represented in the dataset.

The **Management** job family has the highest average salary in this dataset, with an average of:

**$125,000.00 per year.**

The average salaries for the other job families range from **$70,000.00** for Human Resources to **$113,937.50** for Data & Analytics, with the remaining job families falling between these values.

These results were obtained using data conversion, filtering, grouping, aggregation, and sorting with Pandas.

The salary results describe the job postings contained in this particular dataset. They do not represent guaranteed salaries for every position within a job family.



# Data Visualization

The program creates a visualization of the most demanded technical skills.

The generated graph is saved as:


top_10_technical_skills.png


The graph makes it easier to compare the number of job postings associated with each of the top technical skills.

The visualization supports the first question by providing a visual representation of the skill demand found in the dataset.



# Development Environment

## Development Tools

The software was developed using the following tools:

* **Visual Studio Code** — used as the main development environment.
* **Python** — used to write the data analysis program.
* **Pandas** — used for loading, cleaning, transforming, filtering, grouping, and analyzing the dataset.
* **NumPy** — used for numerical operations.
* **Matplotlib** — used to create data visualizations.
* **Microsoft Excel** — used to inspect and work with the Excel dataset.
* **Git/GitHub** — used for source code management and project version control.

## Programming Language

The project was developed using **Python**.

The main libraries used are:

### Pandas

Pandas is used to work with the Excel dataset and perform data analysis operations such as:

python
pd.read_excel()
pd.to_numeric()
groupby()
sum()
mean()
sort_values()


For example, the dataset is loaded using:


df = pd.read_excel(data_path)


### NumPy

NumPy is used for numerical operations and calculations.

### Matplotlib

Matplotlib is used to create graphs that visually represent the analysis results.

The project generates a graph of the top 10 most demanded technical skills.



# Data Processing

The program follows several steps to analyze the dataset.

## 1. Load the Dataset

The program loads the Excel file using Pandas:


data/job_market.xlsx


The dataset contains:

* 32 job postings
* 49 columns

## 2. Explore the Dataset

The program displays the available columns and previews the first five job postings.

This makes it possible to understand the structure of the dataset before performing the analysis.

## 3. Clean the Data

The salary values are converted into numeric values so they can be used in mathematical calculations.

The program also identifies unrealistic salary values and excludes them from the salary analysis.

## 4. Analyze Technical Skills

The program identifies columns beginning with:


skill_


It converts their values into numeric values and calculates how many job postings contain each skill.

The results are sorted to identify the most frequently requested skills.

## 5. Analyze Salaries

The program groups job postings by:


job_family


It then calculates the average salary for each job family.

This allows the program to compare salary levels across different categories of jobs.

## 6. Create Visualizations

The program uses Matplotlib to generate a graph showing the top 10 technical skills.



# Dataset Summary

The dataset contains information about job postings from different companies and locations.

Important columns include:


job_title
company
location
source
job_type
work_from_home
salary_average
salary_minimum
salary_maximum
skills
posted_timedelta
job_family


The dataset also contains technical skill indicators such as:


skill_excel
skill_python
skill_javascript
skill_docker
skill_linux
skill_networking
skill_node_js
skill_react
skill_power_bi
skill_aws
skill_csharp
skill_cybersecurity


This structure makes the dataset useful for analyzing relationships between job categories, salaries, and technical skills.


# Useful Websites

The following websites were useful for developing this project and learning about Python data analysis.

* [Python Documentation](https://docs.python.org/3/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [NumPy Documentation](https://numpy.org/doc/)
* [Matplotlib Documentation](https://matplotlib.org/stable/)
* 



# Future Work

The project can be improved in several ways in the future.

* Collect a larger dataset containing more job postings.
* Include job postings from additional countries and regions.
* Analyze technical skills by individual job family.
* Analyze the relationship between specific technical skills and salary.
* Compare salaries by location.
* Analyze salary ranges instead of only average salaries.
* Add more historical job market data to analyze changes over time.
* Improve the trend analysis using a larger historical dataset.
* Use machine learning techniques to develop more advanced salary or job-market predictions.
* Add an interactive dashboard for exploring the dataset.
* Automate the collection of new job postings from publicly available sources.
* Add additional visualizations for salaries, locations, job families, and technical skills.
