"""
═══════════════════════════════════════════════════════════════
    MINI-PROJECT BLOCK 1: IMPORTATION
═══════════════════════════════════════════════════════════════

CONTEXT:
You are a data analyst in a Colombian company. The director asks you for
a consolidated report of Q3 2023 combining employee, sales
and departments.

AVAILABLE FILES:
1. employees.csv - Employee information (15 records)
2. sales_q3.csv - Sales of Q3 2023 (20 records)
3. departments.csv - Department information (5 records)

═══════════════════════════════════════════════════════════════
    TASKS TO DO
═══════════════════════════════════════════════════════════════

TASK 1: Importation of employees from the commercial area
─────────────────────────────────────────────────────
Import ONLY employees who work in sales (Marketing).

Requirements:
- File: employees.csv
- Only employees with id 1, 2, 5, 10, 15 (use skiprows strategically)
- Columns: name, age, salary, city, hire_date
- Use 'name' as index
- Save in variable: df_sales_team

- You will have to skip the rows you DON'T want (the other departments)


TASK 2: Importation of sales data for August
─────────────────────────────────────────────────────
Import ONLY the sales for the month of August.

Requirements:
- File: sales_q3.csv
- Only the first 10 rows after the header (contain data from July and August)
- You will need to identify which ones are from August (but that's filtering, 
  so for now just import the first 10 rows)
- Columns: employee_id, month, sales_amount, region
- Do NOT use a custom index (default numeric index)
- Save in variable: df_august_sales

- Use nrows to limit the reading


TASK 3: Importation of department information
─────────────────────────────────────────────────────
Import all departments except Operations.

Requirements:
- File: departments.csv
- All rows EXCEPT row 5 (Operations)
- Columns: dept_code, department_name, manager_name, budget
- Use 'dept_code' as index
- Save in variable: df_departments

- Use skiprows to skip row 5


TASK 4: Exportation of reports
─────────────────────────────────
Export the 3 DataFrames to separate CSV files:

1. df_sales_team → 'report_sales_team.csv'
   - WITHOUT index in the exported file
   
2. df_august_sales → 'report_august_sales.csv'
   - WITHOUT index in the exported file
   
3. df_departments → 'report_departments.csv'
   - WITH index in the exported file (because dept_code is important)

All files must be saved in the 'data/reports' folder


TASK 5: Validation and basic analysis
───────────────────────────────────────────────────────────────
For each DataFrame, show:
- The first 3 rows
- The shape
- The column names
- The type of index it has

═══════════════════════════════════════════════════════════════
    RESTRICTIONS
═══════════════════════════════════════════════════════════════

DO NOT use filtering (.query(), boolean indexing)
DO NOT use concatenation or merge (that's Block 4)
DO NOT use functions you haven't seen in Block 1
ONLY use: read_csv(), to_csv(), info(), describe(), head(), shape

═══════════════════════════════════════════════════════════════
    SUCCESS CRITERIA
═══════════════════════════════════════════════════════════════

The 3 CSV files are exported correctly
The code runs without errors
The reports contain the correct information

═══════════════════════════════════════════════════════════════
    ESTIMATED TIME: 45-60 minutes
═══════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════
#                             CODE:
# ═══════════════════════════════════════════════════════════════

import pandas as pd
from pathlib import Path

route = Path(__file__).parent

# ───────────────────────────────────────────────────────────────
# TASK 1: Importation of sales employees
# ───────────────────────────────────────────────────────────────
df_sales_team = pd.read_csv(route.parent / "data/datasets/employees.csv",
                            usecols=['name', 'age', 'salary', 'city', 'hire_date'], # Import only the requested columns 
                            skiprows=[2,3,4,6,7,8,9,11,12,13,14])  # Exclude all employees who were not in the Marketing department
                            
# ───────────────────────────────────────────────────────────────
# TASK 2: Importation of sales data for August
# ───────────────────────────────────────────────────────────────
df_august_sales = pd.read_csv(route.parent / "data/datasets/sales_q3.csv",
                          nrows=10, # Import only the first 10 rows
                          usecols=['employee_id', 'month', 'sales_amount', 'region']) # Import only the requested columns
                                        
# ───────────────────────────────────────────────────────────────
# TASK 3: Importation of departments information
# ───────────────────────────────────────────────────────────────
df_departments = pd.read_csv(route.parent / "data/datasets/departments.csv",
                             skiprows=[5], # How do I know the last record is from the 'Operations' department, I import the file without the last row
                             usecols=['dept_code', 'department_name', 'manager_name', 'budget']) 

# ───────────────────────────────────────────────────────────────
# TASK 4: Exportation of reports
# ───────────────────────────────────────────────────────────────
# I created a list for more organized code and to avoid DRY (Don't Repeat Yourself)
report_names = ["report_sales_team.csv", "report_august_sales.csv", "report_department.csv"]
# I created too a list with the dataframes names to iterate over them
data_frames = [df_sales_team, df_august_sales, df_departments]
output_dir = route.parent / "data/reports"
""" This is to avoid the error of the directory not existing, basically here i create the directory 
if it doesn't exist with the mkdir() method and the exist_ok=True parameter 
"""
output_dir.mkdir(parents=True, exist_ok=True)

# Over here, i unzip the lists to iterate over them
for df, name in zip(data_frames, report_names):
    output_path = output_dir / name
    try:
       df.to_csv(output_path, index=False)
       print("File exported successfully")
    except PermissionError:
       print(f"\nPermission denied to export in: {output_dir}")
    except Exception as e:
       print(f"\nAn unexpected error occurred while trying to export: {e}")
    

# ───────────────────────────────────────────────────────────────
# TASK 5: Validation and basic analysis
# ───────────────────────────────────────────────────────────────

print("=" * 70)
print("VALIDATION OF DATAFRAMES")
print("=" * 70)

# df_sales_team
print("\n" + "=" * 50 + "SALES TEAM" + "=" * 50)
print(f"\nFirst 3 rows:\n{df_sales_team.head(3)}")
print(f"\nShape: {df_sales_team.shape}")
print(f"\nColumn names: {df_sales_team.columns}")
print(f"\nIndex type: {df_sales_team.index.dtype}")
# # df_august_sales
print("\n" + "=" * 50 + "AUGUST SALES" + "=" * 50)
print(f"\nFirst 3 rows:\n{df_august_sales.head(3)}")
print(f"\nShape: {df_august_sales.shape}")
print(f"\nColumn names: {df_august_sales.columns}")
print(f"\nIndex type: {df_august_sales.index.dtype}\n")
# # df_departments
print("\n" + "=" * 50 + "DEPARTMENTS" + "=" * 50)
print(f"\nFirst 3 rows:\n{df_departments.head(3)}")
print(f"\nShape: {df_departments.shape}")
print(f"\nColumn names: {df_departments.columns}")
print(f"\nIndex type: {df_departments.index.dtype}\n")

print("\n" + "=" * 70)
print("PROJECT COMPLETED ✅")
print("=" * 70)
