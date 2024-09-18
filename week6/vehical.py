"""
Description: This program to car sttart,stoped and honk 
Author: Dhruval patel
"""
class Vehicle:
    def __init__(self) -> None:
          pass
    def start(self):
        print("vehicle started.")

    def stop(self):
              print("Vehicle stoped.")
class Car(Vehicle):
      def hork(self):
            print("Honk! Honk!")

my_car = Car()
my_car.start()
my_car.hork()
my_car.stop()

