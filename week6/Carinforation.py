"""
Description: This program create class to get car information
Author: Dhruval patel
"""
class Car:
    def __init__(self, color,model,year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.color} {self.model}  is driving in {self.year}.")
    def stop(self):
        print(f"The {self.color} {self.model} has stopped in {self.year}.")

car1 = Car("Red", "Toyota", 2024)
car2 = Car("blue", "Honda", 2024)

car1.drive()
car1.stop()

car2.drive()
car2.stop()
