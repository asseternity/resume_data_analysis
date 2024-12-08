### SET UP ENVIRONMENT

import os
import kagglehub
import pandas
import pandasql

path = kagglehub.dataset_download("suriyaganesh/resume-dataset-structured")

print(os.listdir(path))

resume_table = pandas.read_csv(f"{path}/01_people.csv");
abilities_table = pandas.read_csv(f"{path}/02_abilities.csv");
education_table = pandas.read_csv(f"{path}/03_education.csv");
experience_table = pandas.read_csv(f"{path}/04_experience.csv");
person_skills_table = pandas.read_csv(f"{path}/05_person_skills.csv");
skills_table = pandas.read_csv(f"{path}/06_skills.csv");

query = "SELECT * FROM resume_table WHERE name = 'Database Administrator'"

result = pandasql.sqldf(query, locals())

# print(result.head()) # head() prints first five rows

### DATA CLEANING

import resume_data_cleaner as rdc

resume_table_clean = rdc.resume_data_cleaner(resume_table)
abilities_table_clean = rdc.abilities_data_cleaner(abilities_table)
education_table_clean = rdc.education_data_cleaner(education_table)
experience_table_clean = rdc.experience_data_cleaner(experience_table)
person_skills_table_clean = rdc.person_skills_data_cleaner(person_skills_table)
skills_table_clean = rdc.skills_data_cleaner(skills_table)

# print(resume_table_clean.head())

### USE SQL TO FIND COOL STUFF WITH  SOME NUMBERS

# 1. Pie chart: people with "developer" in the title - education title includes "computer science", does not, or unknown?

education_query = "SELECT exp.person_id, exp.title, edu.program, CASE WHEN edu.program LIKE '%computer science%' THEN 'Computer Science' WHEN edu.program IS NULL OR edu.program = 'Unknown' THEN 'Unknown' ELSE 'Other' END AS 'degree' FROM experience_table_clean AS exp JOIN education_table_clean AS edu ON exp.person_id = edu.person_id WHERE exp.title LIKE '%developer'"
education_query_result = pandasql.sqldf(education_query, locals())

### USE PANDAS TO UNDERSTAND / COUNT / STATISTICS THE DATA

degree_counts = education_query_result['degree'].value_counts()
# print(degree_counts)

### VISUALIZE

import matplotlib.pyplot as plt

degree_counts.plot(kind='pie',  # Plot as a pie chart
                   autopct='%1.1f%%',  # Display percentage on slices
                   startangle=90,  # Rotate start angle of the chart
                   legend=False)  # Disable legend
plt.title("Degree Distribution for Developers") # Set chart title
plt.ylabel("")  # Remove label for the y-axis
plt.show() # Display the plot