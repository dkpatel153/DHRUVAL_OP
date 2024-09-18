"""
Description: This program count age and formatted pi value
Author: Dhruval patel
"""

name = input("Enter your name:")
age = input("Enter your age:")
print("Hello,",name,"You are",age,"years old",sep = "")
# fstring
print(f"hello,{name}. you are {age} years old.")

pi = 3.141592653589
print(pi)
formatted_pi = f"Valuem of pi to 2 decimal places: {pi: .2f}"
print(formatted_pi)

salary = float(input("Enter your Salary"))
print(f"you weekly salary is ${salary: .2f}")
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello,",name,"You are",age,"years old",sep = "")
# fstring
print(f"hello,{name}. you are {age} years old.")



pi = 3.141592653589
print(pi)
formatted_pi = f"Valuem of pi to 2 decimal places: {pi: .2f}"
print(formatted_pi)

salary = float(input("Enter your Salary"))
print(f"you weekly salary is ${salary: .2f}")