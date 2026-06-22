### Task 1: The "Clean-Room" Data Entry Engine**

Focus: Casting, Strings, and Membership Operators.

The Scenario: A client sent a CSV-style string where prices are messy. You must clean the data and validate if it belongs to a "Premium" category.

- The Input: Ask the user to input a product record in this format: `Laptop : $1,200.50` (Note the spaces and symbols).
- The Logic:
  1. Use string methods to remove the `$` and `,`.
  2. Cast the cleaned price to a **float** and the product name to **lowercase**.
  3. Define a list (or string) of "luxury_keywords" like `"laptop, smartphone, camera"`.
- 
The Operators: Use a **Membership Operator** (`in`) to check if the input product is in your luxury list and a **Comparison Operator** to check if the price is `> 1000`.
- **Output:** Return a Boolean value (`True/False`) stating if the item is a "High-Value Electronic."

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
python Task.py