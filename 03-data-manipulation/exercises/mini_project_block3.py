"""
═══════════════════════════════════════════════════════════════════════════
    INTEGRATIVE MINI-PROJECT - BLOCK 3: DATA MANIPULATION
═══════════════════════════════════════════════════════════════════════════

CONTEXT:
You are a Data Analyst at a tech company. The HR Manager needs a complete
and automated payroll analysis with multiple transformations and categorizations
for the annual review.

AVAILABLE FILES:
1. employees.csv - Data for 20 employees

═══════════════════════════════════════════════════════════════════════════
    TASKS TO PERFORM
═══════════════════════════════════════════════════════════════════════════

TASK 1: Personal Data Preparation
─────────────────────────────────────────────────────
Enrich personal information:

Requirements:
- 'full_name_formatted': Full name in title case (First Letter Capitalized)
- 'first_name': First name only
- 'last_name': Last name only
- 'name_length': Length of the full name
- 'initials': Initials in format "A.G." 
  HINT: Split name, take first character of each part, join with dot

Save columns in: df (modify the original DataFrame)


TASK 2: Corporate Email Transformation
─────────────────────────────────────────────────────
The company is migrating to a new domain:

Requirements:
- 'email_username': Username (before @)
- 'email_domain_old': Current domain (after @)
- 'email_new': Replace '@company.com' with '@techcorp.global'
- 'email_professional': Format "[FirstName].[LastName]@techcorp.global"
  HINT: Use lowercased first_name and last_name

Validation: All emails_new must end with '@techcorp.global'


TASK 3: Complete Salary Analysis
─────────────────────────────────────────────────────
Calculate compensations and categories:

Requirements:
- 'annual_salary': Monthly salary * 12
- 'salary_in_k': Monthly salary / 1000 (rounded to 1 decimal)
- 'salary_bracket': Use nested np.where():
  * 'Premium' if >= 55000
  * 'Alto' if >= 48000
  * 'Competitivo' if >= 40000
  * 'Estándar' otherwise

- 'performance_bonus_monthly': Use custom function with .apply():
  * If performance_score >= 90: salary * 0.20
  * If performance_score >= 85: salary * 0.15
  * If performance_score >= 75: salary * 0.10
  * If not: salary * 0.05

- 'total_monthly_comp': salary + performance_bonus_monthly
- 'total_annual_comp': total_monthly_comp * 12

HINT: Define function calculate_bonus(score, salary) and use it with .apply()


TASK 4: Performance Evaluation
─────────────────────────────────────────────────────
Categorize employee performance:

Requirements:
- 'performance_grade': Use .map() with dictionary:
  First create ranges with np.where():
  * 90-100 → 'A+'
  * 85-89 → 'A'
  * 80-84 → 'B+'
  * 75-79 → 'B'
  * 70-74 → 'C'
  * <70 → 'D'

- 'performance_category': Use .map():
  * 'A+', 'A' → 'Sobresaliente'
  * 'B+', 'B' → 'Satisfactorio'
  * 'C', 'D' → 'Necesita Mejorar'

- 'needs_coaching': Boolean
  * True if performance_score < 75
  * False otherwise


TASK 5: Experience and Tenure Analysis
─────────────────────────────────────────────────────
Categorize by experience:

Requirements:
- 'hire_year': Extract year from hire_date (use .str.split('-').str[0] and convert to int)
- 'years_in_company': 2024 - hire_year
- 'seniority_level': Use np.where:
  * 'Director' if years_of_experience >= 10
  * 'Senior' if >= 7
  * 'Mid-Level' if >= 4
  * 'Junior' if >= 2
  * 'Entry-Level' otherwise

- 'tenure_category': Based on years_in_company:
  * 'Veterano' if >= 6
  * 'Establecido' if >= 4
  * 'Consolidado' if >= 2
  * 'Nuevo' otherwise

- 'eligible_for_sabbatical': Boolean
  * True if years_in_company >= 5 AND performance_score >= 80


TASK 6: Department Analysis
─────────────────────────────────────────────────────
Encode and analyze departments:

Requirements:
- 'dept_code': Use .map() with dictionary:
  * IT → 'TEC'
  * HR → 'RHH'
  * Sales → 'VTA'
  * Finance → 'FIN'

- 'is_tech_dept': Boolean (True if department is 'IT')
- 'is_revenue_dept': Boolean (True if department is 'Sales' or 'Finance')

- 'employee_classification': Use function with .apply(axis=1):
  Format: "[Dept_Code]-[Seniority_Level]-[Performance_Grade]"
  Example: "TEC-Senior-A"


TASK 7: Key Talent Identification
─────────────────────────────────────────────────────
Identify strategic employees (Boolean columns):

Requirements:
- 'high_performer': performance_score >= 85 AND years_of_experience >= 5
- 'retention_risk': salary_bracket in ['Estándar', 'Competitivo'] AND performance_score >= 80
- 'promotion_candidate': 
  * years_in_company >= 2 AND
  * performance_score >= 85 AND
  * years_of_experience >= 4

- 'star_employee':
  * performance_score >= 90 OR
  * (performance_score >= 85 AND years_of_experience >= 8)


TASK 8: Geographic Analysis
─────────────────────────────────────────────────────
Categorize by location:

Requirements:
- 'city_tier': Use .map():
  * Bogotá, Medellín → 'Tier 1'
  * Cali, Barranquilla → 'Tier 2'
  * Others → 'Tier 3' (use .fillna())

- 'region': Use .map():
  * Bogotá → 'Centro'
  * Medellín → 'Antioquia'
  * Cali → 'Valle'
  * Cartagena, Barranquilla → 'Caribe'
  * Others → 'Otra' (use .fillna())


TASK 9: Descriptive Report
─────────────────────────────────────────────────────
Create descriptive text columns:

Requirements:
- 'employee_summary': Use .apply(axis=1) with function returning:
  "[Name] is [Seniority_Level] at [Department] with [X] years of experience and rating [Performance_Grade]"
  
  Example: "Ana García is Senior at IT with 5 years of experience and rating A"

- 'compensation_summary': 
  "Salary: $[salary_in_k]K, Bracket: [salary_bracket], Bonus: [performance_bonus %]"
  
  Example: "Salary: $45.0K, Bracket: Competitivo, Bonus: 15%"


TASK 10: Cleanup and Final Export
─────────────────────────────────────────────────────
1. Rename original columns to Spanish:
   - name → nombre
   - department → departamento
   - salary → salario_base
   - performance_score → calificacion
   - hire_date → fecha_contratacion
   - years_of_experience → años_experiencia

2. Create final DataFrame 'employee_report' with ONLY these columns (in order):
   ['nombre', 'email_new', 'departamento', 'dept_code', 'salario_base',
    'salary_bracket', 'annual_salary', 'performance_grade', 'seniority_level',
    'years_in_company', 'high_performer', 'promotion_candidate', 'city', 'region']

3. Sort by: departamento (ascending), then calificacion (descending)

4. Export 'employee_report' to 'final_employee_analysis.csv' in resources/
   - No index
   - With error handling


TASK 11: Statistical Analysis
─────────────────────────────────────────────────────
Calculate and show:
- Total high_performers
- Total promotion_candidates
- Total retention_risk
- Average salary by salary_bracket (use .groupby())
- Count of employees by department and seniority_level (use .groupby() with 2 columns)


TASK 12: Final Validation
──────────────────────────────────────────────────────
Show:
- Shape of final DataFrame
- Included columns
- First 5 rows of the report
- Last 3 rows of the report
- Data types info (.dtypes)

═══════════════════════════════════════════════════════════════════════════
    RESTRICTIONS
═══════════════════════════════════════════════════════════════════════════

❌ DO NOT use functions outside Block 3
❌ DO NOT use merge, concat, pivot (that's for future blocks)
✅ YOU CAN use: .apply(), .map(), .str, np.where(), basic operations,
                .rename(), .drop(), .sort_values(), .groupby()

═══════════════════════════════════════════════════════════════════════════
    SUCCESS CRITERIA
═══════════════════════════════════════════════════════════════════════════

✅ All columns created correctly
✅ All calculations are accurate
✅ Custom functions well defined
✅ Correct use of .apply(), .map(), np.where()
✅ Final DataFrame exported correctly
✅ Statistical analyses correct
✅ Code executes without errors

═══════════════════════════════════════════════════════════════════════════
    ESTIMATED TIME: 90-120 minutes
═══════════════════════════════════════════════════════════════════════════

NOTES:
- This project is LONGER than Block 2, but each task is simple
- Work on one task at a time, validate it works before continuing
- Use print() to verify intermediate results
- The reference guide has examples of ALL necessary techniques

GOOD LUCK! 🚀
"""

# ═══════════════════════════════════════════════════════════════════════════
#     YOUR CODE HERE
# ═══════════════════════════════════════════════════════════════════════════

import pandas as pd
import numpy as np
import operator
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / 'data/datasets/employees.csv') # Updated path for structure

# ───────────────────────────────────────────────────────────────────────────
# TASK 1: Personal Data Preparation
# ───────────────────────────────────────────────────────────────────────────

# Cleaning up names
# Title case looks better on reports (juan perez -> Juan Perez)
df['full_name_formatted'] = df['name'].str.capitalize()

# Extracting first and last names
# We assume the name is "First Last", so split by space ' '
df['first_name'] = df['name'].str.split(' ').str[0]
df['last_name'] = df['name'].str.split(' ').str[1]

# Counting characters (sometimes useful for ID generation or validation)
df['name_length'] = df['name'].str.len()

# Creating initials (e.g. J.P.)
# We take the first letter of each word in the name
df['initials'] = df['name'].apply(lambda x: ' '.join([word[0] for word in x.split()]))

print(f"\n{df[['name', 'full_name_formatted', 'first_name', 'last_name', 'name_length', 'initials']]}")

# ───────────────────────────────────────────────────────────────────────────
# TASK 2: Corporate Email Transformation
# ───────────────────────────────────────────────────────────────────────────

# Breaking down the email
df['email_username'] = df['email'].str.split('@').str[0]
df['email_domain_old'] = df['email'].str.split('@').str[1]

# Simple replace: Updating the domain
df['email_new'] = df['email'].str.replace('company.com', 'techcorp.global')

# Constructing a standardized professional email
# Format: firstname.lastname@techcorp.global
# We force lowercase to keep it clean
df['email_professional'] = (
  df['first_name'].str.lower() + '.' + df['last_name'].str.lower() + '@' + 'techcorp.global'
)

print(f"\n{df['email_professional']}")


# ───────────────────────────────────────────────────────────────────────────
# TASK 3: Complete Salary Analysis
# ───────────────────────────────────────────────────────────────────────────

# 1. Flexible Calculation Block
"""
   This is the heavy lifter of the project! 💪
   It handles both:
   1. Simple logic (If X then Y)
   2. Complex math expressions saved as strings ("salary * 0.15")
   
   It's built to be safe: it tries to calculate things, but if it fails (because of bad data),
   it keeps going without crashing using try/except.
"""
def salarial_and_others_block(
  df,
  nc,
  conditions=None,
  ret_args=None,
  default=None
):
  ret_args_evaluated = []

  # We check every result to see if it's a formula to solve or just a value
  for expr in ret_args:
    if isinstance(expr, str) and any(op in expr for op in ['*', '+', '-', '/']):
      try:
        # Try to solve the math formula
        ret_args_evaluated.append(df.eval(expr))
      except Exception:
        # If it fails, just use the value as is (better safe than sorry)
        ret_args_evaluated.append(expr)
    else:
      ret_args_evaluated.append(expr)

  # Same logic for the default value (the "else" part)
  if isinstance(default, str) and any(op in default for op in ['*', '+', '-', '/']):
    try:
      default_evaluated = df.eval(default)
    except Exception:
      default_evaluated = default
  else:
    default_evaluated = default

  default_array = np.array(default_evaluated, dtype='object')

  # Evaluate all conditions and apply the results
  conditions = [df.eval(cond) for cond in conditions]
  df[nc] = np.select(conditions, ret_args_evaluated, default_array)
  
  return df


# ───────────────────────────────────────────────────────────────────────────
# TASK 3: Complete Salary Analysis
# ───────────────────────────────────────────────────────────────────────────

# Let's crunch some numbers! 
# First, basic math for annual salary and a "pretty" version in K (thousands)
df['annual_salary'] = df['salary'] * 12
df['salary_in_k'] = ((df['salary'] / 1000).round(1)).astype('str') + 'K'

# Categorizing salaries using our Flexible Calculation Block
# It's like sorting candy into buckets: Premium, High, Competitive, or Standard
df = salarial_and_others_block(
  df,
  'salary_bracket',
  conditions=[
    'salary >= 55000',
    'salary >= 48000',
    'salary >= 40000'
  ],
  ret_args=[
    'Premium', 'Alto', 'Competitivo'
  ],
  default='Estándar'
)

# Calculating bonuses based on performance
# Better performance = more money! 
df = salarial_and_others_block(
  df,
  'performance_bonus_monthly',
  conditions=[
    'performance_score >= 90',
    'performance_score >= 85',
    'performance_score >= 75'
  ],
  ret_args=[
    'salary * 0.20',
    'salary * 0.15',
    'salary * 0.10'
  ],
  default='salary * 0.05'
)

# Saving just the percentage number for reports later
df = salarial_and_others_block(
  df,
  'performance_bonus_percentage',
  conditions=[
    'performance_score >= 90',
    'performance_score >= 85',
    'performance_score >= 75'
  ],
  ret_args=[
    '20',
    '15',
    '10'
  ],
  default='5'
)

# Final addition: Base Salary + Bonus
df['total_monthly_comp'] = (df['salary'] + df['performance_bonus_monthly'])
df['total_annual_comp'] = df['total_monthly_comp'] * 12

print(df[['salary', 'annual_salary', 'salary_in_k', 'salary_bracket', 'performance_bonus_monthly', 'total_monthly_comp', 'total_annual_comp']])


# ───────────────────────────────────────────────────────────────────────────
# TASK 4: Performance Evaluation
# ───────────────────────────────────────────────────────────────────────────

# Assigning letter grades (A+, A, B...) based on score
df = salarial_and_others_block(
  df,
  'performance_grade',
  conditions=[
    'performance_score >= 90',
    'performance_score >= 85',
    'performance_score >= 80',
    'performance_score >= 75',
    'performance_score >= 70'
  ],
  ret_args=[
    'A+', 'A', 'B+', 'B', 'C'
  ],
  default='D'
)

# Grouping grades into broader categories
# We check if the grade is in a list of good grades
df = salarial_and_others_block(
  df,
  'performance_category',
  conditions=[
    'performance_grade in ["A+", "A"]',
    'performance_grade in ["B+", "B"]',
    'performance_grade in ["C", "D"]',
  ],
  ret_args=[
    'Sobresaliente', 'Satisfactorio', 'Necesita Mejorar'
  ],
  default='Sin calificación registrada'
)

# Identify who needs help (Score < 75)
df['needs_coaching'] = np.where(df['performance_score']  < 75, True, False)

print(df[['name', 'performance_score', 'performance_grade', 'performance_category', 'needs_coaching']])


# ───────────────────────────────────────────────────────────────────────────
# TASK 5: Experience and Tenure Analysis
# ───────────────────────────────────────────────────────────────────────────

# Defining seniority levels based on years of experience
df = salarial_and_others_block(
  df, 
  'seniority_level',
  conditions=[
    'years_of_experience >= 10',
    'years_of_experience >= 7',
    'years_of_experience >= 4',
    'years_of_experience >= 2',
  ],
  ret_args=[
    'Director',
    'Senior',
    'Mid-Level',
    'Junior'
  ],
  default='Entry-Level'
)

# Analyzing loyalty (Time in company)
# We extract the year from the hire_date string
df['hire_year'] = df['hire_date'].str.split('-').str[0].astype(int)

# Assuming current year is 2026 (for this exercise)
df['years_in_company'] = (2026 - df['hire_year'])

# Categorizing tenure (how long they've stuck around)
df = salarial_and_others_block(
  df, 
  'tenure_category',
  conditions=[
    'years_in_company >= 6',
    'years_in_company >= 4',
    'years_in_company >= 2',
  ],
  ret_args=[
    'Veterano',
    'Establecido',
    'Consolidado',
  ],
  default='Nuevo'
)

# Checking if they deserve a break (Sabbatical)
# Must be loyal (5+ years) AND good performer (80+ score)
df = salarial_and_others_block(
  df, 
  'elegible_for_sabbatical',
  conditions=[
    'years_in_company >= 5 and performance_score >= 80',
  ],
  ret_args=[True],
  default=False
)

print(df[['name', 'performance_score', 'years_of_experience', 'seniority_level', 'hire_year', 'years_in_company', 'tenure_category', 'elegible_for_sabbatical']])

# ───────────────────────────────────────────────────────────────────────────
# TASK 6: Department Analysis
# ───────────────────────────────────────────────────────────────────────────

# Mapping departments to short codes used internally
dept_code_dict = {
   'IT': 'TEC',
   'HR': 'RHH',
   'Sales': 'VTA',
   'Finance': 'FIN'
}

df['dept_code'] = df['department'].map(dept_code_dict)

# Boolean flags: True/False for department types
df['is_tech_dept'] = np.where(df['department'] == 'IT', True, False)

# Checking multiple values. "Is this dept in the list of money-makers?"
salarial_and_others_block(
  df,
  'is_revenue_dept',
  conditions=[
    'department in ["Sales", "Finance"]'
  ],
  ret_args=[True],
  default=False
)

# 2. String Builder Function
"""
   Simple but effective!
   It takes a template (like "Hello {name}") and fills the blanks using data from the row.
   Perfect for creating reports or descriptions in a single line.
"""
def concat_values(
  df,
  nc,
  template
):
  # Using f-string logic (but with .format method) for each row
  df[nc] = df.apply(lambda row: template.format(**row), axis=1)
  return df

# Creating a unique ID string for each employee
# Format: DEPT-LEVEL-GRADE (e.g. TEC-Senior-A)
df = concat_values(
  df,
  'employee_classification',
  template="{dept_code}-{seniority_level}-{performance_grade}"
)

print(df[['department', 'dept_code', 'is_tech_dept', 'is_revenue_dept', 'employee_classification']])
# ───────────────────────────────────────────────────────────────────────────
# TASK 7: Key Talent Identification
# ───────────────────────────────────────────────────────────────────────────

# Building our "Dream Team" roster using logic

# 1. High Performer: Good results over a long time
df = salarial_and_others_block(
  df,
  'high_performer',
  conditions=[
    'performance_score >= 85 & years_of_experience >= 5'
  ],
  ret_args=[True],
  default=False
)

# 2. Flight Risk: Good employee, potentially underpaid
df = salarial_and_others_block(
  df,
  'retention_risk',
  conditions=[
    'salary_bracket in ["Estándar", "Competitivo"] & performance_score >= 80'
  ],
  ret_args=[True],
  default=False
)

# 3. Future Leader: Loyal, good results, experienced
df = salarial_and_others_block(
  df,
  'promotion_candidate',
  conditions=[
    'years_in_company >= 2 & performance_score >= 85 & years_of_experience >= 4'
  ],
  ret_args=[True],
  default=False
)

# 4. STAR: The absolute best of the best
df = salarial_and_others_block(
  df,
  'star_employee',
  conditions=[
    'performance_score >= 90 or performance_score >= 85 & years_of_experience >= 8'
  ],
  ret_args=[True],
  default=False
)

print(df[['name', 'performance_score', 'years_of_experience', 'years_in_company', 
          'salary_bracket', 'high_performer', 'retention_risk', 'promotion_candidate',
          'star_employee']])



# ───────────────────────────────────────────────────────────────────────────
# TASK 8: Geographic Analysis
# ───────────────────────────────────────────────────────────────────────────

# Mapping cities to economic tiers
city_tier_dict = {
  'Bogotá': 'Tier 1',
  'Medellín': 'Tier 1',
  'Cali': 'Tier 2',
  'Barranquilla': 'Tier 2'
}

# Mapping cities to regions
region_dict = {
  'Bogotá': 'Centro',
  'Medellín': 'Antioquia',
  'Cali': 'Valle',
  'Cartagena': 'Caribe',
  'Barranquilla': 'Caribe'
}

# Apply mappings and fill gaps (fillna) for cities we missed
df['city_tier'] = df['city'].map(city_tier_dict).fillna('Tier 3')
df['region'] = df['city'].map(region_dict).fillna('Otra')

print(df[['city', 'city_tier', 'region']])


# ───────────────────────────────────────────────────────────────────────────
# TASK 9: Descriptive Report
# ───────────────────────────────────────────────────────────────────────────

# ───────────────────────────────────────────────────────────────────────────
# TASK 9: Descriptive Report
# ───────────────────────────────────────────────────────────────────────────

# Creating our stories (narrative columns)
# 1. Summary of the employee
df = concat_values(
  df,
  'employee_sumary',
  template="{name} es {seniority_level} en {department} con {years_of_experience} años de experiencia y calificación{performance_grade}"
)

# 2. Summary of their money
df = concat_values(
  df,
  'compensation_summary',
  template="Salario: ${salary_in_k}K, Bracket: {salary_bracket}, Bonus: {performance_bonus_percentage}%"
)

print(df[['name', 'seniority_level', 'department', 
      'years_of_experience', 'performance_grade', 'employee_sumary']])

print(df[['compensation_summary']])


# ───────────────────────────────────────────────────────────────────────────
# TASK 10: Cleanup and Final Export
# ───────────────────────────────────────────────────────────────────────────

# Renaming to Spanish (Client requirement?)
df = df.rename(columns={
  'name': 'nombre',
  'department': 'departamento',
  'salary': 'salario_base',
  'performance_score': 'calificacion',
  'hire_date': 'fecha_contratacion',
  'years_of_experience': 'años_experiencia'
})

print(df[['nombre', 'departamento', 'salario_base', 
        'calificacion', 'fecha_contratacion', 'años_experiencia']])

# Selecting only the columns we want in the final report
new_df = [
  'nombre', 
  'email_new', 
  'departamento', 
  'dept_code',
  'salario_base',
  'salary_bracket',
  'annual_salary',
  'performance_grade',
  'seniority_level',
  'years_in_company',
  'high_performer',
  'promotion_candidate',
  'city',
  'region'
]

# Creating the final clean copy
employee_report = df[new_df].copy()

# Sorting: By Dept (A-Z) and then by Score (Best to Worst)
employee_report.sort_values(by=['departamento', 'seniority_level'], 
            ascending=[True, False], inplace=True)
 
print(employee_report)

# Exporting safely
report_name = 'final_employee_analysis.csv'
output = current_dir.parent / 'data/reports/final_employee_analysis.csv' # Updated path

try:
  employee_report.to_csv(output, index=False)
except PermissionError:
  print(f"Permission denied for export to: {output}")
except Exception as e:
  print(f"An unexpected error occurred, please try again: {e}")

# ───────────────────────────────────────────────────────────────────────────
# TASK 11: Statistical Analysis
# ───────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("STATISTICAL ANALYSIS")
print("=" * 70)

# Quick stats for the boss
total_high_performers = employee_report['high_performer'].sum()
print(f"\nTotal Top Performers: {total_high_performers}")

total_promotion_candidates = employee_report['promotion_candidate'].sum()
print(f"\nTotal Eligible for Promotion: {total_promotion_candidates}")

total_retention_risk = df['retention_risk'].sum()
print(f"\nTotal Retention Risk: {total_retention_risk}")

# Who pays the best?
mean_by_bracket = df.groupby('salary_bracket')['salario_base'].mean()
print(f"\n{mean_by_bracket}")

# Heatmap of talent (Dept x Seniority)
employees_by = df.groupby(['departamento', 'seniority_level'])['nombre'].count()
print(f"\n{employees_by}")

# ───────────────────────────────────────────────────────────────────────────
# TASK 12: Final Validation
# ───────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("FINAL VALIDATION")
print("=" * 70)

print(f"\nShape: {employee_report.shape} (rows_cols)")
print(f"\nColumns:\n{employee_report.columns}")
print(f"\nFirst 5 rows:\n{employee_report.head(5)}")
print(f"\nLast 3 rows:\n{employee_report.tail(3)}")
print(f"\nData types:\n{employee_report.dtypes}")

print("\n" + "=" * 70)
print("PROJECT COMPLETED ✅")
print("=" * 70)
