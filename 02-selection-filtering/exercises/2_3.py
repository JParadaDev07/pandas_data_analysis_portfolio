# EXERCISE 2.3: Simple conditional filtering
"""
OBJECTIVE: Learn to filter rows based on conditions.

Using the products.csv DataFrame, filter and show:

1. Products with price greater than 500,000
2. Products of the 'Electronics' category
3. Products with stock less than 20 units
4. Products with rating greater than or equal to 4.5
5. Products that are NOT active (is_active == 0)

EXTRA: For each filter, show how many products met the condition
using len() or .shape[0]
"""
# Code:

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/products.csv")

# 1. Price > 500,000
price_filter = df.loc[df['price'] > 500000]
print(f"\nProducts with price greater than 500K:\n{price_filter}")

# 2. Category 'Electronics'
category_filter = df.loc[df['category'].isin(['Electronics'])]
print(f"\nProducts of the 'Electronics' category:\n{category_filter}")

# 3. Stock < 20
stock_filter = df.loc[df['stock'] < 20]
print(f"\nProducts with stock less than 20 units:\n{stock_filter}")

# 4. Rating >= 4.5
rating_filter = df.loc[df['rating'] >= 4.5]
print(f"\nProducts with rating greater than or equal to 4.5 stars:\n{rating_filter}")

# 5. Products NOT active
inactive_filter = df.loc[df['is_active'] == 0]
print(f"\nProducts that are not active:\n{inactive_filter}")

# EXTRA: Show the count of each filter
print(f"\nProducts that passed the price filter: {price_filter.shape[0]}")
print(f"\nProducts that passed the category filter: {category_filter.shape[0]}")
print(f"\nProducts that passed the stock filter: {stock_filter.shape[0]}")
print(f"\nProducts that passed the rating filter: {rating_filter.shape[0]}")
print(f"\nProducts that passed the inactive filter: {inactive_filter.shape[0]}")
