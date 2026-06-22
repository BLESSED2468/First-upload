## **Task 3: Automated Office Service Receipt**

File Name: `task3_receipt.py`

The Scenario: You are building a CLI tool for the front desk to bill clients for refreshments and parking.

Requirements:

1. User Inputs:
   - Number of guests (e.g., `6`).
   - Cost per refreshment (e.g., `12.50`).
   - Arrival Time and Departure Time (Use 24-hour format: `HH:MM`).
2. The Logic:
   - Refreshment Subtotal: `Guests * Price`.
   - Bulk Discount: If guests > 5, apply a 10% discount to the refreshment subtotal.
   - Parking Fee: Parking costs **₦5.00 per hour**. You must charge for a full hour even if they stay for a fraction of an hour (e.g., 1 hour and 10 minutes = 2 hours charged).
3. The Brain-Tasker (Formatting):
   - Generate a "Receipt" in the terminal.
   - You must use **string alignment** (`<`, `>`, or `^`) to ensure that all prices align vertically, regardless of the length of the label.
   - Apply a final 7.5% Service Tax to the grand total.

**Example Output Style:**

Plaintext

```
===============================
       OFFICE RECEIPT
===============================
Refreshments:          ₦  67.50
Parking Fee:           ₦  10.00
Tax (7.5%):            ₦   5.81
-------------------------------
TOTAL DUE:             ₦  83.31
===============================
```

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
python task_3.py