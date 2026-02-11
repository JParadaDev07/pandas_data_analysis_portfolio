# 📁 Block 1: DataFrame Basics & Import
## 🎯 Overview
This fundamental block covers the essential skills for loading data into Pandas. We explore the powerful `read_csv()` function, learning how to selectively import data using parameters like `nrows`, `usecols`, `index_col`, and `skiprows`. The block culminates in a mini-project that simulates a real-world data consolidation task.
## 🧠 Learning Objectives
- **Import Data:** Load CSV files using specific parameters to optimize memory and relevance.
- **Inspect Structure:** specific Understand DataFrame dimensions, data types, and statistics.
- **Export Data:** Save processed DataFrames to new CSV files.
- **Selective Loading:** Import only specific rows (`skiprows`, `nrows`) and columns (`usecols`).
- **Index Management:** Set custom indices during import (`index_col`).
---
## 📝 Exercises Breakdown
### [1.1 Basic Import](./exercises/1_1.py)
**Goal:** Load the employee dataset and perform initial inspection.
- **Key functions:** `pd.read_csv()`, `.head()`, `.shape`, `.columns`.
- **Outcome:** Successful loading of the "employees.csv" file.
### [1.2 Data Inspection](./exercises/1_2.py)
**Goal:** Analyze data types and statistical summaries.
- **Key functions:** `.dtypes`, `.describe()`, `.select_dtypes(include='number')`.
- **Insight:** Distinguishing between numerical and object (string) data types.
### [1.3 Selective Import (Rows & Cols)](./exercises/1_3.py)
**Goal:** Import only specific subsets of the data.
- **Parameters:** `nrows=10` (first 10 rows), `usecols=['name', 'department', 'salary']`.
- **Outcome:** A lighter DataFrame containing only relevant information.
### [1.4 Custom Indexing](./exercises/1_4.py)
**Goal:** understand the impact of using a specific column as the DataFrame index.
- **Parameters:** `index_col='id'`.
- **Insight:** How setting an index changes the data display and structure compared to the default RangeIndex (0, 1, 2...).
### [1.5 Exporting Data](./exercises/1_5.py)
**Goal:** Filter data and save it to a new file.
- **Task:** Filter 'IT' department employees and export results.
- **Key functions:** `.to_csv(index=False)`, `try-except` for error handling.
- **Outcome:** Creation of [it_employees.csv](cci:7://file:///C:/Users/japar/OneDrive/Documentos/pandas_data_analysis_portfolio/01-dataframe-basics/data/reports/it_employees.csv:0:0-0:0) in the reports folder.
---
## 🏆 Challenge: Advanced Import
**File:** [`1_6_challenge.py`](./exercises/1_6_challenge.py)
**Objective:** Import a specific subset of employees (IDs 5-12) without using post-import filtering.
- **Constraint:** Must use `skiprows` logic to skip specific lines (header + unwanted rows).
- **Result:** A DataFrame with exactly 8 rows and 4 specific columns, using 'name' as the index, exported to [challenge_output.csv](cci:7://file:///C:/Users/japar/OneDrive/Documentos/pandas_data_analysis_portfolio/01-dataframe-basics/data/reports/challenge_output.csv:0:0-0:0).
---
## 🚀 Mini-Project: Q3 Reporting
**File:** [`mini_project_block1.py`](./exercises/mini_project_block1.py)
**Scenario:** You are a Data Analyst consolidating Q3 reports from multiple sources (Employees, Sales, Departments).
**Tasks Accomplished:**
1. **Sales Team Import:** Used `skiprows` to pick specific employees (IDs 1, 2, 5, 10, 15) from the marketing department.
2. **August Sales:** Extracted specific sales records using `nrows` and specific columns.
3. **Departments:** Imported department data excluding 'Operations' using `skiprows`.
4. **Reporting:** Exported three clean CSV reports (`report_sales_team.csv`, `report_august_sales.csv`, `report_department.csv`) to a dedicated reports folder.
5. **Validation:** Automated text-based validation of shapes and indices.
**Key takeaway:** Mastering `read_csv` parameters allows for "ETL-lite" operations (Extract, Transform, Load) directly during the import phase.
---
## 📂 Datasets Used
All datasets are located in the `data/` directory:
- [employees.csv](cci:7://file:///C:/Users/japar/OneDrive/Documentos/pandas_data_analysis_portfolio/01-dataframe-basics/data/employees.csv:0:0-0:0): Main employee records.
- [departments.csv](cci:7://file:///C:/Users/japar/OneDrive/Documentos/pandas_data_analysis_portfolio/01-dataframe-basics/data/departments.csv:0:0-0:0): Department codes and budgets.
- `sales_q3.csv`: Quarterly sales records.
---