"""
program wich calculate Grocerie bill
Author = Dhruval patel
"""
item1=10
item2=20
item3=30

item1=float(input("Enter the price for item1:-"))
item2=float(input("Enter the price for item2:-"))
item3=float(input("Enter the price for item3:-"))
sub_total = item1 + item2 + item3
sales_tax= sub_total* 0.15
calculate_total= sub_total + sales_tax

print("calculatestotal",calculate_total)
