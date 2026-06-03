import pandas as pd
import os

curr_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(curr_dir, 'data.csv')
df = pd.read_csv(csv_file_path)

print(df.groupby("department").size())
print(df.groupby("department")["salary"].median())
print(df.groupby("department")["salary"].sum())
print(df.groupby(
    "department"
)["salary"].max())
print(df.groupby("department").count())

print(df.groupby(
    "department"
)["salary"].agg(
    ["mean", "min", "max"]
))

df["dept_avg_salary"] = (
    df.groupby(
        "department"
    )["salary"]
    .transform("mean")
)

print(df["dept_avg_salary"])

print(df.nlargest(
    3,
    "salary"
))

print(
    df.groupby("department")
      ["salary"]
      .size()
      .sort_values(
          ascending=False
      )
)