import pandas as pd

employees = pd.DataFrame({
    "employee_id": [1, 2, 3],
    "Name": ["Sai", "Ravi", "Kiran"],
    })

departments = pd.DataFrame({
    "employee_id": [1, 2, 4],
    "Department": ["HR", "Finance", "IT"]
})

merged = pd.merge(
    employees,
    departments,
    on="employee_id",
    how="inner"
)
print(merged)

merged = pd.merge(
    employees,
    departments,
    on="employee_id",
    how="left"
)
print(merged)

merged = pd.merge(
    employees,
    departments,
    on="employee_id",
    how="right"
)
print(merged)

merged = pd.merge(
    employees,
    departments,
    on="employee_id",
    how="outer"
)   
print(merged)