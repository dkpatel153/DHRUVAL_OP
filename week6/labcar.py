"""
Description: This program car infomration
Author: Dhruval patel
"""
class Car:
    def __init__(self, color,model,year):
        self.color = color
        self.model = model
      

    def drive(self):
        print(f"The {self.color} {self.model}  is driving.")
    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

car1 = Car("Red", "Toyota", 2024)
car2 = Car("blue", "Honda", 2024)

car1.drive()
car1.stop()

car2.drive()
car2.stop()
