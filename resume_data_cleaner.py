def resume_data_cleaner(table):
    # No need to import pandas because the methods are in built to the dataframe object

    # Fill missing values in specific columns with "Unknown"
    table['email'] = table['email'].fillna('Unknown')
    table['phone'] = table['phone'].fillna('Unknown')
    table['linkedin'] = table['linkedin'].fillna('Unknown')

    # Drop rows with any missing values (if there are still any)
    table_no_miss = table.dropna()

    # Standardize column names (lowercase and replace spaces with underscores)
    table_no_miss.columns = table_no_miss.columns.str.lower().str.replace(' ', '_')

    # Drop duplicate rows
    table_no_miss_no_duplicates = table_no_miss.drop_duplicates()

    return table_no_miss_no_duplicates

def abilities_data_cleaner(table):
    # Fill missing values in specific columns with "Unknown"
    table['ability'] = table['ability'].fillna('Unknown')

    # Drop rows with any missing values (if there are still any)
    table_no_miss = table.dropna()

    # Standardize column names (lowercase and replace spaces with underscores)
    table_no_miss.columns = table_no_miss.columns.str.lower().str.replace(' ', '_')

    # Drop duplicate rows
    table_no_miss_no_duplicates = table_no_miss.drop_duplicates()

    return table_no_miss_no_duplicates

def education_data_cleaner(table):
    # Fill missing values in specific columns with "Unknown"
    table['institution'] = table['institution'].fillna('Unknown')
    table['program'] = table['program'].fillna('Unknown')
    table['start_date'] = table['start_date'].fillna('Unknown')
    table['location'] = table['location'].fillna('Unknown')

    # Drop rows with any missing values (if there are still any)
    table_no_miss = table.dropna()

    # Standardize column names (lowercase and replace spaces with underscores)
    table_no_miss.columns = table_no_miss.columns.str.lower().str.replace(' ', '_')

    # Drop duplicate rows
    table_no_miss_no_duplicates = table_no_miss.drop_duplicates()

    return table_no_miss_no_duplicates

def experience_data_cleaner(table):
    # Fill missing values in specific columns with "Unknown"
    table['title'] = table['title'].fillna('Unknown')
    table['firm'] = table['firm'].fillna('Unknown')
    table['start_date'] = table['start_date'].fillna('Unknown')
    table['end_date'] = table['end_date'].fillna('Unknown')
    table['location'] = table['location'].fillna('Unknown')

    # Drop rows with any missing values (if there are still any)
    table_no_miss = table.dropna()

    # Standardize column names (lowercase and replace spaces with underscores)
    table_no_miss.columns = table_no_miss.columns.str.lower().str.replace(' ', '_')

    # Drop duplicate rows
    table_no_miss_no_duplicates = table_no_miss.drop_duplicates()

    return table_no_miss_no_duplicates

def person_skills_data_cleaner(table):
    # Fill missing values in specific columns with "Unknown"
    table['skill'] = table['skill'].fillna('Unknown')

    # Drop rows with any missing values (if there are still any)
    table_no_miss = table.dropna()

    # Standardize column names (lowercase and replace spaces with underscores)
    table_no_miss.columns = table_no_miss.columns.str.lower().str.replace(' ', '_')

    # Drop duplicate rows
    table_no_miss_no_duplicates = table_no_miss.drop_duplicates()

    return table_no_miss_no_duplicates

def skills_data_cleaner(table):
    # Fill missing values in specific columns with "Unknown"
    table['skill'] = table['skill'].fillna('Unknown')

    # Drop rows with any missing values (if there are still any)
    table_no_miss = table.dropna()

    # Standardize column names (lowercase and replace spaces with underscores)
    table_no_miss.columns = table_no_miss.columns.str.lower().str.replace(' ', '_')

    # Drop duplicate rows
    table_no_miss_no_duplicates = table_no_miss.drop_duplicates()

    return table_no_miss_no_duplicates