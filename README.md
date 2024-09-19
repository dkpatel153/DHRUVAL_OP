class LeaveRequest:
    def __init__(self, request_id, employee_info, leave_type, start_date, end_date, reason):
        self.request_id = request_id
        self.employee_info = employee_info
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = "pending"  # default status

    def approve(self):
        self.status = "approved"

    def reject(self):
        self.status = "not approved"

class LeaveRequestManager:
    def __init__(self):
        self.requests = {}
        self.id_counter = 1

    def create_request(self, employee_info, leave_type, start_date, end_date, reason):
        new_request = LeaveRequest(self.id_counter, employee_info, leave_type, start_date, end_date, reason)
        self.requests[self.id_counter] = new_request
        self.id_counter += 1
        return new_request

    def respond_to_request(self, request_id, decision):
        if request_id in self.requests:
            if decision.lower() == "approve":
                self.requests[request_id].approve()
            elif decision.lower() == "reject":
                self.requests[request_id].reject()
            else:
                return "Invalid decision. Use 'approve' or 'reject'."
            return f"Request ID {request_id} has been {self.requests[request_id].status}."
        return "Request ID not found."

    def display_requests(self):
        for request in self.requests.values():
            print(f"Request ID: {request.request_id}, Employee: {request.employee_info}, Leave Type: {request.leave_type}, "
                  f"Dates: {request.start_date} to {request.end_date}, Reason: {request.reason}, Status: {request.status}")

    def display_statistics(self):
        approved = sum(1 for req in self.requests.values() if req.status == "approved")
        pending = sum(1 for req in self.requests.values() if req.status == "pending")
        not_approved = sum(1 for req in self.requests.values() if req.status == "not approved")
        total = len(self.requests)

        print(f"Total requests: {total}, Approved: {approved}, Pending: {pending}, Not Approved: {not_approved}")

def main():
    manager = LeaveRequestManager()

    while True:
        print("\nLeave Request Management System")
        print("1. Submit leave request")
        print("2. Respond to a leave request")
        print("3. Display leave requests")
        print("4. Display statistics")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            employee_info = {'name': name, 'email': email}
            leave_type = input("Enter leave type (Sick, Vacation, Personal): ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            reason = input("Enter reason for leave: ")
            request = manager.create_request(employee_info, leave_type, start_date, end_date, reason)
            print(f"Leave request submitted with ID: {request.request_id}. Status: {request.status}")

        elif choice == '2':
            request_id = int(input("Enter request ID: "))
            response = input("Enter response (approve/reject): ")
            print(manager.respond_to_request(request_id, response))

        elif choice == '3':
            manager.display_requests()

        elif choice == '4':
            manager.display_statistics()

        elif choice == '5':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()



The code shows a simple form of the Leave Request Management System. The objective is to refactor this code with the intent of making it more maintainable, scalable, and readable through the principles of SOLID.

Single Responsibility Principle - SRP

The LeaveRequest class does a bit of everything; it stores the information about the request and handles its status. Currently, the LeaveRequestManager class has the responsibility of creating requests, responding to a request, viewing requests, and analyzing statistics. We will do some refactorings to split these responsibilities into different classes, with each class having one single main responsibility.

Open/Closed Principle (OCP)

Changes should not be done in the LeaveRequestManager class, but it can be extended with extra functionality. This shall be achieved by applying inheritance and polymorphism.

Liskov Substitution Principle - LSP

Yet, the subclasses can't replace the LeaveRequest class. One should be able to make sure that the subclasses can replace their parent class.

Interface Segregation Principle (ISP)

 
The LeaveRequestManager class has a fat, general-purpose interface. We would like to split it into leaner, client-specific interfaces.

Dependency Inversion Principle (DIP) 

The LeaveRequestManager class is tightly coupled to the LeaveRequest class. We will loosen this relationship by introducing an abstraction.
