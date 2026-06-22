## **Task 2: Workday & Budget Calculator**

**File Name:** `task2_project.py`

**The Scenario:** A Project Manager needs a tool to estimate the end date of a task based on work hours, avoiding weekends.

**Requirements:**

1. **User Inputs:**
   - Project Start Date (Format: `YYYY-MM-DD`).
   - Total Estimated Work Hours (Integer).
   - Hourly Rate (Float).
2. **Calculation:**
   - Calculate the total cost of the project (Hours × Rate).
   - Calculate the number of **workdays** needed (assume exactly 8 hours of work per day).
3. **The Deadline Logic:**
   - Add the number of workdays to the start date to find the "Project Completion Date."
   - **The Brain-Tasker:** If the calculated completion date falls on a **Saturday** or **Sunday**, your script must automatically increment the date to the **following Monday**.
4. **Output:**
   - Display the total cost formatted to 2 decimal places with a currency symbol.
   - Display the final completion date in a readable format (e.g., `Monday, May 18, 2026`).

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
python task_2.py