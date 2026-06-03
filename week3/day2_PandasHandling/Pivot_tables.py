import pandas as pd 
import os

curr_dir = os.path.dirname(__file__)
csv_path = os.path.join(curr_dir, 'data.csv')

df = pd.read_csv(csv_path)


df["city"] = df["city"].fillna("Unknown")
df["department"] = df["department"].fillna("Not Assigned")
df["salary"] = df["salary"].fillna(
    df["salary"].median()
)

report = pd.pivot_table(

    data=df,                    # Dataset

    index="department",         # Rows

    columns="city",             # Columns

    values="salary",            # Values to aggregate

    aggfunc=["mean", "max"],    # Multiple aggregations

    fill_value=0,               # Replace NaN

    margins=True,               # Grand totals

    margins_name="Total"        # Rename grand total row

)

print(report)