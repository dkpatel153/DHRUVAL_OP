"""
Description: This program enter user numbers
Author: Dhruval patel
"""

def total_user_unmbers():
    total = 0
    number = int(input("Enter a number (0 to end):"))
    while number != 0:
        total += number
        number = int(input("Enter a number ( 0 to end):"))
    print("Total:", total)

def main():
    total_user_unmbers()

main()
