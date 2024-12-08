# Setting up my environment

import os
import kagglehub
import pandas
import pandasql

path = kagglehub.dataset_download("suriyaganesh/resume-dataset-structured")

print(os.listdir(path))

resume_table = pandas.read_csv(f"{path}/01_people.csv");
abilities_table = pandas.read_csv(f"{path}/02_abilities.csv");
education_table = pandas.read_csv(f"{path}/03_education.csv");
person_skills_table = pandas.read_csv(f"{path}/05_person_skills.csv");
skills_table = pandas.read_csv(f"{path}/06_skills.csv");

query = "SELECT * FROM resume_table WHERE name = 'Database Administrator'"

result = pandasql.sqldf(query, locals())

print(result.head()) # head() prints first five rows

# Data cleaning

import resume_data_cleaner as rdc

clean_table = rdc.resume_data_cleaner(resume_table)

print(clean_table.head())

# Well then, combine pandas and sql to find cool shit with SOME NUMBERS