"""
Description: This program to collect user data to generat ID
Author: Dhruval patel
"""

def collect_user_data(id_counter):
    """
    Collects user information and generates a unique ID.

    Args:
        id_counter (int): Current ID counter value

    Returns:
        tuple: Updated ID counter, generated ID, user data
    """
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    user_email = input("Enter your email: ")

    id_counter += 1
    user_id = id_counter

    user_data = {
        "name": user_name,
        "age": user_age,
        "email": user_email,
        "id": user_id
    }

    print("User Information:")
    print("----------------")
    print(f"Name: {user_name}")
    print(f"Age: {user_age}")
    print(f"Email: {user_email}")
    print(f"ID: {user_id}")
    print("----------------")
    
    return id_counter, user_id, user_data
