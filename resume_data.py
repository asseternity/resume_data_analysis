### SET UP ENVIRONMENT

import os
import kagglehub
import pandas
import pandasql

path = kagglehub.dataset_download("suriyaganesh/resume-dataset-structured")

# print(os.listdir(path)) # find out what files or folders the dataset has

resume_table = pandas.read_csv(f"{path}/01_people.csv");
abilities_table = pandas.read_csv(f"{path}/02_abilities.csv");
education_table = pandas.read_csv(f"{path}/03_education.csv");
experience_table = pandas.read_csv(f"{path}/04_experience.csv");
person_skills_table = pandas.read_csv(f"{path}/05_person_skills.csv");
skills_table = pandas.read_csv(f"{path}/06_skills.csv");

query = "SELECT * FROM resume_table WHERE name = 'Database Administrator'"

result = pandasql.sqldf(query, locals())

# head() prints first five rows
# print(result.head()) 

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

with open('education_query.sql') as f:
    education_query = f.read()

education_query_result = pandasql.sqldf(education_query, locals())

### USE PANDAS TO UNDERSTAND / COUNT / STATISTICS THE DATA

degree_counts = education_query_result['degree'].value_counts()
# print(degree_counts)

### VISUALIZE 1: TOTALS

import matplotlib.pyplot as plt

# Create a ranked bar chart
plt.figure(figsize=(10, 5))  # Set figure size
degree_counts.sort_values(ascending=True).plot(kind='barh', color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel("Number of People")
plt.ylabel("Degree")
plt.title("Ranked Degree Distribution for Developers")

# Display value labels on bars

# Iterate over the sorted degree counts (ascending order)
for index, value in enumerate(degree_counts.sort_values(ascending=True)):  
    # Add text label on the bar: value (+1 for spacing), at the position 'index' (degree title)
    plt.text(value + 1, index, str(value), va='center', fontsize=10)  
    # 'value + 1' positions the text slightly to the right of the bar
    # 'index' corresponds to the degree title in the sorted order
    # 'va' ensures the text is centered vertically along the bar
    # 'fontsize' adjusts the size of the text

plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add a light grid for readability

### VISUALIZE 2: WHAT IS OTHER?

# Filter the 'Other' degrees
other_degree = education_query_result[education_query_result['degree'] == 'Other']

# Limit to the first 100
other_degree_limited = other_degree.head(200)

# Create a new figure for the second page
plt.figure(figsize=(10, 8))  # Set figure size

# Add a long list of "Other" degrees to the second page
plt.text(0.1, 1, '\n'.join(other_degree_limited['program'].values), ha='left', va='top', fontsize=10)

# Hide axes (no need for grid or ticks)
plt.axis('off')

# Title for the page
plt.title('List of "Other" Degrees')

# Display the plot
plt.show()