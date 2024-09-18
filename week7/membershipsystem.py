"""
Description: This program create for membership registeration system
Author: Dhruval patel
"""


class MembershipSystem:
    def __init__(self):
        self.members = {}  # {membership_id: (student_id, last_name, programme)}
        self.next_membership_id = 1
        self.registered_count = 0
        self.withdrawn_count = 0
        self.programme_counts = {'Diploma': 0, 'Bachelor': 0}

    def register_member(self, student_id, last_name, programme):
        if programme not in ['Diploma', 'Bachelor']:
            raise ValueError("Invalid programme. Must be 'Diploma' or 'Bachelor'.")
        membership_id = self.next_membership_id
        self.members[membership_id] = (student_id, last_name, programme)
        self.next_membership_id += 1
        self.registered_count += 1
        self.programme_counts[programme] += 1
        print(f"Registration successful. Membership ID: {membership_id}")

    def withdraw_member(self, membership_id, last_name):
        if membership_id not in self.members:
            print("Invalid Membership ID.")
            return
        student_id, stored_last_name, programme = self.members[membership_id]
        if last_name != stored_last_name:
            print("Last name does not match.")
            return
        del self.members[membership_id]
        self.registered_count -= 1
        self.withdrawn_count += 1
        self.programme_counts[programme] -= 1
        print("Membership withdrawn successfully.")

    def display_statistics(self):
        print("\nMembership Statistics:")
        print(f"Number of registered members: {self.registered_count}")
        print(f"Number of students in Diploma programme: {self.programme_counts['Diploma']}")
        print(f"Number of students in Bachelor of IT programme: {self.programme_counts['Bachelor']}")
        print(f"Number of students who have withdrawn their membership: {self.withdrawn_count}")

def main():
    system = MembershipSystem()

    while True:
        print("\nWhitecliffe Students’ Club Membership System")
        print("1. Register new member")
        print("2. Withdraw membership")
        print("3. Display statistics")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            last_name = input("Enter Student Last Name: ")
            programme = input("Enter Student Programme (Diploma or Bachelor): ")
            system.register_member(student_id, last_name, programme)
        elif choice == '2':
            membership_id = int(input("Enter Membership ID: "))
            last_name = input("Enter Student Last Name: ")
            system.withdraw_member(membership_id, last_name)
        elif choice == '3':
            system.display_statistics()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()