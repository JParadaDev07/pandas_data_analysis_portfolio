import pandas as pd
from pathlib import Path

prompt = Path(__file__).parent

# EXERCISE 1.4: Index handling

"""
Import the CSV using the 'id' column as index (parameter: index_col)
Show the first 3 rows.

What difference do I notice compared to the normal import?
"""
# Code:

# The diference between import an .csv file without the 'index_col' parameter, is the way by the data is displayed
# Using the traditional way, all the data will be displayed by their index, and on the data analysis the first value is '0'. 
# This may confusing, specially if a person is not used to view data like that.
# Using the index_col, will perform the way to see the data, for example, by creating a dataframe and assigning it a different more readable index, 
# as in the example below: 

df = pd.read_csv(prompt.parent / "data/datasets/employees.csv", index_col='id', nrows=3) # This will print the data using the 'id' as index
print(df)