"""
program of user information
Author: Dhruval patel
"""
def user_information():
    print("Enter User Information:")
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    email = input("Email Address: ").strip()

    unique_id = id_counter + 1
    id_counter = unique_id

    print(f"\nUser Information")
    print(f"ID: {unique_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
