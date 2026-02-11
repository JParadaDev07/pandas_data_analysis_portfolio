import pandas as pd
from pathlib import Path

prompt = Path(__file__).parent

# EXERCISE 1.5: Export data
"""
NEW CONCEPT: .to_csv()

1. Import the complete CSV
2. Filter only employees from the 'IT' department
3. Export the result to a new file: 'it_employees.csv'
4. Verify that it was created correctly by importing it again

Look for: pd.DataFrame.to_csv() in documentation
"""
# Code:
# I used the 'new_file_name' variable to store the name of the new file
new_file_name = "it_employees.csv"
# I used the 'output' variable to store the path of the new file
output = prompt.parent / "data/reports" / new_file_name

df = pd.read_csv(prompt.parent / "data/datasets/employees.csv")
it_employees = df.query('department == "IT"')
# I used the try-except block to handle potential errors when exporting the file
try:
    it_employees.to_csv(output, index=False)
    print("File exported successfully!")
except PermissionError:
    print(f"\nERROR: Permission denied to export in: {output}")
except Exception as e:
    print(f"\nAn unexpected error occurred while trying to export: {e}")

# Finally, i use the .to_csv() method to export the data to a new file.
df_exported = pd.read_csv(prompt.parent / "data/reports/it_employees.csv", index_col="id")

print(df_exported)

