import pandas as pd
from pathlib import Path

prompt = Path(__file__).parent

# EXERCISE 1.3: Importation with parameters
"""
Importing the CSV but:
- Only the first 10 rows (parameter: nrows)
- Only the columns: name, department, salary (parameter: usecols)

"""
# Code:

# The 'nrows' parameter is used to read a specific quantity of rows of a dataset
# The 'usecols' parameter is used to specify wich columns from a CSV file should be loaded into the DataFrame

df_employees = pd.read_csv(prompt.parent / "data/datasets/employees.csv", nrows=10, usecols=['name', 'department', 'salary'])
print(df_employees)