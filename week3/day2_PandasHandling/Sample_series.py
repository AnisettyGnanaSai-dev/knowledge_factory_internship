import pandas as pd

students = pd.Series(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], index=['A', 'B', 'C', 'D', 'E'])

print(students)
print(students['A'])
print(students.index.is_unique)

customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
})
print(customers)

employees = pd.DataFrame({
    "Name": ["Sai", "Ravi", "Kiran"],
    "Salary": [40000, 50000, 60000]
})

employees["Salary"] = employees["Salary"] * 1.15# Increase salary by 15%

print(employees)

s1 = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)

s2 = pd.Series(
    [10, 20, 30],
    index=["B", "C", "D"]
)

print(s1 + s2)
#pandas align by index not by position, so the result will have NaN for index 'A' and 'D' because they don't have corresponding values in both series.

print(type(customers["Age"]))
print(type(customers[["Age"]]))

data = [
    [
        'Sai', 40000
    ],
    [
        'Ravi', 50000
    ],
    [
        'Kiran', 60000
    ]
]

df = pd.DataFrame(data, columns=['name', 'salary'])
print(df)
