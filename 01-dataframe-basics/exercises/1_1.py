# ============================================
# BLOCK 1: IMPORTATION
# Concepts: read_csv, read_json, parameters of reading
# ============================================
# EXERCISE 1.1: Basic Importation
"""
Import the file 'employees.csv' and show:
- The first 5 rows
- The shape of the DataFrame (rows, columns)
- The names of the columns
"""
# Code:

import pandas as pd
from pathlib import Path

prompt = Path(__file__).parent # Gets the absolute path of the current file

df_employees = pd.read_csv(prompt.parent / "data/datasets/employees.csv") 

print(f"\nFirst 5 rows:\n{df_employees.head()}")
print(f"\nShape of the DataFrame:\n{df_employees.shape}")
print(f"\nColumn names:\n{df_employees.columns}")