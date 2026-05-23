class Cars:
    def __init__(self, model = "Unknown", year = 1970):
        self.model = model
        self.year = year

class Electric_Cars(Cars):
    def __init__(self, model = "Unknown", year = 1970, battery_size = 0):
        super().__init__(model, year)
        self.battery_size = battery_size
    
car1 = Cars("Toyota", 2020)
car2 = Electric_Cars("Tesla", 2021, 100)
print(car1.model)  # Output: Toyota
print(car1.year)   # Output: 2020
print(car2.model)  # Output: Tesla
print(car2.year)   # Output: 2021
print(car2.battery_size)  # Output: 100

    