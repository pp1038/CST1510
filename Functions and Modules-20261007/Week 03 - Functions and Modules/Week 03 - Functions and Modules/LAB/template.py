"""
RECORD CHECK  -  my version
===========================

Name  :  Priyesh Parekh
Lane  :  AI and Data Science      (delete two)
Date  :  11-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted
limit = 0.0     # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

difference = 0.0   # replace with your code
percent = 0.0       # replace with your code
status = ""          # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.

def status_of(percent):
    """Return status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the formatted report."""
    border = "=" * 29
    print(border)
    print(f"  RECORD CHECK  -  {label}")
    print(border)
    print(f"  {'Used':<10} : {value:>10.2f}")
    print(f"  {'Total':<10} : {limit:>10.2f}")
    print(f"  {'Free':<10} : {difference:>10.2f}")
    print(f"  {'Percent':<10} : {percent:>10.2f} %")
    print(f"  {'Status':<10} : {status:>10}")
    print(border)

over_limit_count = 0

while True:
    dataset_name = input("Enter dataset name (or 'quit' to stop): ").strip()
    if dataset_name.lower() == "quit":
        break

    rows_loaded = float(input("Enter rows loaded: "))
    rows_expected = float(input("Enter rows expected: "))

    difference, percent = check(rows_loaded, rows_expected)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(dataset_name, rows_loaded, rows_expected, difference, percent, status)
    print()

print(f"Total records OVER LIMIT: {over_limit_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
