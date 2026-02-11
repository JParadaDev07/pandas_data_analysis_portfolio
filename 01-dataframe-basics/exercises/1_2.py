# EXERCISE 1.2: DataFrame Information
"""
Using the imported DataFrame, show:
- Data types of each column (use .info())
- Descriptive statistics (use .describe())

Question: How many columns are numeric?

"""
# Your code:
import pandas as pd
from pathlib import Path

prompt = Path(__file__).parent

df = pd.read_csv(prompt.parent / "data/datasets/employees.csv")
print(f"\nData types of each column in the DataFrame:\n{df.dtypes}")
print(f"\nDescriptive statistics of the DataFrame:\n{df.describe()}")
print(f"\nNumeric columns of the DataFrame: {df.select_dtypes(include='number').columns}") # <==== If I only need to print the columns, use 'columns'