"""
RECORD CHECK  -  my version
===========================

Name  :  Priyesh
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("C:\\Users\\pbpar\\CST1510\\Pandas-20261104\\Week 06 - Pandas\\Week 06 - Pandas\\LAB\\Priyesh.csv")   # replace with pd.read_csv("your_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda x: "overlimit" if x > 100 else ("warning" if x >= 90 else "ok")
    )


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.


result = df[df["status"] != "OK"]
print(result)

import matplotlib.pyplot as plt

# Count per status
counts = df.groupby("status").size()
print(counts)

# Save the full DataFrame
df.to_csv("results.csv", index=False)

# Bar chart of counts per status
counts.plot(kind="bar", color=["tab:green", "tab:red", "tab:orange"])
plt.title("Count per status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("status_counts.png")
plt.close()
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
