"""
Description: This program using a while loop to print a line
Author: Dhruval patel
"""

def print_lines():
    count = 0
    while count < 100:
        print(f"{count} - I like kali linux...")
        count = count + 1

def main():
    print_lines()
main()