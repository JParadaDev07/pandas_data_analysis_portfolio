"""

UNGUIDED CHALLENGE - Block 3: Data Manipulation
================================================

OBJECTIVE:
Apply ALL manipulation techniques learned in Block 3.

CONTEXT:
You are an HR Analyst. You must prepare a comprehensive employee report
with transformations, categorizations, and data analysis.

═══════════════════════════════════════════════════════════════════════

TASK 1: Basic Information
────────────────────────────────────────────
Create the following derived columns:

- 'full_name_upper': Full name in uppercase
- 'first_name': First name
- 'email_username': Email username (before @)
- 'hire_year': Hiring year (extract from hire_date)

TASK 2: Salary Calculations
────────────────────────────────────────────

- 'annual_salary': Monthly salary * 12

- 'salary_range': 
  * 'High' if >= 50000
  * 'Medium' if >= 40000
  * 'Low' if < 40000

- 'performance_bonus': 
  * salary * 0.15 if performance_score >= 85
  * salary * 0.10 if performance_score >= 75
  * salary * 0.05 otherwise

- 'total_compensation': annual_salary + (performance_bonus * 12)

TASK 3: Employee Categorization
────────────────────────────────────────────

- 'experience_category':
  * 'Senior' if years_of_experience >= 8
  * 'Mid-Level' if >= 5
  * 'Junior' if >= 2
  * 'Entry-Level' otherwise

- 'performance_rating':
  * 'Outstanding' if >= 90
  * 'Excellent' if >= 85
  * 'Good' if >= 75
  * 'Average' if >= 65
  * 'Needs Improvement' otherwise

- 'department_code': Use .map() with dictionary:
  * IT → 'TEC'
  * HR → 'RHH'
  * Sales → 'VTA'
  * Finance → 'FIN'

TASK 4: Special Cases Identification
────────────────────────────────────────────
Create boolean columns for:

- 'top_performer': performance_score >= 90 AND years_of_experience >= 5
- 'needs_review': performance_score < 75
- 'eligible_for_promotion': 
  * years_of_experience >= 5 AND performance_score >= 85

- 'high_value_employee':
  * (salary >= 50000) OR (performance_score >= 90)

TASK 5: Email Transformation
────────────────────────────────────────────
The company changed domains. Update:

- 'email_new': Replace '@company.com' with '@techcorp.io'
- 'email_length': Length of the new email

TASK 6: Department Analysis
────────────────────────────────────────────
Using .apply() with axis=1, create 'dept_analysis' returning a string:

"[Name] works in [Department] with [X] years of experience"

Example: "Ana García works in IT with 5 years of experience"

TASK 7: Cleanup and Reorganization
────────────────────────────────────────────

1. Rename original columns to Spanish:
   - name → nombre
   - department → departamento
   - salary → salario
   - performance_score → calificacion

2. Reorganize columns in this order:
   ['nombre', 'email_new', 'departamento', 'experience_category',
    'salario', 'salary_range', 'performance_rating', 'total_compensation']

3. Drop temporary columns not needed in final report

TASK 8: Export
────────────────────────────────────────────
Export processed DataFrame to 'employee_report.csv' in resources/
- No index
- Only reordered columns from TASK 7

TASK 9: Validation
────────────────────────────────────────────
Show:
- First 5 rows of final report
- Total top_performers
- Total employees eligible for promotion
- Average salary by salary_range

═══════════════════════════════════════════════════════════════════════

"""

# ═══════════════════════════════════════════════════════════════════════
#                                 CODE
# ═══════════════════════════════════════════════════════════════════════

import pandas as pd
import numpy as np
import operator
from pathlib import Path

current_dir = Path(__file__).parent

df = pd.read_csv(current_dir.parent / 'data/datasets/employees.csv') # Adjusted path for new structure

# 1. Transformation Block Function
"""
   This function is super useful to apply different transformations to a column
   without repeating the same code over and over again. It's like a "universal remote"
   for data changes.
   
   It handles 3 main cases:
   1. Function with arguments (like replacing text)
   2. Simple function without arguments (like converting to uppercase)
   3. Splitting text (like extracting the first part of an email)
"""
def trans_block(
  df, 
  new_column, 
  selected_column,
  func=None, 
  func_arg=None, 
  split_arg=None, 
  position_arg=None
):
  # Case 1: The function needs extra arguments (e.g. what to replace)
  if func and func_arg and not split_arg:
    if isinstance(func_arg, tuple):
      df[new_column] = df[selected_column].apply(lambda x: func(x, *func_arg))
    else:
      df[new_column] = df[selected_column].apply(lambda x: func(x, func_arg))

  # Case 2: The function is simple and needs no extra arguments
  elif func and not func_arg and not split_arg:
    df[new_column] = df[selected_column].apply(func)

  # Case 3: We need to split text and take a specific part
  elif not func and split_arg and position_arg is not None:
    df[new_column] = df[selected_column].apply(lambda x: x.split(split_arg)[position_arg])
  return df


# 2. Batch Transformation Block Function
"""
   Since I'm lazy (in a good way!), I don't want to call 'trans_block' five times
   if I have 5 columns to change.
   
   This function takes a dictionary (a recipe book) and applies 'trans_block'
   to all the ingredients (columns) at once. Loop smarter, not harder!
"""
def batch_trans_block(df, transformation_dict):
  # Unpacking the "recipe book" (dictionary) to get all lists
  for new_col, source, func, func_arg, split, pos in zip(
        transformation_dict['nc'],
        transformation_dict['sc'],
        transformation_dict['fctn'],
        transformation_dict['fctn_arg'],
        transformation_dict['splt'],
        transformation_dict['pstn'],
    ):
        # We cook each column using our single transformation tool
        trans_block(df, new_col, source, func, func_arg, split, pos)
  return df


# 3. Modification Block Function
"""
   Sometimes we need to clean up the house: renaming things, throwing trash away (dropping columns),
   or just rearranging furniture (reordering columns).
   
   This function handles all those 'structural' changes to the DataFrame.
"""
def mod_block(df, func=None, cols=None, cols_reordered=None):
  # Option 1: Rename columns (give them better names)
  if func == 'rename' and cols is not None:
    df = df.rename(columns=cols)

  # Option 2: Drop columns (get rid of what we don't need)
  elif func == 'drop' and cols is not None:
    df = df.drop(columns=cols)

  # Option 3: Reorder columns (put them in a nice order)
  elif cols_reordered is not None:
    df = df[cols_reordered]
  return df


# 4. Return Analysis Function
"""
   This one is for storytelling! 
   It takes data from different columns and formats it into a nice sentence.
   Great for generating reports or summaries for humans to read.
"""
def ret_analysis(df, new_column, fmt_string):
  # Takes a string template (like "Hello {name}") and fills it with row data
  df[new_column] = df.apply(lambda row: fmt_string.format(**row), axis=1)
  return df


# 5. Simple Financial Calculations
"""
   Money matters! This function handles the basic math for salaries and bonuses.
   
   It can do two things:
   1. Apply conditions (like `np.select`) to categorize things (e.g. High/Low salary).
   2. Simple math operations (like multiplying salary by 1.1).
   
   It uses `df.eval()` which allows us to write conditions as strings ("salary > 50000").
   This makes the configuration much cleaner!
"""
def finances_simple_block(
  df, new_col, 
  selected_col=None, 
  op=None, 
  conditions=None, 
  ret_args=None, 
  value=None, 
  default=None
):
  # Case 1: Conditional Logic (e.g. Salary Ranges)
  if not selected_col and conditions and ret_args:
    if isinstance(conditions, (list, tuple, dict)):
      ret_args_evaluated = ret_args
      default = np.array(default, dtype=('object'))
      
      # We evaluate string conditions like "salary > 5000" into actual boolean masks
      conditions = [df.eval(cond) for cond in conditions]

      # np.select is like a super-powered if/else for entire columns
      df[new_col] = np.select(conditions, ret_args_evaluated, default)
   
  # Case 2: Simple Arithmetic (e.g. Salary * 12)
  elif value and selected_col is not None:
    df[new_col] = op(df[selected_col], value)

  else:
    raise('ERROR: You must enter the required args based on the working function')
  
  return df


# 6. Complex Financial Calculations
"""
   Sometimes simple math isn't enough. We need to calculate things dynamically based on rows!
   
   Example: 
   - If performance is high -> Bonus = Salary * 0.15
   - If performance is low -> Bonus = Salary * 0.05
   
   This function evaluates math expressions saved as strings. It's like magic!
   "salary * 0.15" becomes an actual calculation locally.
"""
def finances_complex_block(
  df, new_col,
  conditions=None,
  ret_args=None,
  default=None
):
  ret_args_evaluated = []

  # We check if the result is a formula (string with math symbols) or a fixed value
  for expr in ret_args:
    if isinstance(expr, str) and any (op in expr for op in ['*', '+', '-', '/']):
      # Convert "salary * 0.15" into actual numbers
      ret_args_evaluated.append(df.eval(expr))
    else:
      ret_args_evaluated.append(expr)
  
  # Same check for the default value (fallback)
  if isinstance(default, str) and any (op in default for op in ['*', '+', '-', '/']):
    default_evaluated = df.eval(default)

  else:
    default_evaluated = default
    
  default_array = np.array(default_evaluated, dtype=('object'))
    
  # Evaluate the conditions (True/False)
  conditions = [df.eval(cond) for cond in conditions]

  # Apply the magic!
  df[new_col] = np.select(conditions, ret_args_evaluated, default_array)

  return df


# 7. Batch Financial Functions
"""
   Just like `batch_trans_block`, these functions are the "bulk chefs" for finances.
   They take a dictionary with all the rules and apply the financial calculations
   one by one.
"""
def batch_fin_sim_block(df, simple_finances_dict):
  for new_col, source, op, conditions, ret_args, value, default in zip(
        simple_finances_dict['nc'],
        simple_finances_dict['sc'],
        simple_finances_dict['op'],
        simple_finances_dict['cond'],
        simple_finances_dict['ret'],
        simple_finances_dict['val'],
        simple_finances_dict['def'],
    ):
        finances_simple_block(df, new_col, source, op, conditions, ret_args, value, default)
  return df


def batch_fin_com_block(df, complex_finances_dict):
  for new_col, conditions, ret_args, default in zip(
        complex_finances_dict['nc'],
        complex_finances_dict['cond'],
        complex_finances_dict['ret'],
        complex_finances_dict['def'],
    ):
        finances_complex_block(df, new_col, conditions, ret_args, default)
  return df
  

# ───────────────────────────────────────────────────────────────────────
# TASK 1: Basic Information
# ───────────────────────────────────────────────────────────────────────

# Setting up our "Transformation Recipe Book"
# We list:
# - 'nc': New Column Name
# - 'sc': Source Column (where data comes from)
# - 'fctn': function to apply (or None)
# - 'splt': character to split by (or None)
# - 'pstn': position to take after splitting (0 = first part)
transformation_dict = {
  'nc' : ['full_name_upper', 'first_name', 'email_username', 'hire_year',],
  'sc' : ['name', 'name', 'email', 'hire_date',],
  'fctn' : [str.upper, None, None, None,],
  'fctn_arg' : [None, None, None, None,],
  'splt' : [None, ' ', '@', '-',],
  'pstn' : [None, 0, 0, 0,]
}

# Sending the book to the chef!
df = batch_trans_block(df, transformation_dict)


# ───────────────────────────────────────────────────────────────────────
# TASK 2: Salary Calculations
# ───────────────────────────────────────────────────────────────────────

# Simple stuff first: Mulitplying and Categorizing
# We use 'operator.mul' for multiplication and a list of conditions for the ranges.
simple_finances_dict = {
  'nc' : ['annual_salary', 'salary_range'],
  'sc' : ['salary', None],
  'op' : [operator.mul, None],
  'cond' : [None, [
    'salary >= 50000',
    'salary >= 40000',
    'salary < 40000'
    ]],
  'ret' : [None, ['Alto', 'Medio', 'Bajo']], # Kept values in Spanish for the final report
  'val' : [12, None],
  'def' : [None, 'N/A']
}

df = batch_fin_sim_block(df, simple_finances_dict)

# Now the fun part: Complex Formulas!
# We write the math as strings ('salary * 0.15') and let pandas evaluate it.
complex_finances_dict = {
  'nc' : ['performance_bonus'],
  'cond' : [[
    'performance_score >= 85',
    'performance_score >= 75'
    ]],
  'ret': [[
    'salary * 0.15',
    'salary * 0.10'
    ]],
  'def': ['salary * 0.05'] # Everyone gets at least 5%
}

df = batch_fin_com_block(df, complex_finances_dict)

# Manual addition because sometimes doing it directly is faster than writing a function for it!
df['total_compensation'] = df['annual_salary'] + (df['performance_bonus'] * 12)

# Data Formatting (Make it look pretty)
# Using lambda to remove decimals from float numbers, but keeping them as objects/strings
df['performance_bonus'] = df['performance_bonus'].apply(
  lambda x: f"{x:.0f}" if isinstance(x, (int, float)) else x 
)

df['total_compensation'] = df['total_compensation'].apply(
  lambda x: f"{x:.0f}" if isinstance(x, (int, float)) else x
)

# ───────────────────────────────────────────────────────────────────────
# TASK 3: Employee Categorization
# ───────────────────────────────────────────────────────────────────────

# Defining the rules of the game (Conditions) used for np.select
# It's cleaner to have them here than inside the function call
hwrk_3_conditions = [
  # years_of_experience
  df['years_of_experience'] >= 8,
  df['years_of_experience'] >= 5,
  df['years_of_experience'] >= 2,
  df['years_of_experience'] < 2,

  # performance_score
  df['performance_score'] >= 90,
  df['performance_score'] >= 85, 
  df['performance_score'] >= 75,
  df['performance_score'] >= 65,
  df['performance_score'] < 65,
]

# Simple dictionary mapping for Dept Codes
# IT -> TEC, etc.
department_code_dict = {
  'IT': 'TEC',
  'HR': 'RHH',
  'Sales': 'VTA',
  'Finance': 'FIN'
}

# The labels we want to assign based on the conditions above
hmwrk_3_values = [
  'Senior', 
  'Mid-Level', 
  'Junior',
  'Entry-level',
  'Sobresaliente',
  'Excelente',
  'Bueno',
  'Regular',
  'Necesita Mejorar'
]

# Using .map() is the fastest way to replace values using a dictionary
df['deparment_code'] = df['department'].map(department_code_dict)

# Using np.select to apply the conditions and values defined above
# It checks conditions in order: if condition[0] is true, it assigns values[0], and so on.
df['experience_category'] = np.select(
  hwrk_3_conditions[0:3], 
  hmwrk_3_values[0:3], 
  default='N/A'
)

df['performance_rating'] = np.select(
  hwrk_3_conditions[4:], 
  hmwrk_3_values[4:], 
  default='N/A'
)

# ───────────────────────────────────────────────────────────────────────
# TASK 4: Special Cases Identification
# ───────────────────────────────────────────────────────────────────────

# Boolean Masks: true/False columns based on logic
# Who is a star? (High performance AND experienced)
df['top_performer'] = (
  (df['performance_score'] >= 90) &
  (df['years_of_experience'] >= 5)
)

# Who needs help? (Low performance)
# np.where is like IF(Excel)
df['needs_review'] = np.where(df['performance_score'] < 75, True, False)

# Who can move up? (Experienced enough AND Good performance)
df['eligible_for_promotion'] = (
  (df['years_of_experience'] >= 5) &
  (df['performance_score'] >= 85)
)

# Who is expensive or very good? (OR logic)
df['high_value_employee'] = (
  (df['salary'] >= 50000) | (df['performance_score'] >= 90)
)



# ───────────────────────────────────────────────────────────────────────
# TASK 5: Email Transformation
# ───────────────────────────────────────────────────────────────────────

# Updating our "Recipe Book" with new instructions
# We add new columns (nc), sources (sc), and functions (fctn)
# str.replace acts like Find & Replace
# str.__len__ just counts the characters
transformation_dict.update({
  'nc' : ['email_new', 'email_length'],
  'sc' : ['email', 'email_new'],
  'fctn' : [str.replace, str.__len__],
  'fctn_arg' : [('company.com', 'techcorp.io'), None],
  'splt' : [None, None],
  'pstn' : [None, None]
})

# Running the batch processor again with the new rules
df = batch_trans_block(df, transformation_dict)  


# ───────────────────────────────────────────────────────────────────────
# TASK 6: Department Analysis
# ───────────────────────────────────────────────────────────────────────

# Creating a narrative string. 
# We use Python's f-string style formatting {variable} inside a template.
ret_analysis(
  df,
  'dept_analysis',
  '''{name} trabaja en {department} 
  con {years_of_experience} 
  años de experiencia'''
)

# ───────────────────────────────────────────────────────────────────────
# TASK 7: Cleanup and Reorganization
# ───────────────────────────────────────────────────────────────────────

# Time to clean up!
# Renaming columns to Spanish as requested
df = mod_block(
  df,
  func='rename',
  cols={
    'name': 'nombre',
    'department': 'departamento',
    'salary': 'salario',
    'performance_score': 'calificacion'
  }
)

# Dropping temporary columns (we don't need 'email' anymore since we have 'email_new')
df = mod_block(
  df,
  func='drop',
  cols=['email', 'email_length']
)

# Reordering columns to make the report look professional
df_reordered = mod_block(
  df,
  cols_reordered=[
    'nombre', 
    'email_new',
    'departamento',
    'experience_category',
    'salario',
    'salary_range',
    'performance_rating',
    'total_compensation'
  ]
)

# ───────────────────────────────────────────────────────────────────────
# TASK 8: Export
# ───────────────────────────────────────────────────────────────────────

# Saving the work!
# We use a try/except block just in case the file is open (PermissionError)
# or if the path doesn't exist. Better safe than sorry!
report_name = 'employee_report.csv'
output = current_dir.parent / 'data/reports/employee_report.csv'

try:
  df_reordered.to_csv(output, index=False)
except PermissionError:
  print(f"Permission denied for export to: {output}")
except Exception as e:
  print(f"An unexpected error occurred, please try again: {e}")


# ───────────────────────────────────────────────────────────────────────
# TASK 9: Validation
# ───────────────────────────────────────────────────────────────────────

print("=" * 70)
print("RESULTS VALIDATION")
print("=" * 70)

# Quick sanity checks to make sure our logic worked
total_top_performers = df['top_performer'].sum()
print(f"\nTotal Top Performers: {total_top_performers}")

total_promotion = df['eligible_for_promotion'].sum()
print(f"Total Eligible for Promotion: {total_promotion}")

# Checking if salary ranges make sense (High should be higher than Low!)
avg_salary_by_range = df.groupby('salary_range')['salario'].mean()
print(f"\nAverage Salary by Range:\n{avg_salary_by_range}")

print("\nFirst 5 rows of final report:")
print(df_reordered.head(5))
