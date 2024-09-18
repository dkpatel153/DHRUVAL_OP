
def fun(num1,num2,num3):
    sum = num1 + num2 + num3
    minimum = min(num1,num2,num3)
    return sum - minimum

num1 = int(input("Enter the num1:"))
num2 = int(input("Enter the num2:"))
num3 = int(input("Enter the num3:"))
print(fun(num1,num2,num3))
