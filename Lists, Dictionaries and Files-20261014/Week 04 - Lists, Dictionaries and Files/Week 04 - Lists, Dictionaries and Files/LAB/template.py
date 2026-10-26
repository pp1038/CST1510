"""
RECORD CHECK  -  my version
===========================

Name  :  Priyesh Parekh
Lane  :  AI and data science      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def recorded(value, limit):
    diff = limit - value
    per = (value/limit)*100

    if value > limit:
        status = "overlimit"
    else:
        status = "ok"
        return diff, per, status

def report(label, value, limit, diff, per, status):
    print(f"\nLable:{label}")
    print(f"Value:{value}")
    print(f"Limit:{limit}")
    print(f"Difference:{diff}")
    print(f"Percentage:{per}")
    print(f"Status:{status}")

records = [{"label": "R-001", "value": 87, "limit": 100},
           {"label": "R-002", "value": 60, "limit": 120}]

over_limit_count = 0

for record in records:
    diff , per, status = recorded(record["value"], record["limit"])

    report(record["label"],
           record["value"],
           record["limit"],
           diff,
           per,
           status
           )
    if status == "overlimit":
        over_limit_count += 1

print(f"over limit count: {over_limit_count}")


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
