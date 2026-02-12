# ============================================
# BLOCK 3: DATA MANIPULATION
# Concepts: Create and modify columns
# ============================================
# EXERCISE 3.1: Create and modify basic columns
"""
Import the 'employees.csv' file and perform the following operations:

1. Create a new column 'annual_salary' multiplying 'salary' by 12
2. Create a column 'performance_level' with the value 'High' for all
3. Create a column 'salary_k' dividing 'salary' by 1000 (salary in thousands)
4. Create a column 'is_it_dept' that is True if department is 'IT', False if not

CONCEPTUAL QUESTION:
What is the difference between:
  df['nueva_col'] = value
  df.loc[:, 'nueva_col'] = value
?
"""
# Code:

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/employees.csv")

print("DataFrame original:")
print(df.head())

df_copy = df.copy()

# 1. Annual salary
df_copy['annual_salary'] = df['salary'] * 12
 
# 2. Performance level constant
df_copy['performance_level'] = 'High'
print(df_copy)

# 3. Salary in thousands
df_copy['salary_k'] = df['salary'] // 1000

# 4. Is IT department
df_copy['is_it_dept'] = df['department'] == 'IT'

# Show the first 5 rows with the new columns
print("\nDataFrame with new columns:")
print(df_copy[['name', 'salary', 'annual_salary', 'salary_k', 'is_it_dept']].head())
