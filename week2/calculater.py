
"""
program which calculate the area of circle
Author = Dhruval patel
"""

num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
calculate = input("Enter the sum:")
if calculate == "+":
    print(num1+num2)
elif calculate == "-":
    print(num1-num2)
elif calculate == "*":
    print(num1*num2)
elif calculate == "/":
    print(num1/num2)
elif calculate == "//":
    print(num1//num2)
elif calculate == "%":
    print(num1%num2)
else:
    print("invalid sum")

