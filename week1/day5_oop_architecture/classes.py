class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("John", "Doe", 60000)

print(emp_1.email)
print(emp_2.email)

emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "corey.schafer@company.com"
emp_1.pay = 50000
