# 📁 Block 2: Selection & Filtering
## 🎯 Overview
This block focuses on the core capability of any Data Analyst: extracting specific insights from large datasets. I've move beyond simple loading to precise data selection using label-based (`.loc`) and position-based (`.iloc`) indexing, boolean masking, and advanced query strings. The block concludes with a sophisticated product inventory analysis system.
## 🧠 Learning Objectives
- **Precise Selection:** Master the difference between selecting Series (`df['col']`) vs DataFrames (`df[['col']]`).
- **Indexing Methods:** Understand when to use `.loc[]` (labels) vs `.iloc[]` (integer positions).
- **Boolean Logic:** Filter data using complex conditions with `&` (AND), `|` (OR), and `~` (NOT).
- **Advanced Filtering:** Use efficient methods like `.query()`, `.isin()`, and `.between()`.
- **String Matching:** Filter text data with `.str.contains()`.
---
## 📝 Exercises Breakdown
### [2.1 Basic Selection](./exercises/2_1.py)
**Goal:** specific Differentiate between Series and DataFrame selection.
- **Concept:** `df['col']` returns a Series, while `df[['col']]` returns a DataFrame.
- **Task:** Select single and multiple columns ('product_name', 'category', 'price', 'stock').
### [2.2 Indexing (.loc vs .iloc)](./exercises/2_2.py)
**Goal:** Master label-based vs position-based extraction.
- **Key Insight:** `.loc[0:5]` includes the end index (6 rows), while `.iloc[0:5]` excludes it (5 rows).
- **Tasks:** Slicing rows and selecting specific columns by name (`.loc`) and position (`.iloc`).
### [2.3 Simple Filtering](./exercises/2_3.py)
**Goal:** Apply single conditions to filter data.
- **Conditions:** Price > 500k, Category == 'Electronics', Stock < 20, Active status.
- **Method:** Boolean indexing with comparison operators (`>`, `<`, `==`).
### [2.4 Multiple Conditions](./exercises/2_4.py)
**Goal:** Combine multiple logic gates.
- **Logic:**
  - [(Category == 'Electronics') & (Price > 200k)](./exercises/2_4.py)
  - [(Category == 'Furniture') | (Price < 100k)](./exercises/2_4.py)
  - `~ (Category == 'Electronics')` (NOT)
- **Functions:** `.between(20, 50)` for stock ranges.
### [2.5 Advanced Methods (.query)](./exercises/2_5.py)
**Goal:** Write cleaner, more readable filtering code.
- **Method:** `df.query('category == "Electronics" and price > 300000')`.
- **String Ops:** `.str.contains('LED|HD', case=False)` to find specific products by name.
- **List Ops:** `.isin(['TechSupply'])` for filtering by list of values.
---
## 🏆 Challenge: Inventory Reporting
**File:** [`2_6_challenge.py`](./exercises/2_6_challenge.py)
**Scenario:** As an inventory analyst, you need to generate specific lists for management.
**Tasks Accomplished:**
1. **Premium Electronics:** Filtered for Price >= 500k, Rating >= 4.5, Stock > 15. Sorted by price/rating.
2. **Low Stock Alert:** Identified active products with < 20 units and low price (< 300k).
3. **Top Rated:** Found products with Rating >= 4.6 using `.query()`.
4. **Supplier Analysis:** Counted active products per supplier.
5. **Export:** Generated `premium_products_report.csv` without index.
**Validation:** Used `.shape` to verify row counts for every logical set.
---
## 🚀 Mini-Project: Product Analytics System
**File:** [mini_project_block2.py](./exercises/mini_project_block2.py)
**Scenario:** Building a reusable reporting system for "TechSupply" and "OfficeMax" products.
**Advanced Implementation:**
- **Modular Functions:**
  - [get_category(df, cat)](./exercises/mini_project_block2.py): Reusable logic to filter and sort any category.
  - [provider_analysis(df, prov)](./exercises/mini_project_block2.py): Calculates metrics (Count, Avg Price, Total Stock) for any provider.
  - [reports(df, name)](./exercises/mini_project_block2.py): Handles CSV export with error management and directory creation.
- **Complex Reports Generated:**
  1. **High Value:** Products >= $800k and 4.5+ rating (Sorted).
  2. **Critical Stock:** Active non-furniture items with < 25 units.
  3. **Mid-Range Electronics:** Electronics between $100k-$500k using `.between()`.
  4. **Specific Search:** Products containing 'Gaming', 'Ergonómica', 'HD', or 'WiFi'.
- **Comparative Analysis:** Automated print-out comparing metrics between 'TechSupply' and 'OfficeMax'.
**Key Takeaway:** Demonstrafed how to turn repetitive filtering tasks into reusable functions for scalable data analysis.
---
## 📂 Datasets Used
- [products.csv](../data/datasets/products.csv): Inventory data including price, stock, supplier, rating, and active status.
---