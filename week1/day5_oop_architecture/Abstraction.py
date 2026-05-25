from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car is starting"
    
class Bike(Vehicle):
    def start(self):
        return "Bike is starting"
    
car = Car()
bike = Bike()
print(car.start())  # Output: Car is starting
print(bike.start()) # Output: Bike is starting