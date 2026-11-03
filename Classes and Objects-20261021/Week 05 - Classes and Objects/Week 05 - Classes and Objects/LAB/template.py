"""
RECORD CHECK  -  my version
===========================

Name  :  Priyesh Parekh
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    """A single reading with a label, a value and a limit it is checked against."""

    over_limit_count = 0  # class-level running total shared by every Record

    def __init__(self, label, value, limit):
        """Store the label, value and limit, and count this record if it is over limit."""
        self.label = label
        self.value = value
        self.limit = limit
        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def status(self):
        """Return "OVER LIMIT" at 100%+ of the limit, "WARNING" at 90%+, otherwise "OK"."""
        if self.value >= self.limit:
            return "OVER LIMIT"
        if self.value * 10 >= self.limit * 9:   # same as value >= 90% of limit
            return "WARNING"
        return "OK"

        
# ==================================================================== RECORDS
# 2. Create your records.

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path, "r") as f:
        for line in f:
            if not line.strip():                # skip blank lines
                continue
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records(r"C:\Users\pbpar\CST1510\Classes and Objects-20261021\Week 05 - Classes and Objects\Week 05 - Classes and Objects\LAB\records_sample.txt")

# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")
    print("=" * 34)

print()
print(f"Records over Limit: {Record.over_limit_count} of {len(records)}")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
