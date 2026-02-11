import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "data/datasets/products.csv")

"""
    This function helps with the selection an filtering of products by category
    that's why there's two args: df and cat

    df: being the dataframe with the products
    cat: being the category of the products

    The function returns the top 5 products of a given category
    It also sorts the products by rating in descending order
"""
def get_category(df, cat):
    result = (
        df.query('category == @cat')
        .loc[df['is_active'] == 1, ['product_name', 'category', 'rating', 'price']]
        .sort_values('rating', ascending=False)
    )    
    return result

"""
    This function helps with the selection an filtering of products by provider
    that's why there's two args: df and prov

    df: being the dataframe with the products
    prov: being the provider of the products

    The function returns the quantity of products, the average data of the products and the total stock of the products
    It also sorts the products by rating in descending order
"""
def provider_analysis(df, prov):
    main_filter = 'supplier == @prov and is_active == 1'
    product_quantity, average_data, total_stock = (
        len(df.query(main_filter)),
        df.query(main_filter)[['price', 'rating']].mean(),
        df.query(main_filter)['stock'].sum())

    return product_quantity, average_data, total_stock
    
"""
    This function helps with the creation of reports
    that's why there's two args: df and report_name

    df: being the dataframe with the products
    report_name: being the name of the report

    The function allows me to export the dataframes to a csv file
    to do this, first it needs to check if the directory exists
    if not, it needs to create it
    then, it needs to export the dataframe to a csv file
    finally, it needs to print the path where the report was created

    It also needs to handle the errors that may occur during the process
    like permission errors or unexpected errors
"""
def reports(df, report_name):
    report_dir = current_dir / "/data/reports" 

    if not report_dir.exists():
        report_dir.mkdir(parents=True, exist_ok=True)
        print(f"Report directory created: {report_dir}")
    
    report_path = report_dir / report_name
    
    try:
        df.to_csv(report_path, index=False)
        print(f"Reports have been created successfully in the path: {report_dir}")
    except PermissionError:
        print(f"\nPermission denied to export in: {report_dir}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
    return current_dir

"""
    There's two dicts that help with the code to make it more readable

    category_dict: being the dictionary that helps with the categories
    provider_dict: being the dictionary that helps with the providers

    Those dicts are used to make the code more readable and maintainable
    in addition, they help to the scalability of the code
"""

category_dict = {
    'electronic_category' : 'Electronics', 
    'furniture_category' : 'Furniture'
}

provider_dict = {
    'tech_provider' : 'TechSupply',
    'office_provider' : 'OfficeMax'
}


# ───────────────────────────────────────────────────────────────────────────
# TASK 1: High Value Products Report
# ───────────────────────────────────────────────────────────────────────────
high_value_products = (
    df.loc[(df['price'] >= 800000) 
           & (df['rating'] >= 4.5) 
           & (df['is_active'] == 1), 
           ['product_name', 'price', 
            'rating', 'stock', 'supplier']]
    .sort_values('price', ascending=False)
)
print(f"\nHigh Value Products:\n{high_value_products}\n")

# ───────────────────────────────────────────────────────────────────────────
# TASK 2: Critical Stock Analysis
# ───────────────────────────────────────────────────────────────────────────
critical_stock = (
    df.loc[(df['stock'] < 25) 
           & (df['is_active'] == 1) 
           & ~(df['category'] == "Furniture"),
           ['product_name', 'category', 'stock','supplier']])

print(f"\nCritical Stock Products:\n{critical_stock}\n")

# ───────────────────────────────────────────────────────────────────────────
# TASK 3: Mid Range Electronics
# ───────────────────────────────────────────────────────────────────────────            
mid_range_electronics = (
    # I pass the category name using the category_dict to make the code more readable
    # and in a future, i can change the category name in the category_dict to 
    # make the code more scalable
    df.query('category == @category_dict["electronic_category"]')
    .loc[(df['price'].between(100000, 500000)) & (df['stock'] >= 30), 
        ['product_name', 'price', 'stock', 'rating']]
)

print(f"\nMid Range Electronics:\n{mid_range_electronics}\n")

# ───────────────────────────────────────────────────────────────────────────
# TASK 4: Top 5 Products by Category
# ───────────────────────────────────────────────────────────────────────────

"""
   Over here, I'm going to use the function get_category to get the top 5 products by category
   
   I'll only need to pass the required args, being the df and the category name, using 
   the category_dict to get the category name, and in a future, i should put more than one 
   category to get the top 5 products by category, using a loop to iterate over the 
   category_dict
"""

# By this function, i can economize lines of code, and make the code more readable
# Two same tasks are being done, but with different arguments
top_electronics = get_category(df, category_dict['electronic_category'])
top_furniture = get_category(df, category_dict['furniture_category'])

print(f"\nTop 5 Electronics Products:\n{top_electronics}\n")
print(f"\nTop 5 Furniture Products:\n{top_furniture}\n")

# ───────────────────────────────────────────────────────────────────────────
# TASK 5: Featured Products Search
# ───────────────────────────────────────────────────────────────────────────
# str.contains is very similar to the LIKE operator in SQL
# It allows me to search for a pattern in a string
# The pattern is 'Gaming|Ergonómica|HD|WiFi', which means I'm looking for products that contain
# 'Gaming' or 'Ergonómica' or 'HD' or 'WiFi' in their name
# case=False means that the search is case-insensitive

featured_products = (df.loc[df['product_name'].str.contains
                    ('Gaming|Ergonómica|HD|WiFi', case=False), 
                    ['product_name', 'category', 'price']])

print(f"\nFeatured Products:\n{featured_products}\n")

# ───────────────────────────────────────────────────────────────────────────
# TASK 6: Supplier Analysis
# ───────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("SUPPLIER ANALYSIS")
print("=" * 70)


# TechSupply
"""
    Like in the get_category function, i'm going to use the function provider_analysis to get the top 5 products by category
    
    And over here, the criteria are the same, but instead of category, i'm going to use the provider name
    
    The provider name is 'TechSupply', which means I'm looking for products that contain
    'TechSupply' in their name
"""
tech_supply = provider_analysis(df, provider_dict['tech_provider'])
print("Supplier Analysis - TECHSUPPLY:\n")
print(f"Quantity of active products: {tech_supply[0]}")
print(f"Average price: ${tech_supply[1]['price']:,.0f}")
print(f"Average rating: {tech_supply[1]['rating']:.2f}")
print(f"Total stock: {tech_supply[2]}")

# OfficeMax
office_max = provider_analysis(df,provider_dict['office_provider'])
print("\nSupplier Analysis - OFFICEMAX:\n")
print(f"Quantity of active products: {office_max[0]}")
print(f"Average price: ${office_max[1]['price']:,.0f}")
print(f"Average rating: {office_max[1]['rating']:.2f}")
print(f"Total stock: {office_max[2]}")



# ───────────────────────────────────────────────────────────────────────────
# TASK 7: Export Reports
# ───────────────────────────────────────────────────────────────────────────
reports_dict = {
    "hvr" : "report_high_value.csv",
    "cls" : "report_critical_stock.csv",
    "mde" : "report_mid_range_electronics.csv"
}

hvr_report = reports(high_value_products, reports_dict['hvr'])
cls_report = reports(critical_stock, reports_dict['cls'])
mde_report = reports(mid_range_electronics, reports_dict['mde'])


# ───────────────────────────────────────────────────────────────────────────
# TASK 8: Validation and Summary
# ───────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("VALIDATION OF RESULTS")
print("=" * 70)

"""
    This dict is used to validate the results of the previous tasks
    It contains the names of the variables and the names of the reports
    The keys are the names of the variables and the values are the names of the reports
    The values are the names of the reports

    It goes with the hand with the Validation Function, basically, to make the process of validation easier
    Instead of writing the same code for each variable, I can just use the validation function
    to validate the results of the previous tasks
"""

df_var_dict = {
    "hvp_name": "high_value_products",
    "cls_name": "critical_stock",
    "mde_name": "mid_range_electronics",
    "tpe_name": "top_electronics",
    "tpf_name": "top_furniture",
    "fp_name": "featured_products",
}

def validation(var, df):        
    result = (
        print(f"\n- Variable name: {var}"), # This arg will be the dict and its key:value specified in the dict
        print(f"- Products found: {len(df)}"),
        print(f"- Columns included: {df.columns.tolist()}"),
        print(f"- First 2 rows:\n{df.head(2)}")
    )
    return result

# high_value_products
hvp_validation = validation(df_var_dict['hvp_name'], high_value_products)

# critical_stock
cls_validation = validation(df_var_dict['cls_name'], critical_stock)

# mid_range_electronics
mde_validation = validation(df_var_dict['mde_name'], mid_range_electronics)

# top_electronics
tpe_validation = validation(df_var_dict['tpe_name'], top_electronics)

# top_furniture
tpf_validation = validation(df_var_dict['tpf_name'], top_furniture)

# featured_products
fp_validation = validation(df_var_dict['fp_name'], featured_products)


print("\n" + "=" * 70)
print("PROJECT COMPLETED")
print("=" * 70)
