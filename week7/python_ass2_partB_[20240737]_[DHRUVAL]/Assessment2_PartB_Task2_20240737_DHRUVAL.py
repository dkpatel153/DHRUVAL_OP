"""
Description: This program create Requisitionsystem to staff information
Author: Dhruval patel
"""
class RequisitionSystem():
    id_counter = 0

    def __init__(self):
        self.requests = {}  
        self.total_requisition = 0
        self.approved_requisition = 0
        self.pending_requisition = 0
        self.not_approved_requisitions = 0
        self.staff_name = ""
        self.staff_id = ""
        self.date = ""

    def staff_information(self):                      # Prompt staff member for input
        print("Printing Staff Information: ")
        self.staff_name = input("Staff Name: ").strip()                      # Remove the space from strip() function
        self.staff_id = input("Staff ID: ").strip()
        self.date = input("Date: ").strip()  

        unique_id = RequisitionSystem.id_counter
        RequisitionSystem.id_counter += 1

        Rstaff_id = self.staff_id + str(unique_id)[-3:]
        R_Number = Rstaff_id
        approval_ref_number = f"APR-{Rstaff_id}"
        return R_Number, approval_ref_number

    def requisitions_details(self, items_with_costs):
        """
        Accepts a list of request items with their costs and calculates the total.
        """
        total_amount = sum(cost for item, cost in items_with_costs)
        return total_amount, items_with_costs

    def requisition_approval(self, items_with_costs):
        """
        Determines if the request is approved based on the requisitions_details method.
        """
        total_amount, _ = self.requisitions_details(items_with_costs)
        if total_amount < 500:
            status = "approved"
        else:
            status = "pending"
        requisition_id, approval_ref_number = self.staff_information()
        self.requests[requisition_id] = {
            'name': self.staff_name,
            'total': total_amount,
            'status': status,
            'approval_ref_number': approval_ref_number
        }
        self.total_requisition += 1
        if status == "approved":
            self.approved_requisition += 1
        else:
            self.pending_requisition += 1
        return requisition_id, status, approval_ref_number

    def respond_requisition(self, requisition_id, response):
        if requisition_id not in self.requests:
            print("Requisition ID not found.")
            return
        
        request = self.requests[requisition_id]
        if request['status'] == "pending":
            if response == "Approved":
                request['status'] = "approved"
                self.approved_requisition += 1
                self.pending_requisition -= 1
            elif response == "Not Approved":
                request['status'] = "not approved"
                self.not_approved_requisitions += 1
                self.pending_requisition -= 1
            else:
                print("Invalid response. Use 'Approved' or 'Not Approved'.")
        else:
            print("Request is not pending or has already been responded to.")

    def display_requisition(self):
        """
        Prints information for all request objects.
        """
        print("\nRequest Details:")
        for req_id, details in self.requests.items():
            print(f"Request ID: {req_id}")
            print(f"Name: {details['name']}")
            print(f"Total: ${details['total']:.2f}")
            print(f"Status: {details['status']}")
            print(f"Approval Reference Number: {details['approval_ref_number']}")
            print("-" * 30)

    def request_statistic(self):
        """
        Displays statistical information about the requisitions.
        """
        print("\nRequisitions Statistics:")
        print(f"Total number of requisitions submitted: {self.total_requisition}")
        print(f"Total number of approved requisitions: {self.approved_requisition}")
        print(f"Total number of pending requisitions: {self.pending_requisition}")
        print(f"Total number of not approved requisitions: {self.not_approved_requisitions}")

def main():
    requisition_system = RequisitionSystem()

    while True:
        print("\nRequisition Management System")
        print("1. Submit staff information and requisitions")
        print("2. Respond to a requisitions")
        print("3. Display requisitions details")
        print("4. Display requisitions statistics")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            items = []
            requisition_id, approval_ref_number = requisition_system.staff_information()
            while True:
                item_name = input("Enter request item name (or type 'done' to finish): ")
                if item_name.lower() == 'done':
                   break
                item_cost = float(input(f"Enter cost for '{item_name}': "))
                items.append((item_name, item_cost))
            request_id, status, approval_ref_number = requisition_system.requisition_approval(items)
            print(f"Request submitted with ID: {request_id}. Status: {status}. Approval Reference Number: {approval_ref_number}")

        elif choice == '2':
            request_id = int(input("Enter request ID to respond to: "))
            response = input("Enter response (Approved/Not Approved): ")
            requisition_system.respond_requisition(request_id, response)

        elif choice == '3':
            requisition_system.display_requisition()

        elif choice == '4':
            requisition_system.request_statistic()

        elif choice == '5':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
