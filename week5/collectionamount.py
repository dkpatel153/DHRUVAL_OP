
"""
Description: This program calculate total amount 
Author: Dhruval patel
"""
def calculate_total_amount():
    """
    Collects item prices and calculates the total amount.

    Returns:
    - tuple: Total amount of all items and a list of item details.
    """
    items = []
    total_amount = 0.0

    print("\nEnter Item Details (Type 'finish' to end):")
    while True:
        item_name = input("Item Name and Price (e.g., Cables $200): ").strip()
        if item_name.lower() == 'finish':
            break
        try:
            name, price = item_name.rsplit(' ', 1)
            price = float(price.replace('$', ''))
            items.append((name, price))
            total_amount += price
        except ValueError:
            print("Invalid input. Please enter item name and price separated by a space.")

    return total_amount, items


def categorize_request(total_amount):
    
    if total_amount < 1000:
        category = "Low"
        recommendation = "Approve"
    elif total_amount < 5000:
        category = "Medium"
        recommendation = "Review"
    else:
        category = "High"
        recommendation = "Escalate"

    return category, recommendation


def main():
    """
    Main function to categorize request and display recommendation.
    """
    total_amount, items = calculate_total_amount()
    category, recommendation = categorize_request(total_amount)

    # Display the results
    print("\nRequest Summary:")
    # print(f"Total amount: ${total_amount:.2f}")
    print("total amount",total_amount)
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")
    print("\nItem Details:")
    for item in items:
        print(f"{item[0]}: ${item[1]:.2f}")


if __name__ == "__main__":
    main()