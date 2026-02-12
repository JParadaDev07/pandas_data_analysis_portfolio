# 📁 Block 3: Data Manipulation
## 🎯 Overview
In Block 2, we learned how to *find* data. In **Block 3**, we learn how to **create** it.
This block marks the transition from passive data reading to **active data transformation**. We don't just accept the dataset as it is; we enrich it, clean it, and calculate new insights. The journey culminates in a professional-grade Payroll System that introduces a reusable **"Transformation Framework"**.

## 🧠 Learning Objectives
- **Column Creation:** Basic arithmetic (`salary * 12`) and boolean logic (`is_it_dept`).
- **String Engineering:** Master `.str` accessors for splitting, slicing, and formatting text.
- **Mapping & Decoding:** Use `.map()` with dictionaries to standardize categorical data.
- **Conditional Logic:** Move beyond simple filters to complex logic using `np.where()` and `np.select()`.
- **Function Abstraction:** Create reusable "Heavy Lifter" functions to handle repetitive tasks cleanly.

---

## 📝 Exercises Breakdown

### [3.1 Basic Column Creation](./exercises/3_1.py)
**Goal:** The basics of enriching a DataFrame.
- **Math:** Annualizing arithmetic (`salary * 12`).
- **Booleans:** Creating flags (`is_it_dept`) for binary classification.

### [3.3 Mapping & Standardization](./exercises/3_3.py)
**Goal:** decoding and standardizing categories.
- **Technique:** Using python dictionaries as lookup tables with `.map()`.
- **Application:** Converting 'IT' -> 'TEC', and mapping cities to regions.

### [3.4 String Operations Masterclass](./exercises/3_4.py)
**Goal:** deeply understanding text manipulation.
- **Tools:** `.str.split()`, `.str.upper()`, regex matching.
- **Innovation:** Introduction of `main_transform_function`, a first attempt at a generic wrapper for string operations.

### [3.5 Conditional Logic](./exercises/3_5.py)
**Goal:** sophisticated decision making.
- **Tools:** `np.where` for binary choices and `np.select` for multiple conditions (SQL CASE WHEN equivalent).
- **Outcome:** assigning tiers and bonuses based on complex criteria.

---

## 🏆 Challenge: The "Recipe Book" Pattern
**File:** [`3_6_challenge.py`](./exercises/3_6_challenge.py)

**The Leap:** Instead of writing disparate lines of code, we introduced a **"Transformation Recipe Book"**.
- We define *what* we want to do in a dictionary (the recipe).
- We pass it to a `batch_trans_block` (the chef) to execute it.
- **Why it matters:** It separates *logic* from *instruction*, making code cleaner and more scalable.

---

## 🚀 Mini-Project: Payroll & Analytics System
**File:** [`mini_project_block3.py`](./exercises/mini_project_block3.py)

> [!IMPORTANT]
> **Most Complex Project to Date**
> This project represents a shift towards **Production-Ready Code**. It doesn't just solve the problem; it builds a reusable framework to solve *future* problems.

### 🏗️ The Framework Architecture
We moved away from hardcoding transformations to using **Specific Helper Functions**:

1.  **`salarial_and_others_block` (The Heavy Lifter):**
    *   A universal function for conditional logic.
    *   Handles simple rules ("If X then Y") and complex math strings ("salary * 0.15").
    *   Includes error handling (`try/except`) to prevent crashes on bad data.

2.  **`concat_values` (The String Builder):**
    *   A template engine for text.
    *   Generates human-readable summaries like: *"Ana is Senior at IT with rating A"*.

### 📖 Code Storytelling
The code itself was refactored to "speak" to the developer.
*   **Narrative Comments:** Instead of explaining *what* code does (e.g., "split string"), we explain *why* (e.g., *"Breaking down the email for migration"*).
*   **Human Tone:** "Better performance = more money!", "Time to clean up!".

### 📊 Key Deliverables
*   **Professional Email Migration:** Transforming legacy domains to standard formats.
*   **Compensations Model:** Automated bracket assignment and bonus calculation.
*   **Talent Heatmap:** Identifying 'Stars', 'Flight Risks', and 'Future Leaders'.

---

## 📂 Datasets Used
- [employees.csv](./data/datasets/employees.csv): The core HR dataset enriched throughout the block.
