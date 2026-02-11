"""
CHALLENGE - Block 2: Selection and Filtering
================================================

OBJECTIVE:
Perform complex queries combining EVERYTHING learned in Block 2.

CONTEXT:
You are an inventory analyst. The manager asks you for several specific reports
from the product catalog.

═══════════════════════════════════════════════════════════════════════

TASK 1: Premium Electronics Products
────────────────────────────────────────────
Find "premium" Electronics products:
- Price >= 500,000
- Rating >= 4.5
- Stock > 15

Show only: product_name, price, rating, stock
Sort by price (highest to lowest) - HINT: research .sort_values()

Save in variable: premium_electronics


TASK 2: Low Stock Products
────────────────────────────────────────
Products that need replenishment:
- Stock < 20
- Are active (is_active == 1)
- Price < 300,000 (priority to economic products)

Show only: product_name, stock, price, supplier
Save in variable: low_stock_products


TASK 3: Top Rated Products
────────────────────────────────────────
Find the best rated products:
- Rating >= 4.6
- Any category
- Only active products

Use .query() for this filter
Show only: product_name, category, rating, price
Save in variable: top_rated


TASK 4: Supplier Analysis
────────────────────────────────────────
For each supplier, count how many active products they have.

HINT: You will need:
1. Filter only active products
2. Use .groupby('supplier')
3. Count with .size() or .count()

Save in variable: supplier_count


TASK 5: Export Report
────────────────────────────────────────
Export premium_electronics to a CSV called 'premium_products_report.csv'
in the resources/ folder

Requirements:
- Do not include the index
- Use error handling (try/except)


TASK 6: Validation
────────────────────────────────────────
Show for each variable:
- Number of rows (use .shape[0])
- Column names
- First 3 rows

═══════════════════════════════════════════════════════════════════════

SUCCESS CRITERIA:
premium_electronics has at least 2 products
low_stock_products has at least 3 products
top_rated has at least 5 products
supplier_count shows count for both suppliers
CSV file is exported correctly
Code runs without errors

"""

# ═══════════════════════════════════════════════════════════════════════
#                                   CODE
# ═══════════════════════════════════════════════════════════════════════

import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/products.csv")

# ───────────────────────────────────────────────────────────────────────
# TASK 1: Premium Electronics Products
# ───────────────────────────────────────────────────────────────────────
category = "Electronics"
premium_electronics = df.query(
    'category == @category and price >= 500000 and rating >= 4.5 and stock > 15')[
    ['product_name', 'price', 'rating', 'stock']]
print(f"\nPremium Electronics Products\n{premium_electronics.sort_values(['price', 'rating', 'stock'], ascending=False)}") #Sorted from highest price to lowest

# ───────────────────────────────────────────────────────────────────────
# TASK 2: Low Stock Products
# ───────────────────────────────────────────────────────────────────────
low_stock_products = df.loc[(df['stock'] < 20) 
                            & (df['is_active'] == 1)
                            & (df['price'] < 300000),
                            ['product_name', 'stock', 'price', 'supplier']] 
# con el precio indicado para filtrar
print(f"\nLow Stock Products:\n{low_stock_products}")

# ───────────────────────────────────────────────────────────────────────
# TASK 3: Top Rated Products
# ───────────────────────────────────────────────────────────────────────
top_rated = df.query('rating >= 4.6 and is_active == 1')[['product_name', 'category', 'rating', 'price']]
print(f"\nTop Rated Products:\n{top_rated.sort_values(['rating'], ascending=False)}") # Usé para mejor visibilidad

# ───────────────────────────────────────────────────────────────────────
# TASK 4: Supplier Analysis
# ───────────────────────────────────────────────────────────────────────
supplier_count = df.loc[df['is_active'] == 1].groupby('supplier').size()
print(f"\nCantidad de productos por cada proveedor:\n{supplier_count}")

# ───────────────────────────────────────────────────────────────────────
# TASK 5: Export Report
# ───────────────────────────────────────────────────────────────────────
new_file = "premium_products_report.csv"
report_dir = current_dir.parent / "data/reports" / new_file

try:
    premium_electronics.to_csv(report_dir, index=False)
except PermissionError:
   print(f"\nPermission denied to export in: {report_dir}")
except Exception as e:
    print(f"\nUnexpected error: {e}")

# ───────────────────────────────────────────────────────────────────────
# TASK 6: Validation
# ───────────────────────────────────────────────────────────────────────

print("=" * 70)
print("VALIDATION OF RESULTS")
print("=" * 70)

# premium_electronics
print(f"\n- Number of rows for 'premium' products: {premium_electronics.shape[0]}")
print(f"- Column names:\n{premium_electronics.columns}")
print(f"- First 3 rows:\n{premium_electronics.head(3)}")

# low_stock_products
print(f"\n- Number of rows for 'low stock' products: {low_stock_products.shape[0]}")
print(f"- Column names:\n{low_stock_products.columns}")
print(f"- First 3 rows:\n{low_stock_products.head(3)}")

# top_rated
print(f"\n- Number of rows for 'top rated' products: {top_rated.shape[0]}")
print(f"- Column names:\n{top_rated.columns}")
print(f"- First 3 rows:\n{top_rated.head(3)}")

# supplier_count
print(f"\n- Number of rows for 'counted by each supplier' products: {supplier_count.shape[0]}")
print(f"- Column names:\n{supplier_count.columns}")
print(f"- First 3 rows:\n{supplier_count.head(3)}")


print("\n" + "=" * 70)
print("CHALLENGE COMPLETED")
print("=" * 70)
