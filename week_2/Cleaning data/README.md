## Log Data Sanitization & Analysis

The Scenario: Our server generates raw logs that are often "dirty" with irregular spacing. You must extract key security information and perform a quick time-based calculation.

Input Data:

Copy this exact string into your script:

```
raw_log = "  2026-05-04 |  user_jdoe  |  LOGIN_SUCCESS  | IP:192.168.1.1 "
```

Requirements:

1. **String Cleaning:** Remove the leading/trailing whitespace and split the data into individual components (Date, Username, Status, IP).

2. Data Transformation:

   - The **Username** must be converted to all uppercase (e.g., `JDOE`).
   - The **IP Address** must be extracted without the "IP:" prefix.

3. Date Logic:

   - Convert the date string into a Python `date` object.
   - Calculate how many days are left in the year 2026 starting from the log date.

4. Output: Use an **f-string** to print a single-line summary:

   `[SECURITY ALERT]: User <USER> accessed from <IP> on <DD/MM/YYYY>. Days remaining in year: <DAYS>.`

------
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
python strip.py