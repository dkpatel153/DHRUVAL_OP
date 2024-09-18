"""
Program: Check the given conditions
Author: Dhruval patel
"""

def main():
    a = 42
    b = 17
    c = 94
    if a > b and a > c:
        print("You")
    if not (a > b and a > c):
        print("cannot")
    if a > b or a > c:
        print("tuna")
    if not (a > b or a > c):
        print("fish")
main()
    
