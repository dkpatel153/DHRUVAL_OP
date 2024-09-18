"""
Description: collect staff member submitting information a requisition
Author: DHRUVAL PATEL
"""
def collect_staff_information(id_requisition):                      # Prompt staff member for input
    print("Printing Staff Information: ")
    staff_name = input("Staff Name: ").strip()                      # Remove the space from strip() function
    staff_id = input("Staff ID: ").strip()
    date = input("Date: ").strip()  

    uniqe_id = id_requisition + 1
    id_requisition = uniqe_id

    
    print(f"\nPrinting Staff Information:")
    print(f"Staff Name: {staff_name}")
    print(f"Staff_id: {staff_id}" )
    print(f"Date: {date}")
    print(f"Requisition ID: {id_requisition}")
    
    return id_requisition, uniqe_id, staff_name, staff_id, date

def main():
    id_requisition = 10000
    id_requisition, uniqe_id, staff_name, staff_id, date = collect_staff_information(id_requisition)
main()
