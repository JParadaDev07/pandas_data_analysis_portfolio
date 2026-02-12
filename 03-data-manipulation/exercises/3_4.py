# EXERCISE 3.4: String operations (.str)
"""
OBJECTIVE: Master string operations using .str

Using the employees.csv DataFrame:

1. Create 'name_upper' converting 'name' to uppercase
2. Create 'name_lower' converting 'name' to lowercase
3. Create 'first_name' extracting the first word of the name
4. Create 'last_name' extracting everything after the first space
5. Create 'email_username' extracting the part before the @ in email
6. Create 'email_domain' extracting the part after the @ in email
7. Create 'name_length' with the length of the name
8. Create 'has_garcia' that is True if the last name contains 'García' or 'garcia'
9. Create 'email_updated' replacing '@company.com' with '@newcorp.com'
10. Create 'initials' with the initials (ej: "Ana García" → "A.G.")

HINT: Use .split() and then access the first character of each part
"""
# Code:

import pandas as pd
import numpy as np  
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/employees.csv")

print("DataFrame original:")
print(df[['name', 'email']].head())

# Arguments

"""
    This function is more complex than the previous ones,
    but actually, it's uses are very common and easiest than appears.

    I'm gonna explain each argument:
    - df: The DataFrame 
    - new_column_name: It's name says everything, it's the name of the new column to create
    - selected_column: This is the column that we're gonna use to create the new column
    - func: This is the function (build-in or lambda) that we're gonna apply to the selected column
    - arg: This argument is maden to use as argument of a split argument, for example, extract an specific value.
    - position: This one goes by the hand of arg, it's the position of the element that we're gonna use to create the new column
    - case_arg: This is the case of the argument that we're gonna use to create the new column
    - ret_args: This is the return arguments that we're gonna use to create the new column
    - arg_to_replace: This is the argument that we're gonna use to replace the selected column
    - new_arg: This is the new argument that we're gonna use to replace the selected column

    The function is divided by conditions, each condition is a different way to create a new column
    depending on the arguments that we pass to the function.

    By default, df, new_column_name, selected_column are required arguments, the others will be set to None by default
    so we can use the function in different ways.

"""

def main_transform_function(
    df, new_column_name, selected_column, 
    func=None, arg=None, position=None,
    case_arg=None, ret_args=[None, None],
    arg_to_replace=None, new_arg=None):
    # If func is provided, use it to create the new column
    if func and not arg:
        df[new_column_name] = df[selected_column].map(func)
        
    # If arg_to_replace and new_arg are provided, use them to create the new column
    elif arg_to_replace and new_arg: 
        df[new_column_name] = df[selected_column].apply( #We use the apply() function to apply a function to each element of the selected column
            lambda x: x.replace(arg_to_replace, new_arg)) # We use the replace() function to replace the argument with the new argument
    
    # If arg and position are provided, use them to create the new column
    elif arg is not None and position is not None:
        df[new_column_name] = df[selected_column].str.split(arg).str[position] # This way, is created to split elements
    
    # If arg and ret_args are provided, use them to create the new column
    elif arg is not None and ret_args is not None:
        df[new_column_name] = np.where(df[selected_column].str. # We use the where() function to create a new column based on a condition
            contains(arg, case=case_arg, regex=True), # Then we use the contains() function to check if the selected column contains the argument
            ret_args[0], # If the condition is true, we assign the first element of ret_args to the new column
            ret_args[1]) # If the condition is false, we assign the second element of ret_args to the new column
    else:
        print("ERROR: You must enter the required args")
    return df

# 1. Creating a new column with the name in uppercase
main_transform_function(
    df, # The DataFrame
    'name_upper', # The name of the new column
    'name', # The column to use
    str.upper # The function to apply
)

# 2. Creating a new column with the name in lowercase
main_transform_function(
    df, 
    'name_lower', 
    'name', 
    str.lower # The same that the previous one, but in lowercase
)

# 3. Creating a new column with the first name
main_transform_function(
    df, 
    'first_name', 
    'name', 
    arg=' ', # This kwarg, will be used to split the elements, in this case, the space between the first and last name
    position=0 # In this kwarg, we're using the 0 index, it means, that it's gonna take all the elements before the first space
)

# 4. Creating a new column with the last name
main_transform_function(
    df, 
    'last_name', 
    'name', 
    arg=' ', 
    position=1 # In this kwarg, we're using the 1 index, it means, that it's gonna take all the elements after the first space
)

# 5. Email username (before @)
main_transform_function(
    df, 
    'email_username', 
    'email', 
    arg='@', # This is the same logic than the previous ones, but with the @ symbol
    position=0 # In this kwarg, we're using the 0 index, it means, that it's gonna take all the elements before the @ symbol 
)

# 6. Email domain (after @)
main_transform_function(
    df, 
    'email_domain', 
    'email', 
    arg='@', 
    position=1 # Over here, we're using the 1 index, it means, that it's gonna take all the elements after the @ symbol (the email domain)
)

# 7. Name length
main_transform_function(
    df, 
    'name_length', 
    'name', 
    str.__len__ # This is a built-in function that returns the length of the string
)

# 8. Has "García" in the name
main_transform_function(
    df, 
    'has_garcia', 
    'name', 
    None, 
    'Garc(i|í)a', # This is a regular expression that matches "Garcia" or "García", a powerful tool to work with strings and accents
    case_arg=False, # This kwarg is used to specify the case of the argument, in this case, False means that it's gonna match both cases
    ret_args=["Positivo", "Negativo"] # This kwarg is used to specify the return arguments, in this case, if the condition is true, it will return "Positivo", otherwise it will return "Negativo"
)

# 9. Email updated
main_transform_function(
    df, 
    'email_updated', 
    'email', 
    arg_to_replace='company.com', # This kwarg is used to specify the argument that we're gonna replace
    new_arg='newcorp.com' # This kwarg is used to specify the new argument that we're gonna use to replace the old argument
)

# 10. Initials
# On this case, we are not using a personalized function, because with lambda, we can do it in a more concise way
df['initials'] = df['name'].apply(lambda x: ' '.join([word[0] for word in x.split()])) # This way, we're splitting the name by the space, and then we're taking the first letter of each word

# Show results
print("\nResults:")
print(df[['name', 'name_upper', 'name_lower', 'first_name', 'last_name', 'initials', 'has_garcia','email_username']].head())
