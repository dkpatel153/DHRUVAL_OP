"""
Description: This program display the adds and offer price
Author: Dhruval patel
"""

def display_intro():
    message = "Welcome to Deltin Jack Man's showroom"
    print(message)

def display_shop_details(combo, price):
    message = "*** " + combo.upper() + " ($" + str(price) + ") ***"
    print(message)


display_intro() 
display_shop_details("Combo A", 29.99)  

