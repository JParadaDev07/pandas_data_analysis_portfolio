# EXERCISE 3.2: .apply() and custom functions
"""
OBJECTIVE: Learn to use .apply() with custom functions.

Using the employees.csv DataFrame:

PART A - Defined functions:
1. Create a function `categorize_salary(salary)` that returns:
   - 'High' if salary >= 50000
   - 'Medium' if salary >= 40000
   - 'Low' if salary < 40000
   
   Apply it to create the 'salary_category' column

2. Create a function `years_to_senior(years)` that returns how many years are left 
   to reach 10 years of experience (if already 10+, return 0)
   
   Apply it to create the 'years_to_senior' column

PART B - Lambda functions:
3. Use lambda to create 'performance_percentage' formatted as "85%"
4. Use lambda to create 'name_initials' (first letters of the name, e.g., "Ana García" → "AG")

PART C - apply() with multiple columns (axis=1):
5. Create a function `calculate_bonus(row)` that calculates:
   - If performance_score >= 85: salary * 0.15
   - If performance_score >= 75: salary * 0.10
   - Else: salary * 0.05
   
   Apply it with axis=1 to create 'bonus'
"""
# Code:

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/employees.csv")
df_copy = df.copy()

print("=" * 70)
print("PART A: Defined functions")
print("=" * 70)

# 1. Function categorize_salary
"""
   This function is useful, to categorize the salary of each employee
   based on the salary amount, this will help us to identify the salary range of each employee
   and make decisions based on that.
"""
def categorize_salary(salary):
   if salary >= 50000:
      return 'High'
   elif salary >= 40000:
      return 'Medium'
   else:
      return 'Low'
   

df_copy['salary_category'] = df_copy['salary'].apply(categorize_salary)

# 2. Function years_to_senior
"""
   This function is useful, to calculate the number of years left to reach 10 years of experience
   based on the years_of_experience column, this will help us to identify the years left to reach 10 years of experience
   and make decisions based on that.
"""
def years_to_senior(years):
   if years >= 10:
      return 'Valid for Senior'
   else:
      return 10 - years
   
df_copy['years_to_senior'] = df_copy['years_of_experience'].apply(years_to_senior)

print("\n" + "=" * 70)
print("PART B: Lambda functions")
print("=" * 70)

# 3. Performance percentage
"""
   This lambda function or anonymous function, help us to format the performance score as a percentage
   based on the performance_score column, this will help us to identify the performance percentage of each employee
   and make decisions based on that.
"""
df_copy['performance_percentage'] = df_copy['performance_score'].apply(lambda x: f"{x:,.0f}%")

# 4. Name initials
"""
   This other lambda function, help us to get the initials of the name
   based on the name column, this will help us to identify the initials of each employee
   and make decisions based on that.

   First we start with the name column, then we split the name into a list of strings
   then we take the first letter of each string and convert it to uppercase
   then we join the initials with a hyphen

   Example: 
   name = "Ana García"
   name.split() = ["Ana", "García"]
   [n[0].upper() for n in name.split()] = ["A", "G"]
   "-".join(["A", "G"]) = "A-G"
"""
df_copy['name_initials'] = df_copy['name'].apply(lambda x: '-'.join([n[0].upper() for n in x.split()]))

print("\n" + "=" * 70)
print("PART C: apply() with axis=1")
print("=" * 70)

# 5. Calculate bonus
"""
   This function is useful, to calculate the bonus of each employee
   based on the performance_score column, this will help us to identify the bonus of each employee
   and make decisions based on that.

   Example: 
   row = {'performance_score': 85, 'salary': 50000}
   calculate_bonus(row) = 50000 * 0.15 = 7500
"""
def calculate_bonus(row):
   if row['performance_score'] >= 85:
      return row['salary'] * 0.15
   elif row['performance_score'] >= 75:
      return row['salary'] * 0.10
   else: 
      return row['salary'] * 0.05
   
df_copy['bonus'] = df_copy.apply(calculate_bonus, axis=1)
print(df_copy)

# IT'S VERY IMPORTANT TO USE THE APPLY METHOD TO BE ABLE TO USE A FUNCTION, WITHOUT IT, IT'S NOT POSSIBLE TO USE A FUNCTION
