# EXERCISE 2.5: .query() and advanced methods
"""     
OBJECTIVE: Use .query() and advanced filtering methods.

PART A - Using .query():
1. Products with price > 300,000 (use .query())
2. Electronics with stock > 40 (use .query())
3. Products with rating >= 4.5 and price < 500,000 (use .query())

PART B - Advanced methods:
4. Products of the 'Electronics' or 'Furniture' categories (use .isin())
5. Products with price between 100,000 and 500,000 (use .between())
6. Products whose name contains 'LED' or 'HD' (use .str.contains(), case=False)
7. Products with supplier 'TechSupply' (use .isin() with list of one element)

PART C - Combining filters with column selection:
8. Electronics products, show only 'product_name' and 'price' (use .loc[])
9. Products with rating > 4.5, show 'product_name', 'price', 'rating'
10. Active products with .query(), show only 'product_name' and 'stock'
"""
# Tu código:

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/products.csv")

print("=" * 70)
print("PART A: .query()")
print("=" * 70)

# 1. Price > 300,000 with .query()
print(f"\nProducts with price greater than 300K:\n{df.query('category == "Electronics" and price > 300000')}")

# 2. Electronics with stock > 40
print(f"\nProducts with stock greater than 40 units:\n{df.query('cateogry == "Electronics" and stock > 40')}")

# 3. Rating >= 4.5 and price < 500,000
print(f"\nProducts with rating greater than or equal to 4.5 stars:\n{df.query('rating >= 4.5')}")

print("\n" + "=" * 70)
print("PART B: Advanced methods")
print("=" * 70)

# 4. Categories Electronics or Furniture (.isin())
print(f"\nProducts that are in the 'Electronics' or 'Furniture' category:\n{df.loc[df['category'].isin(['Electronics', 'Furniture'])]}")

# 5. Price between 100,000 and 500,000 (.between())
print(f"\nProducts that have a price between 100k and 500k:\n{df.loc[df['price'].between(100000, 500000)]}")

# 6. Name contains 'LED' or 'HD' (.str.contains())
print(f"\nProducts that contain 'LED' or 'HD' in their name:\n{df.loc[df['product_name'].str.contains('LED|HD', case=False)]}")

# 7. Proveedor TechSupply (.isin())
print(f"\nProducts with supplier 'TechSupply':\n{df.loc[df['supplier'].isin(['TechSupply'])]}")

print("\n" + "=" * 70)
print("PART C: Filters + Column selection")   
print("=" * 70)

# 8. Electronics, only name and price
print(f"\nProducts of the 'Electronics' category with only their name and price:\n{df.loc[df['category'].str.contains('Electronics'), ['product_name', 'price']]}")

# 9. Rating > 4.5, only name, price, rating
print(f"\nProducts with rating greater than 4.5 stars with only their name, price and rating:\n{df.loc[df['rating'] > 4.5, ['product_name', 'price', 'rating']]}")

# 10. Active products with .query(), show only name and stock
print(f"\nActive products with only their name and stock:\n{df.query('is_active == 1')[['product_name', 'stock']]}")

