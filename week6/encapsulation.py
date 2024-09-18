"""
Description: This program print name
Author: Dhruval patel
"""
class Person:
    def __init__(self):
        self.a = 'Sarthak'
        self._b = 'Divya'
    def PrintName(self):
        print(self.a)
        print(self._b)

p = Person()
p.a
p._b

p.PrintName()