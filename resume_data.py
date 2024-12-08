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
experience_table = pandas.read_csv(f"{path}/04_experience.csv");
person_skills_table = pandas.read_csv(f"{path}/05_person_skills.csv");
skills_table = pandas.read_csv(f"{path}/06_skills.csv");

query = "SELECT * FROM resume_table WHERE name = 'Database Administrator'"

result = pandasql.sqldf(query, locals())

# print(result.head()) # head() prints first five rows

# Data cleaning

import resume_data_cleaner as rdc

resume_table_clean = rdc.resume_data_cleaner(resume_table)
abilities_table_clean = rdc.abilities_data_cleaner(abilities_table)
education_table_clean = rdc.education_data_cleaner(education_table)
experience_table_clean = rdc.experience_data_cleaner(experience_table)
person_skills_table_clean = rdc.person_skills_data_cleaner(person_skills_table)
skills_table_clean = rdc.skills_data_cleaner(skills_table)

# print(resume_table_clean.head())

# Well then, combine pandas and sql to find cool shit with SOME NUMBERS

