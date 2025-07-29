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

# DATAPOINT 6: Break down datapoint 1 by IT job: front-end, back-end, devops, etc.
# SQL to group compute
with open('IT_by_field.sql') as f:
    it_fields_query = f.read()

it_fields_query_result = pandasql.sqldf(it_fields_query, locals())
filtered_it_fields = it_fields_query_result[
    ~it_fields_query_result['field'].isin(['Unknown']) & ~it_fields_query_result['degree'].isin(['Unknown'])
]

# A: Degrees of front-enders
it_fields_a = filtered_it_fields[filtered_it_fields['field'] == 'Front-end']
datapoint_6a = it_fields_a['degree'].value_counts().sort_values(ascending=False)
df6a = datapoint_6a.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns6a = sns.barplot(
    data=df6a,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns6a.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Degrees of Front-end Developers"
)

total6a = df6a['count'].sum()
for element in sns6a.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total6a * 100
    sns6a.text(
        element.get_width() + total6a*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df6a['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout()

# B: Degrees of back-enders
it_fields_b = filtered_it_fields[filtered_it_fields['field'] == 'Back-end']
datapoint_6b = it_fields_b['degree'].value_counts().sort_values(ascending=False)
df6b = datapoint_6b.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns6b = sns.barplot(
    data=df6b,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns6b.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Degrees of Back-end Developers"
)

total6b = df6b['count'].sum()
for element in sns6b.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total6b * 100
    sns6b.text(
        element.get_width() + total6b*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df6b['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout()

# C: Degrees of full-stackers
it_fields_c = filtered_it_fields[filtered_it_fields['field'] == 'Full-stack']
datapoint_6c = it_fields_c['degree'].value_counts().sort_values(ascending=False)
df6c = datapoint_6c.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns6c = sns.barplot(
    data=df6c,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns6c.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Degrees of Full-stack Developers"
)

total6c = df6c['count'].sum()
for element in sns6c.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total6c * 100
    sns6c.text(
        element.get_width() + total6c*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df6c['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout() 

# D: Degrees of data scientists
it_fields_d = filtered_it_fields[filtered_it_fields['field'] == 'Data Science']
datapoint_6d = it_fields_a['degree'].value_counts().sort_values(ascending=False)
df6d = datapoint_6d.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns6d = sns.barplot(
    data=df6d,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns6d.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Degrees of Data Scientists"
)

total6d = df6d['count'].sum()
for element in sns6d.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total6d * 100
    sns6d.text(
        element.get_width() + total6d*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df6d['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout() 

# 7: Degrees of seniors (new SQL query)
with open('IT_by_field_sr_jr.sql') as f:
    it_fields_sr_jr_query = f.read()

it_fields_sr_jr_query_result = pandasql.sqldf(it_fields_sr_jr_query, locals())
filtered_it_fields_sr_jr = it_fields_sr_jr_query_result[
    ~it_fields_sr_jr_query_result['level'].isin(['Unknown']) & ~it_fields_sr_jr_query_result['degree'].isin(['Unknown'])
]

it_fields_7 = filtered_it_fields_sr_jr[filtered_it_fields_sr_jr['level'] == 'Senior']
datapoint_7 = it_fields_7['degree'].value_counts().sort_values(ascending=False)
df7 = datapoint_7.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns7 = sns.barplot(
    data=df7,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns7.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Degrees of Senior Developers"
)

total7 = df7['count'].sum()
for element in sns7.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total7 * 100
    sns7.text(
        element.get_width() + total7*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df7['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout()

# 8: Degrees of juniors
it_fields_8 = filtered_it_fields_sr_jr[filtered_it_fields_sr_jr['level'] == 'Junior']
datapoint_8 = it_fields_8['degree'].value_counts().sort_values(ascending=False)
df8 = datapoint_8.reset_index().rename(columns={"index": 'degree', 0: 'count'})

plt.figure(figsize=(10, 5))
sns8 = sns.barplot(
    data=df8,
    y='degree',
    x='count',
    orient='h',
    edgecolor="black"
)

sns8.set(
    xlabel="Number of People",
    ylabel="Degree",
    title="Degrees of Junior Developers"
)

total8 = df8['count'].sum()
for element in sns8.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total8 * 100
    sns8.text(
        element.get_width() + total8*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df8['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout()

# DATAPOINT 9: What spheres do people with legal degrees actually work in?
with open('9_query.sql') as f:
    nine_query = f.read()

nine_query_result = pandasql.sqldf(nine_query, locals())
filtered_nine_query = nine_query_result[
    ~nine_query_result['field'].isin(['Unknown'])
]

datapoint_9 = filtered_nine_query['field'].value_counts().sort_values(ascending=False)
df9 = datapoint_9.reset_index().rename(columns={"index": 'field', 0: 'count'})

plt.figure(figsize=(10, 5))
sns9 = sns.barplot(
    data=df9,
    y='field',
    x='count',
    orient='h',
    edgecolor="black"
)

sns9.set(
    xlabel="Number of People",
    ylabel="Field",
    title="Fields of Work for Law Graduates"
)

total9 = df9['count'].sum()
for element in sns9.patches:
    count = int(element.get_width()) # width of the bar in the bar chart = count
    percentage = count/total9 * 100
    sns9.text(
        element.get_width() + total9*0.01, # x position
        element.get_y() + element.get_height()/2, # y position
        f"{count} ({percentage:.1f}%)",
        va="center" # vertical align
    )

plt.xlim(0, df9['count'].max() * 1.3) # xlim() sets the beginning and end of the x axis. This extends x-axis limit to give space for labels
plt.tight_layout()

# What is other in df9
filtered_nine_inv_query = nine_query_result[
    nine_query_result['field'].isin(['Other'])
]
datapoint_10 = filtered_nine_inv_query['title'].value_counts().sort_values(ascending=False)
df10 = datapoint_10.reset_index().rename(columns={"index": 'title', 0: 'count'})
print(df10)

# Maybe I filter the degrees wrong?
datapoint_11 = filtered_nine_query['program'].value_counts().sort_values(ascending=False)
df11 = datapoint_11.reset_index().rename(columns={"index": 'program', 0: 'count'})
print(df11)

# Run
plt.show()