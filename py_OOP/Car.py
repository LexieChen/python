#!/usr/bin/python3

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

## main

car0 = Car("blue", "20,000")
car1 = Car("red", "30,000")

print (car0)
print (car1)
