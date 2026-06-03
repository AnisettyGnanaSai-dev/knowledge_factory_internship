import pandas as pd
import os

#loading the data
curr_dir = os.path.dirname(__file__)
csv_path = os.path.join(curr_dir, 'data.csv')
df = pd.read_csv(csv_path)

#inspecting the data
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())

#inspecting missing values
print(df.isnull().sum())

#filling missing values
df['city'] = df['city'].fillna('Unknown')
df['department'] = df['department'].fillna('Not Assigned')
df['salary'] = df['salary'].fillna(df['salary'].median())
df['age'] = df['age'].fillna(df['age'].median())

#joining date conversion and extracting year and month
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')
df['joining_year'] = df['joining_date'].dt.year
df['joining_month'] = df['joining_date'].dt.month
df['joining_day'] = df['joining_date'].dt.month_name()

print(df.head())

#exploration questions
print(df.shape[0])
print(df["department"].value_counts())
print(df['city'].value_counts())

#salary analysis
print(df['salary'].mean())
print(df['salary'].median())
print(df['salary'].min())
print(df['salary'].max())

#Tpo 5 highest salaries
print(df.nlargest(5, 'salary'))


#group by department and calculate average salary
dept_salary = df.groupby('department')['salary'].mean()
print(dept_salary)

print(df.groupby('department').size())
print(df.groupby('department')['age'].mean())

#employees joined by year
print(df.groupby('joining_year').size())
print(df.groupby('joining_month').size())

#salary pivot table
salary_report = pd.pivot_table(
    data=df,
    index='department',
    columns='city',
    values='salary',
    aggfunc=['mean', 'max'],
    fill_value=0,
    margins=True,
    margins_name='Total'
)
print(salary_report)

