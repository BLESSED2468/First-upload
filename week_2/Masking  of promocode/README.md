### **Task 4: The Membership "Promo Code" Masker**

Focus: Strings, Booleans, and Comparison Operators.

The Scenario: A user enters a promo code. We need to check if it's valid and hide part of it for security.

- **The Input:** A promo code (e.g., `SAVE2026-XYZ`).
- **The Logic:**
  1. Check if the code starts with `"SAVE"` (Boolean).
  2. Check if the total length is exactly 12 characters.
  3. **The Operators:** Use a **Logical Operator** to ensure both conditions are met.
- **The String Mask:** If valid, show the first 4 characters, then four `*`, then the last 2 characters (e.g., `SAVE****YZ`).
- **Output:** Display the masked code and a Boolean `is_valid` status.

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
python task_4.py