# EXERCISE 2.4: Filtering with multiple conditions
"""
OBJECTIVE: Combine multiple conditions with logical operators.

Remember:
- AND: &  (both conditions must be met)
- OR:  |  (at least one must be met)
- NOT: ~  (negate a condition)

IMPORTANT: Use parentheses for each condition

CORRECTO:   df[(df['price'] > 100000) & (df['stock'] < 50)]
INCORRECTO: df[df['price'] > 100000 & df['stock'] < 50]  # Error

Filter and show:

1. Electronics products with price > 200,000
2. Furniture products OR price < 100,000
3. Products with stock between 20 and 50 (use >= and <=)
4. Active products with rating > 4.5
5. Electronics products with stock < 30 AND rating >= 4.5
6. Products NOT from Electronics with price > 500,000

CHALLENGE: Products (Electronics OR Furniture) with rating > 4.3 AND stock < 50
"""
# Code:

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/products.csv")

# 1. Electronics AND price > 200,000
print(f"""\nProducts of the 'Electronics' category and with a price greater than 200K:
      {df.loc[(df['category'] == 'Electronics') & 
      (df['price'] > 200000)]}""")

# 2. Furniture OR price < 100,000
print(f"""\nProducts of the 'Furniture' category or with a price less than 100K:
      {df.loc[(df['category'] == 'Furniture') | 
      (df['price'] < 100000)]}""")

# 3. Stock between 20 and 50
print(f"""\nProducts that have a stock between 20 and 50 units:
      {df.loc[df['stock'].between(20, 50)]}""") 

# 4. Active AND rating > 4.5
print(f"""\nProducts that are active and have a rating greater than 4.5 stars:
      {df.loc[(df['is_active'] == 1) & 
      (df['rating'] > 4.5)]}""")

# 5. Electronics AND stock < 30 AND rating >= 4.5
print(f"""\nProducts of the 'Electronics' category, with a stock less than 30 units and rating greater than or equal to 4.5 stars:
      {df.loc[(df['category'] == 'Electronics') & 
      (df['stock'] < 30) & 
      (df['rating'] >= 4.5)]}""")

# 6. NOT Electronics AND price > 500,000
print(f"""\nProducts that are not from the 'Electronics' category and have a price greater than 500K:
      {df.loc[~((df['category']) == 'Electronics') & 
      (df['price'] > 500000)]}""")

# CHALLENGE: (Electronics OR Furniture) AND rating > 4.3 AND stock < 50
print(f"""\nProducts of the 'Electronics' or 'Furniture' category with a rating greater than 4.3 stars and a stock less than 50 units: 
      {df.loc[((df['category'] == 'Electronics') | 
      (df['category'] == 'Furniture')) & 
      (df['rating'] > 4.3) & 
      (df['stock'] < 50)]}""")

