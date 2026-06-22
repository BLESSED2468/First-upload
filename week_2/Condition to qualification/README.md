### **Task 3: The "Deep-Logic" Loan Qualifier**

Focus: Logical Operators (`and`, `or`, `not`) and Comparison.

The Scenario: You are building the backend for a FinTech app. A user only qualifies for a loan under specific, tricky conditions.

- The Input: Ask for `Age`, `Credit Score`, and `Monthly Income`.
- The Logic: A user is `is_qualified` **ONLY IF**:
  1. They are at least 21 years old.
  2. AND they have a credit score above 700.
  3. OR they have a credit score above 600 **AND** an income over $5,000.
  4. AND NOT if their income is less than $1,500 (regardless of score).
- The Goal: The interns must write this entire logic in **one single line** of code using parentheses and logical operators.
- Output: `Loan Qualification Status: True/False`.

# how to run
1. clone the repository

```bash
git clone <repository-url>

2. Navigate to the project directory:

```bash
cd project-folder
``

3. Run the script:

```bash
python task2_3.py