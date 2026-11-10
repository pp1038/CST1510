"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Clean one messy 'name,key=value,...' line into a dict with a lowercase name and float values."""
    name_part, rest = raw_line.strip().split(",", 1)

    record = {"name": name_part.strip().lower()}
    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        record[key.strip().lower()] = float(value.strip())
    return record


def status_of(record):
    """Return 'FLAGGED' if rating is below 3 or age is under 21, else 'OK'."""
    if record["rating"] < 3 or record["age"] < 21:
        return "FLAGGED"
    return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

# replace with your code
raw_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "SURVEY_2027,RATING=5,AGE=31",
    "  survey_2028 ,  Rating = 3 , Age=45",
    "Survey_2029 , rating=2 , age=19  ",
    "   SURVEY_2030,rating=4,   AGE = 52   ",
    "survey_2031 ,RATING=1 , age=27",
]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

# replace with your code
total = 0
flagged = 0

for raw in raw_records:
    try:
        record = parse_line(raw)
    except ValueError:
        print(f"Could not parse: {raw!r}")
        continue

    status = status_of(record)
    total += 1
    if status == "FLAGGED":
        flagged += 1
    print(record, "->", status)

print(f"Summary: {total} records parsed, {flagged} flagged.")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
