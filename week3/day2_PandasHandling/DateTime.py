import pandas as pd
import os

curr_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(curr_dir, 'data.csv')
df = pd.read_csv(csv_file_path)
df["joining_date"] = (
    df["joining_date"]
    .fillna("2024-01-01")
)
df["joining_date"] = (
    pd.to_datetime(
        df["joining_date"],
        dayfirst=True,
        errors="coerce"
    )
)

print(df["joining_date"])

df["year"] = (
    df["joining_date"].dt.year
)

df["month"] = (
    df["joining_date"].dt.month_name()
)
print(df["year"])
print(df["month"])

today = pd.Timestamp.now()
print(today - df["joining_date"])