### STEP 1: SET UP ENVIRONMENT

import kagglehub
import pandas
import pandasql
import os
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("suriyaganesh/resume-dataset-structured")

print(os.listdir(path)) # find out what files or folders the dataset has

resume_table = pandas.read_csv(f"{path}/01_people.csv");
abilities_table = pandas.read_csv(f"{path}/02_abilities.csv");
education_table = pandas.read_csv(f"{path}/03_education.csv");
experience_table = pandas.read_csv(f"{path}/04_experience.csv");
person_skills_table = pandas.read_csv(f"{path}/05_person_skills.csv");
skills_table = pandas.read_csv(f"{path}/06_skills.csv");

query = "SELECT * FROM resume_table WHERE name = 'Database Administrator'"

result = pandasql.sqldf(query, locals())

# head() prints first five rows
print(result.head()) 

### STEP 2: DATA CLEANING

import resume_data_cleaner as rdc

resume_table_clean = rdc.resume_data_cleaner(resume_table)
abilities_table_clean = rdc.abilities_data_cleaner(abilities_table)
education_table_clean = rdc.education_data_cleaner(education_table)
experience_table_clean = rdc.experience_data_cleaner(experience_table)
person_skills_table_clean = rdc.person_skills_data_cleaner(person_skills_table)
skills_table_clean = rdc.skills_data_cleaner(skills_table)

print(resume_table_clean.head())

### STEP 3: 
### USE SQL TO FIND COOL STUFF WITH  SOME NUMBERS
### USE PANDAS TO UNDERSTAND / COUNT / STATISTICS THE DATA

# DATAPOINT 1: TOTALS

# Apply the SQL query to count the number of people in each degree category
with open('education_query.sql') as f:
    education_query = f.read()

education_query_result = pandasql.sqldf(education_query, locals())

# Remove rows where the degree is 'Unknown'
# ~ is the "not" operator.
filtered_df = education_query_result[
    ~education_query_result['degree'].isin(['Unknown'])
]

# Count the number of people in each degree category
degree_counts = filtered_df['degree'].value_counts()
print(degree_counts)

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
    # Add text label on the bar: total (percentage)
    total = degree_counts.sum()
    sorted_counts = degree_counts.sort_values(ascending=True)
    percentage = (value / total) * 100
    label = f"{value} ({percentage:.1f}%)"
    x_offset = degree_counts.max() * 0.01
    plt.text(value + x_offset, index, label, va='center', fontsize=10)
    # 'value + integer' positions the text slightly to the right of the bar
    # 'index' corresponds to the degree title in the sorted order
    # 'va' ensures the text is centered vertically along the bar
    # 'fontsize' adjusts the size of the text

plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add a light grid for readability
plt.xlim(0, degree_counts.max() * 1.3) # # Extend the x-axis limit to give space for labels
plt.tight_layout() 

# Display the plot
plt.show()