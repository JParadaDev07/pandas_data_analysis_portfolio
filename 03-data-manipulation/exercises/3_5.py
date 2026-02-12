# EXERCISE 3.5: Conditionals with np.where()
"""
OBJECTIVE: Use np.where() to create columns with conditional logic.

Using the employees.csv DataFrame:

1. Create 'salary_status':
   - 'Alto' if salary >= 50000
   - 'Bajo' if not

2. Create 'experience_level':
   - 'Senior' if years_of_experience >= 8
   - 'Mid' if years_of_experience >= 5
   - 'Junior' if not

3. Create 'performance_bonus_pct':
   - 0.15 if performance_score >= 90
   - 0.10 if performance_score >= 80
   - 0.05 if performance_score >= 70
   - 0.00 if not

4. Create 'needs_raise' (boolean):
   - True if (salary < 45000 AND years_of_experience > 5)
   - False if not

5. Create 'employee_tier' combining salary and performance:
   - 'A' if salary >= 50000 AND performance_score >= 85
   - 'B' if salary >= 45000 AND performance_score >= 75
   - 'C' in other cases

HINT: Use nested np.where() for multiple conditions   
"""
# Code:

import pandas as pd
import numpy as np
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/employees.csv")

"""
   The 'main_func' is a very similar function than the previous exercise (3_4.py)
   but this time, we're gonna use the np.where() function to create columns with conditional logic.

   This function, has less arguments than the previous one, but i consider that this is more powerful,
   because here, we're gonna use the np.where() function to create columns with conditional logic, and the most
   special thing, is very similar to the SQL sintaxis and we can use string statements to declare the queries

   Arguments:
   - df: The DataFrame
   - new_col: The name of the new column
   - conditions: The conditions to apply
   - ret_args: The arguments to return
   - default: The default value

   The most curious thing about this function, is that, using the without the ret_args and default args, 
   unfortunally, it's not gonna work, because the np.where() function needs to return a value, 
   so we need to provide the ret_args and default args, so yes, they're required arguments.

   The conditions argument, can be a string or a list of strings, if it's a string, it's gonna use the np.where() function, 
   if it's a list of strings, it's gonna use the np.select() function

"""

def main_func(
   df, 
   new_col, 
   conditions=None, 
   ret_args=None,
   default=None
): 
   if conditions and ret_args: # Main condition
      # it's necessary to check if the conditions are a list or a tuple or a dict
      # without this, it's gonna throw an error, specifically a TypeError
      # this is because the np.select() function expects a list of conditions
      # and the np.where() function expects a single condition
      if isinstance(conditions, (list, tuple, dict)): # Nested condition
         ret_args = np.array(ret_args, dtype=('object')) # We convert the ret_args to a numpy array and set the dtype to object
         default = np.array(default, dtype=('object')) # We convert the default to a numpy array and set the dtype to object
         
         conditions = [df.eval(cond) for cond in conditions] # We evaluate the conditions
         df[new_col] = np.select(conditions, ret_args, default) # We use the np.select() function to create the new column
      else:
         condition = df.eval(conditions) # We evaluate the condition
         df[new_col] = np.where(condition, ret_args[0], ret_args[1]) # We use the np.where() function to create the new column
   else:
      print("ERROR: You must enter the required args")
   return df



# 1. Salary status (Alto/Bajo)

main_func(
   df, # DataFrame
   'salary_status', # New column name
   conditions="salary >= 50000", # Like i said, this is a conditions very SQL like, and it's very easy to understand
   ret_args=['Alto', 'Bajo'], # This is a list of values to return, 'Alto' if the condition is true, 'Bajo' if the condition is false
) 

# 2. Experience level (Senior/Mid/Junior)
main_func(
   df,
   'experience_level',
   conditions=[ # This is a list of conditions, is used when we need to evaluate multiple conditions with multiple return values
      'years_of_experience >= 8',
      'years_of_experience < 5' 
   ],
   ret_args=['Senior', 'Junior'], # In this case, both values are True, because are the result of the evaluation of above conditions
   default='Junior' # This is the False result, or the default value if none of the conditions are met
)

# 3. Performance bonus percentage
main_func(
   df,
   'performance_bonus_pct',
   conditions=[
      'performance_score >= 90',
      'performance_score >= 80',
      'performance_score >= 70',
   ],
   ret_args=[0.15, 0.10, 0.05], # We can return any type of data, including floats, integers, strings, booleans, etc
   default='N/A' # We can return too an string value, even if the ret_args are a distinct type of data
)

# I added this additional, just for better readability
# This is only for formatting the output, not for the logic of the exercise
df['performance_bonus_amount'] = df['salary'] * df['performance_bonus_pct']
df['performance_bonus_amount'] = df['performance_bonus_amount'].apply(
   lambda x: f"${x:,.0f}" if isinstance(x, (int, float)) else x)
df['performance_bonus_pct'] = df['performance_bonus_pct'].apply(
   lambda x: f"{x*100:.0f}%" if isinstance(x, (int, float)) else x)

# 4. Needs raise (boolean)
main_func(
   df,
   'needs_raise',
   conditions="salary < 45000 and years_of_experience > 5", # Like i said, this is literally a SQL query, this is the power of the np.where() function
   ret_args=[True, False],
   default='N/A'
)

# 5. Employee tier (A/B/C)
main_func(
   df,
   'employee_tier',
   conditions=[
      'salary >= 50000 and performance_score >= 85', 
      'salary >= 45000 and performance_score >= 75',
      'salary < 45000 and performance_score < 75'
   ],
   ret_args=['A', 'B', 'C'],
   default='Other'
)


# Show results
print(df[['name', 'salary', 'years_of_experience', 'performance_score', 
          'salary_status', 'experience_level', 'employee_tier']].head(10))
