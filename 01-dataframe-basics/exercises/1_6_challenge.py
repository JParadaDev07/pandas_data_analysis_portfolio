"""
CHALLENGE - Block 1: Importation
========================================

Objective:
Import employees.csv with the following conditions:

1. Only load rows with id from 5 to 12 (8 employees total)
   - Search for the 'skiprows' parameter in the pd.read_csv() documentation
   - I'll need to skip the rows I don't want (id 1-4 and 13-15)
   
2. Only load these columns: name, department, salary, city

3. Use the 'name' column as the index of the DataFrame

4. Export the result to 'challenge_output.csv' in the data/reports folder
   IMPORTANT: The exported CSV must NOT include the index

Restrictions:
- Do NOT use .query() or boolean indexing filtering
- EVERYTHING must be done in the importation/exportation using parameters
- I'll not give you the exact names of the parameters (research in the documentation)

Final validation:
The challenge_output.csv file must have:
- 8 rows (employees with id 5-12)
- 4 columns (name, department, salary, city)
- No additional numeric index column
- The 'name' column must NOT appear as a column (because it's the index)

Useful documentation:
https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
"""

# Code:
import pandas as pd
from pathlib import Path

prompt = Path(__file__).parent

# Step 1: Import with the specified conditions
new_file_name = "challenge_output.csv"
output = prompt.parent / "data/reports" / new_file_name
df = pd.read_csv(prompt.parent / "data/datasets/employees.csv", 
                 skiprows=[1,2,3,4,13,14,15],  
                 usecols=['name', 'department', 'salary', 'city'])

# Step 2: Verify that it was imported correctly
print(df)
print(f"\nShape of the DataFrame: {df.shape}")
print(f"\nIndex: {df.index}")

# Step 3: Export to challenge_output.csv
try:
   df.to_csv(output, index=False)
   print("File exported successfully!")
except PermissionError:
   print(f"\nPermission denied to export in: {output}")
except Exception as e:
   print(f"\nAn unexpected error occurred while trying to export: {e}")
   
# Step 4: Verify that it was exported correctly
df_verificacion = pd.read_csv(prompt.parent / "data/reports/challenge_output.csv", index_col="name")
print(f"\nExported file:\n{df_verificacion}")

