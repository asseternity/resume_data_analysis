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

# Remove rows where the degree is 'Unknown'
# ~ is the "not" operator.
filtered_df = education_query_result[
    ~education_query_result['degree'].isin(['Unknown'])
]

# Count and sort the number of people in each degree category
datapoint_1 = filtered_df['degree'].value_counts().sort_values(ascending=False)

# What I have so far is pandas.Series
# A series isn't a table, it's more like a list of tuples with the label and the value 
# A DataFrame is a table with columns
# reset_index() converts the Series into a table (dataframe)
# now we have columns! they need names
df1 = datapoint_1.reset_index().rename(columns={'index': 'degree', 0: 'count'})

# Create a ranked bar chart with Seaborn
plt.figure(figsize=(10, 5))  # Set figure size
sns1 = sns.barplot(
    data=df1,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

# Add labels and title
sns1.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Ranked Degree Distribution for Developers"
)

# Display value labels on bars
# In plt and Seaborn, a patch is any filled in shape
# So, .patches is the list over which we can iterate to do something to every filled in shape (like a bar in a bar graph) 
total1 = df1['count'].sum()
for element in sns1.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total1 * 100
    sns1.text(
        element.get_width() + total1*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df1['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout() 

# DATAPOINT 2: WHAT FIELD OF IT DO LAWYERS GO TO?
with open('only_lawyers.sql') as f:
    only_lawyers_query = f.read()

only_lawyers_query_result = pandasql.sqldf(only_lawyers_query, locals())
datapoint_2 = only_lawyers_query_result['field'].value_counts().sort_values(ascending=False)
df2 = datapoint_2.reset_index().rename(columns={'index': 'field', 0: 'count'})

plt.figure(figsize=(13, 7))
sns2 = sns.barplot(
    data=df2,
    y='count',
    x='field',
    orient='v',
    edgecolor="black"
)

sns2.set(
    xlabel="Number of people",
    ylabel="IT Field",
    title="Fields of IT that Law Graduates Work In"
)

total2 = df2['count'].sum()
for element in sns2.patches:
    count = element.get_height()
    percentage = count/total2 * 100
    sns2.text(
        element.get_x(),
        count + df2['count'].max()*0.01,
        f"{count} ({percentage:.1f}%)",
        va="bottom", # vertical align
    )

plt.xticks(rotation=45, ha="right") # Rotate the x-axis labels
plt.ylim(0, df2['count'].max() * 1.1)
plt.tight_layout() 
# plt.show()

# DATAPOINT 3: THE OPPOSITE OF 1 - WHAT DEGREES DO PEOPLE WORKING IN LAW HAVE?
with open('lawyers_degrees.sql') as f:
    lawyers_degrees_query = f.read()

lawyers_degrees_query_result = pandasql.sqldf(lawyers_degrees_query, locals())
filtered_lawyers_degrees = lawyers_degrees_query_result[
    ~lawyers_degrees_query_result['degree'].isin(['Unknown'])
]
datapoint_3 = filtered_lawyers_degrees['degree'].value_counts().sort_values(ascending=False)
df3 = datapoint_3.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns3 = sns.barplot(
    data=df3,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns3.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Ranked Degree Distribution for Legal Workers"
)

total3 = df3['count'].sum()
for element in sns3.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total3 * 100
    sns3.text(
        element.get_width() + total3*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df3['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout() 

# DATAPOINT 4: Why so many legal workers are with different degrees?
with open('lawyers_jobs.sql') as f:
    lawyers_jobs_query = f.read()

lawyers_jobs_query_result = pandasql.sqldf(lawyers_jobs_query, locals())
filtered_lawyers_jobs = lawyers_jobs_query_result[
    ~lawyers_jobs_query_result['position'].isin(['Unknown']) & ~lawyers_degrees_query_result['degree'].isin(['Unknown'])
]
datapoint_4 = filtered_lawyers_jobs['position'].value_counts().sort_values(ascending=False)
df4 = datapoint_4.reset_index().rename(columns={"index": 'position', 0: 'count'})

plt.figure(figsize=(10, 5))
sns4 = sns.barplot(
    data=df4,
    y='position',
    x='count',
    orient='h',
    edgecolor="black"
)

sns4.set(
    xlabel="Number of People",
    ylabel="Position",
    title="Positions of Legal Workers"
)

total4 = df4['count'].sum()
for element in sns4.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total4 * 100
    sns4.text(
        element.get_width() + total4*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df4['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout() 
plt.show()

# DATAPOINT 5: Now we remove secretaries, assistants and paralegals, and see what degrees lawyers have
only_senior_lawyers = lawyers_jobs_query_result[
    ~lawyers_jobs_query_result['position'].isin(['Unknown', 'Assistant', 'Secretary', 'Paralegal']) & ~lawyers_jobs_query_result['degree'].isin(['Unknown'])
]
datapoint_5 = only_senior_lawyers['degree'].value_counts().sort_values(ascending=False)
df5 = datapoint_5.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns5 = sns.barplot(
    data=df5,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns5.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Degrees of Lawyers (without Paralegals, Secretaries and Assistants)"
)

total5 = df5['count'].sum()
for element in sns5.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total5 * 100
    sns5.text(
        element.get_width() + total5*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df5['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout() 
plt.show()

# DATAPOINT 6: What spheres do people with legal degrees actually work in?
# DATAPOINT 7: Break down datapoint 1 by IT job: front-end, back-end, devops, etc.