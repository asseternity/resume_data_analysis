### STEP 1: SET UP ENVIRONMENT

import kagglehub
import pandas
import pandasql
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

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

### STEP 3: 
### USE SQL TO FIND COOL STUFF WITH  SOME NUMBERS
### USE PANDAS TO UNDERSTAND / COUNT / STATISTICS THE DATA

# DATAPOINT 1: TOTALS

# Apply the SQL query to count the number of people in each degree category
with open('education_query.sql') as f:
    education_query = f.read()

education_query_result = pandasql.sqldf(education_query, locals())

# Remove rows where the degree is 'Unknown' or 'Other'
# ~ is the "not" operator.
filtered_df = education_query_result[
    ~education_query_result['degree'].isin(['Unknown'])
]

# Count and sort the number of people in each degree category
datapoint_1 = filtered_df['degree'].value_counts().sort_values(ascending=True)

# Create a ranked bar chart
plt.figure(figsize=(10, 5))  # Set figure size
datapoint_1.plot(kind='barh', color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel("Number of People")
plt.ylabel("Degree")
plt.title("Ranked Degree Distribution for Developers")

# Display value labels on bars

# To add text label on each bar "total (percentage)", we need to iterate over the counted and sorted data
for index, value in enumerate(datapoint_1):  
    total = datapoint_1.sum()
    sorted_counts = datapoint_1
    percentage = (value / total) * 100
    label = f"{value} ({percentage:.1f}%)"
    x_offset = datapoint_1.max() * 0.01
    # 'value + integer' positions the text slightly to the right of the bar
    # 'index' corresponds to the degree title in the sorted order
    # 'va' ensures the text is centered vertically along the bar
    # 'fontsize' adjusts the size of the text
    plt.text(value + x_offset, index, label, va='center', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add a light grid for readability
plt.xlim(0, datapoint_1.max() * 1.3) # Extend the x-axis limit to give space for labels
plt.tight_layout() 

# Display the plot
plt.show()

# DATAPOINT 2: WHAT FIELD OF IT DO LAWYERS GO TO?
with open('only_lawyers.sql') as f:
    only_lawyers_query = f.read()

only_lawyers_query_result = pandasql.sqldf(only_lawyers_query, locals())
datapoint_2 = only_lawyers_query_result['field'].value_counts().sort_values(ascending=True)

plt.figure(figsize=(10, 5))
datapoint_2.plot(kind="barh", color="green", edgecolor="black")
plt.xlabel("Number of people")
plt.ylabel("IT Field")
plt.title("Fields of IT that law graduates work in")
for index, value in enumerate(datapoint_2):
    total = datapoint_2.sum()
    sorted_counts = datapoint_2
    percentage = (value / total) * 100
    label = f"{value} ({percentage:.1f}%)"
    x_offset = datapoint_2.max() * 0.01
    plt.text(value + x_offset, index, label, va='center', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add a light grid for readability
plt.xlim(0, datapoint_2.max() * 1.3) # Extend the x-axis limit to give space for labels
plt.tight_layout() 
plt.show()

# DATAPOINT 3: THE OPPOSITE OF 1 - WHAT DEGREES DO PEOPLE WORKING IN LAW HAVE?
with open('lawyers_degrees.sql') as f:
    lawyers_degrees_query = f.read()

lawyers_degrees_query_result = pandasql.sqldf(lawyers_degrees_query, locals())
filtered_lawyers_degrees = lawyers_degrees_query_result[
    ~lawyers_degrees_query_result['degree field'].isin(['Unknown',])
]
datapoint_3 = filtered_lawyers_degrees['degree field'].value_counts().sort_values(ascending=True)

plt.figure(figsize=(10, 5))
datapoint_3.plot(kind="barh", color="red", edgecolor="black")
plt.xlabel("People")
plt.ylabel("Degree")
plt.title("Ranked Degree Distribution for Legal Workers")
for index, value in enumerate(datapoint_3):
    total = datapoint_3.sum()
    sorted_counts = datapoint_3
    percentage = (value / total) * 100
    label = f"{value} ({percentage:.1f}%)"
    x_offset = datapoint_3.max() * 0.01
    plt.text(value + x_offset, index, label, va='center', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add a light grid for readability
plt.xlim(0, datapoint_3.max() * 1.3) # Extend the x-axis limit to give space for labels
plt.tight_layout() 
plt.show()