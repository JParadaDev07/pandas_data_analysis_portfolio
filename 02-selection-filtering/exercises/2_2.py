# EXERCISE 2.2: .loc[] and .iloc[]
"""
Using the imported DataFrame, perform the following selections:

PART A - Using .loc[] (by labels):
1. Select the row with index 0
2. Select rows from index 0 to 5 (including 5)
3. Select row 3, only columns 'product_name' and 'price'
4. Select rows 0 to 4, only columns 'product_name', 'category' and 'price'

PART B - Using .iloc[] (by position):
5. Select the first row (position 0)
6. Select the first 5 rows (positions 0-4, NOT including 5)
7. Select row 3, columns in positions 1 and 3
8. Select the first 10 rows, first 4 columns

CRITICAL QUESTION:
What is the difference between df.loc[0:5] and df.iloc[0:5]?
Run both and count how many rows they return.
"""
# Code:

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/products.csv")

print("=" * 70)
print("PART A: .loc[]")
print("=" * 70)

# 1. Row with index 0
print(f"\nSelection of row 0:\n{df.loc[0]}")

# 2. Rows from index 0 to 5 (INCLUDES 5)
print(f"\nSelection of rows from index 0-5:\n{df.loc[0:5]}")

# 3. Row 3, specific columns
print(f"\nSelection of specific columns:\n{df.loc[3, ['product_name', 'price']]} {type(df)} ")

# 4. Rows 0-4, specific columns
print(f"\nSelection of specific columns:\n{df.loc[0:4, ['product_name', 'category', 'price']]}")



print("\n" + "=" * 70)
print("PART B: .iloc[]")
print("=" * 70)

# 5. First row
print(f"\nSelection of first row:\n{df.iloc[0]}")

# 6. First 5 rows (NOT including 5)
print(f"\nSelection of the first 5 rows:\n{df.iloc[0:5]}")

# 7. Row 3, columns in positions 1 and 3
print(f"\nSelection of row 3, columns 1 and 3:\n{df.iloc[2, [0, 3]]}")

# 8. First 10 rows, first 4 columns
print(f"\nSelection of the first 10 rows and 4 columns:\n{df.iloc[0:10, 0:4]}")


# CRITICAL ANSWER:
print(f"\nRows with .loc[0:5]: {len(df.loc[0:5])}") #Using .loc[], it counts the number 5, that is, it would show the first 6 rows
print(f"Rows with .iloc[0:5]: {len(df.iloc[0:5])}") #Using .iloc[], it does not count the number 5, that is, it would show the first 5 rows
