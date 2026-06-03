import pandas as pd
import os

curr_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(curr_dir, 'data.csv')
df = pd.read_csv(csv_file_path)

df["city"] = df["city"].fillna(
    "Unknown"
)
print(df["city"])

df["age"] = df["age"].fillna(
    df["age"].mean()
)
print(df["age"])


df["city"] = df["city"].fillna(
    "Unknown"
)

df["department"] = df["department"].fillna(
    "Not Assigned"
)

df["age"] = df["age"].fillna(
    df["age"].median()
)

df["salary"] = df["salary"].fillna(
    df["salary"].median()
)
print(df["salary"])