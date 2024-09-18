
def display_BMI(weight , height):
    BMI = weight / (height/100)**2
    return BMI

weight = float(input("Enter weight:"))
height = float(input("Enter height:"))
print(display_BMI(weight , height))


