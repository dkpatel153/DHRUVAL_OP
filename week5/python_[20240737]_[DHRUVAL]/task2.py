"""
Description: call the taks 1 and ask to input item
Author: DHRUVAL PATEL
"""

def requisitions_total():

    items = []
    total_amount = 0.0
    while True:
        item_name = input("Enter Item Name and Price (Type 'finish' to end): ").strip()
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



def main():
    """
    Main function to requisitions total and display result.
    """
    total_amount, items = requisitions_total()
    

    # Display the results
    print("\nOutput:")
    print(f"Total amount: ${total_amount:.2f}")     
    

if __name__ == "__main__":
    main()




