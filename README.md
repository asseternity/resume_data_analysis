# Resume Dataset Analysis

## Summary
Data analysis of 54,000 resumes exploring career transitions into tech. Designed to quantify how professionals move between industries — especially law to software.

## Tech
- **Language:** Python  
- **Libraries:** pandas, SQL (via pandasql), seaborn  
- **Data:** Structured resume dataset  
- **Output:** Visual and statistical analysis

## Highlights
- Analyzed education and career paths across roles  
- Identified law graduates who transitioned into IT fields  
- Compared degree types and seniority distributions  
- Produced visual breakdowns of tech vs. non-tech paths

## Pipeline
1. Import dataset and clean anomalies  
2. Run exploratory SQL queries with pandasql  
3. Merge role, degree, and experience dimensions  
4. Visualize using seaborn (distributions, correlations)

## Insights
- Legal professionals entering tech skew toward data and backend roles  
- Postgraduate degrees correlate with faster transition into mid-level positions  
- Junior developers often come from diverse prior industries

## Testing
- Sanity checks on joins and null handling  
- Unit tests for custom cleaning functions  

## Results
- Notebook output published on Kaggle: `https://www.kaggle.com/code/assetn/resume-dataset-analysis`

## Notebook: https://www.kaggle.com/code/assetn/resume-dataset-analysis
