import os 
import pandas as pd

# Read CSV file
current_dir = os.path.dirname(__file__)

cs_file_path = os.path.join(current_dir, 'students.csv')


df = pd.read_csv(cs_file_path)
print(df)
print(df.columns)
print(df.shape)

df = pd.read_csv(
    cs_file_path,
    usecols=["balance"]
)

print(df)

df = pd.read_csv(
    cs_file_path,
    skiprows=2
)
print(df)

df = pd.read_csv(
    cs_file_path,
    nrows=2
)
print(df)

df = pd.read_csv(
    cs_file_path,
    dtype={
        "customer_id": str
    }
)
print(df.dtypes)
print(df.info())

cs_file_path = os.path.join(current_dir, 'data.csv')

df = pd.read_csv(cs_file_path)

print(df.head())

print(df.shape)

print(df.columns)

print(df.dtypes)


print(df.info())

print(df.describe())

print(df.isnull().sum())

df.loc[:, "name"]
print(df["name"])

print(df.loc[
    df["salary"] > 50000
])  

print(df.loc[
    df["department"] == "IT"
])

print(df.loc[
    (df["salary"] > 50000)
    &
    (df["department"] == "HR")
])

print(df.loc[
    df["city"].isin(
        ["Vizag", "Hyderabad"]
    )
])

print(df.query(
    "salary > 50000 and department == 'HR'"
))

df.loc[
    df["city"].isna(),
    "city"
] = "Unknown"


print(df.loc[
    df["department"] == "Finance"
].sort_values(
    by="salary",
    ascending=False
))