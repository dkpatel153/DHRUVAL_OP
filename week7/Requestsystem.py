"""
Description: This program create requestsystem
Author: Dhruval patel
"""
class RequestSystem:
    # Global unique ID counter
    id_counter = 1
    
    def __init__(self):
        self.requests = {}  # Stores requests with ID as the key
        self.total_requests = 0
        self.approved_requests = 0
        self.pending_requests = 0
        self.not_approved_requests = 0

    def user_info(self, name, age, email):
        """
        Collects basic user information and stores it.
        """
        self.user_name = name
        self.user_age = age
        self.user_email = email

    def request_details(self, items_with_costs):
        """
        Accepts a list of request items with their costs and calculates the total.
        """
        self.items = items_with_costs
        total_amount = sum(cost for item, cost in items_with_costs)
        return total_amount, items_with_costs

    def request_approval(self):
        """
        Determines if the request is approved based on the total amount.
        """
        total_amount, _ = self.request_details(self.items)
        if total_amount < 150:
            status = "approved"
        else:
            status = "pending"
        request_id = RequestSystem.id_counter
        RequestSystem.id_counter += 1
        self.requests[request_id] = {
            'name': self.user_name,
            'total': total_amount,
            'status': status
        }
        self.total_requests += 1
        if status == "approved":
            self.approved_requests += 1
        else:
            self.pending_requests += 1
        return request_id, status

    def respond_request(self, request_id, response):
        """
        Allows a manager to respond to a pending request.
        """
        if request_id not in self.requests:
            print("Request ID not found.")
            return
        
        request = self.requests[request_id]
        if request['status'] == "pending":
            if response == "Approved":
                request['status'] = "approved"
                self.approved_requests += 1
                self.pending_requests -= 1
            elif response == "Not Approved":
                request['status'] = "not approved"
                self.not_approved_requests += 1
                self.pending_requests -= 1
            else:
                print("Invalid response. Use 'Approved' or 'Not Approved'.")
        else:
            print("Request is not pending or has already been responded to.")

    def display_request(self):
        """
        Prints information for all request objects.
        """
        print("\nRequest Details:")
        for req_id, details in self.requests.items():
            print(f"Request ID: {req_id}")
            print(f"Name: {details['name']}")
            print(f"Total: ${details['total']:.2f}")
            print(f"Status: {details['status']}")
            print("-" * 30)

    def request_statistic(self):
        """
        Displays statistical information about the requisitions.
        """
        print("\nRequest Statistics:")
        print(f"Total number of requests submitted: {self.total_requests}")
        print(f"Total number of approved requests: {self.approved_requests}")
        print(f"Total number of pending requests: {self.pending_requests}")
        print(f"Total number of not approved requests: {self.not_approved_requests}")

def main():
    system = RequestSystem()

    while True:
        print("\nRequest Management System")
        print("1. Submit user information and request")
        print("2. Respond to a request")
        print("3. Display request details")
        print("4. Display request statistics")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            email = input("Enter your email: ")
            system.user_info(name, age, email)
            items = []
            while True:
                item_name = input("Enter request item name (or type 'done' to finish): ")
                if item_name.lower() == 'done':
                   break
                item_cost = float(input(f"Enter cost for '{item_name}': "))
                items.append((item_name, item_cost))
            system.request_details(items)
            request_id, status = system.request_approval()
            print(f"Request submitted with ID: {request_id}. Status: {status}")

        elif choice == '2':
            request_id = int(input("Enter request ID to respond to: "))
            response = input("Enter response (Approved/Not Approved): ")
            system.respond_request(request_id, response)

        elif choice == '3':
            system.display_request()

        elif choice == '4':
            system.request_statistic()

        elif choice == '5':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()





# class RequestSystem:
#     def __init__(self):
#         self.requests = []
#         self.request_id_counter = 1

#     def submit_request(self, name, age, email, items):
#         user_data = {"name": name, "age": age, "email": email}
#         total_amount = sum(item["cost"] for item in items)
#         status = "approved" if total_amount < 150 else "pending"
#         request_data = {
#             "id": self.request_id_counter,
#             "user_data": user_data,
#             "items": items,
#             "total_amount": total_amount,
#             "status": status
#         }
#         self.requests.append(request_data)
#         self.request_id_counter += 1

#     def display_request(self, request_id=None):
#         if request_id:
#             for request in self.requests:
#                 if request["id"] == request_id:
#                     print(f"Request ID: {request['id']}")
#                     print(f"Name: {request['user_data']['name']}")
#                     print(f"Total: ${request['total_amount']:.2f}")
#                     print(f"Status: {request['status']}")
#                     print("")
#                     return
#             print("Request not found")
#         else:
#             for request in self.requests:
#                 print(f"Request ID: {request['id']}")
#                 print(f"Name: {request['user_data']['name']}")
#                 print(f"Total: ${request['total_amount']:.2f}")
#                 print(f"Status: {request['status']}")
#                 print("")

#     def request_statistic(self):
#         total_requests = len(self.requests)
#         approved_requests = sum(1 for request in self.requests if request["status"] == "approved")
#         pending_requests = sum(1 for request in self.requests if request["status"] == "pending")
#         not_approved_requests = sum(1 for request in self.requests if request["status"] == "not approved")

#         print("Request Statistics:")
#         print(f"Total number of requests submitted: {total_requests}")
#         print(f"Total number of approved requests: {approved_requests}")
#         print(f"Total number of pending requests: {pending_requests}")
#         print(f"Total number of not approved requests: {not_approved_requests}")

# def main():
#     request_system = RequestSystem()

#     while True:
#         print("1. Submit a new request")
#         print("2. Display all requests")
#         print("3. Display a specific request")
#         print("4. Request statistics")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter your name: ")
#             age = int(input("Enter your age: "))
#             email = input("Enter your email: ")
#             num_items = int(input("Enter the number of items: "))
#             items = []
#             for i in range(num_items):
#                 item_name = input(f"Enter item {i+1} name: ")
#                 item_cost = float(input(f"Enter item {i+1} cost: "))
#                 items.append({"name": item_name, "cost": item_cost})
#             request_system.submit_request(name, age, email, items)
#         elif choice == "2":
#             request_system.display_request()
#         elif choice == "3":
#             request_id = int(input("Enter the request ID: "))
#             request_system.display_request(request_id)
#         elif choice == "4":
#             request_system.request_statistic()
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()