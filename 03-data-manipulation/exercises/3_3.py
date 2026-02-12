# EXERCISE 3.3: .map() and dictionaries
"""
OBJECTIVE: Use .map() to transform values with dictionaries.

Using the employees.csv DataFrame:

1. Create a dictionary `dept_codes` that maps:
   'IT' → 'TEC'
   'HR' → 'RHH'
   'Sales' → 'VTA'
   'Finance' → 'FIN'
   
   Use .map() to create the 'dept_code' column

2. Create a dictionary `city_zones` that maps:
   'Bogotá' → 'Centro'
   'Medellín' → 'Norte'
   'Cali' → 'Sur'
   'Cartagena' → 'Caribe'
   'Barranquilla' → 'Caribe'
   
   Use .map() con .fillna('Otros') to create 'zone'

3. Create a dictionary `performance_grades` that maps performance ranges:
   90-100 → 'A'
   80-89 → 'B'
   70-79 → 'C'
   <70 → 'D'
   
   HINT: First use .apply() or np.where() to create ranges,
   then .map() to assign letters

CHALLENGE:
4. Use .map() with a FUNCTION (not dictionary) to create 'email_provider'
   extracting the domain after the @ of the email
"""
# Code:

import pandas as pd
import numpy as np
from pathlib import Path


current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/employees.csv")

# 1. Department mapping to codes
"""
   This dictionary, is useful to map the department as a code,
   this is a very common operation in data analysis, to map values to codes
   making it easier to work with the data
"""
dept_codes = {
   'IT': 'TEC',
   'HR': 'RHH',
   'Sales': 'VTA',
   'Finance': 'FIN'
}

df['dept_code'] = df['department'].map(dept_codes)


# 2. Mapping cities to zones
"""
   This dictionary is useful to map a city into a region based on the city location,
   depending on the location of the city, it will be assigned to a region, at the end
   we use the fillna() method to fill the missing values with 'Otros', so this is a way to
   automatize the process of assigning a region to a city
"""
city_zones = {
   'Bogotá': 'Centro',
   'Medellín': 'Norte',
   'Cali': 'Sur',
   'Cartagena': 'Caribe',
   'Barranquilla': 'Caribe'
}

df['zone'] = df['city'].map(city_zones).fillna('Otros') #Over here, we use the fillna() method to fill the missing values with 'Otros', since the mapping covers all the areas

# 3. Mapeo de performance a grados
"""
   This dict, like the others, has the function to map the performance score to a grade,
   depending on the performance score, it will be assigned a grade.
"""
performance_grades = {
   '90-100': 'A',
   '80-89': 'B',
   '70-79': 'C',
   '<70': 'D'
}

"""
   A way to do it, is first at all, creating an string column that will store the performance range
   based on the performance score, this will help us to identify the performance range of each employee
   and make decisions based on that.

   Example: 
   performance_score = 90
   performance_range = '90-100'

   performance_score = 85
   performance_range = '80-89'

   performance_score = 75
   performance_range = '70-79'

   performance_score = 65
   performance_range = '<70'
"""

df['performance_range'] = np.where(df['performance_score'] >= 90, '90-100',
                           np.where(df['performance_score'] >= 80, '80-89',
                           np.where(df['performance_score'] >= 70, '70-79', '<70')))


# Then we use the map() method to assign the grade based on the performance range

df['performance_grade'] = df['performance_range'].map(performance_grades)
print(f"\n{df[['performance_score', 'performance_range', 'performance_grade']].head()}")


# CHALLENGE 4: Extract email provider
"""
   This may be confusing, because, we are using .map to apply a lambda function,
   but actually, is very common use .map to apply a function to a column
   and .apply() to apply a function to a row.


   The way that we're extracting the email provider is by splitting the email column by the .split method,
   we pass the @ symbol as parameter, and then we use the [1] index to specify that we want the first element 
   after the @ symbol, which is the email provider, giving us the final result.
"""
df['email_provider'] = df['email'].map(lambda x: x.split('@')[1])
print(f"\n{df[['email', 'email_provider']]}")
