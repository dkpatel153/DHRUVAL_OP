"""
Description: This program create class perspon
Author: Dhruval patel
"""

class Perspon():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Perspon("sarthak", 20)
person2 = Perspon("divya", 19)

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)