import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\pbpar\\CST1510\\Pandas-20261104\\Week 06 - Pandas\\Week 06 - Pandas\\survey_results.csv")
print(df.head())
print(df.dtypes)
print(len(df))

pct_unanswered = len(df[df["answered"] == 0]) / len(df) * 100
print(f"Unanswered: {pct_unanswered:.1f}%")

clean = df[df["answered"] == 1].copy()

avg_by_cat = clean.groupby("category")["score"].mean()
print(avg_by_cat)

ranked = avg_by_cat.sort_values(ascending=False)
print(ranked)
print("Strongest category:", ranked.index[0])

clean["result"] = clean["score"].apply(lambda s: "Pass" if s >= 60 else "Fail")

clean["result"].value_counts().plot(kind="bar")
plt.title("Pass/Fail counts")
plt.xlabel("Result")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("pass_fail_counts.png")
plt.close()

clean.to_csv("survey_results_clean.csv", index=False)