# ============================================
# BLOCK 2: SELECTION AND FILTERING
# Concepts: Selection of columns, basic indexing
# ============================================
# EXERCISE 2.1: Basic column selection
"""
Import the 'products.csv' file and perform the following selections:

1. Show ONLY the 'product_name' column
2. Show the 'product_name' and 'price' columns
3. Show the 'product_name', 'category', 'price' and 'stock' columns

CONCEPTUAL QUESTION:
What is the difference between df['product_name'] and df[['product_name']]?
Run both and observe with type() what type of object they return.
"""
# Code:

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/products.csv")

# 1. One column (returns Series)
print(f"\nSelection of one column:\n{df['product_name']}")

# 2. Two columns (returns DataFrame)
print(f"\nSelection of several columns:\n{df[['product_name', 'price']]}")


# 3. Four columns
print(f"\nSelection of four columns:\n{df[['product_name', 'category', 'price', 'stock']]}")


# CONCEPTUAL ANSWER
print(f"Type of df['product_name']: {type(df['product_name'])}") #This is usually used to choose only one column, that is, it returns a Series
print(f"Type of df[['product_name']]: {type(df[['product_name']])}") #When 'df[[]]' is used, it is because more than two columns will be returned, that is, it will return a DataFrame
