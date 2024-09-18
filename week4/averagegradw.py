"""
Description: This program count average grade
Author: Dhruval patel
"""
def average_grade(records):
    total_grade = sum(record[2] for record in records)
    return total_grade / len(records)

students = (
    ('John', 20, 90),
    ('Jane', 21, 85),
    ('Jim', 19, 92)
)

def main():
    ave_grade = average_grade(students)
    print("Average grade:" ,ave_grade)
main()


  