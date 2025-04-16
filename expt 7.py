'''
Mohd Qazim Ansari
Fe-D
241P105/36
'''

student_records = {}

def display_students():
    if not student_records:
        print("No student records available.")
    else:
        print("\n---- Student Records ----")
        for name, details in student_records.items():
            print(f"Name: {name}, Grade: {details['grade']}, Attendance: {details['attendance']}%\n")

def add_student():
    name = input("Enter student's name: ").strip().title()
    if name in student_records:
        print("Student already exists.")
    else:
        grade = input(f"Enter {name}'s grade: ").upper()
        attendance = float(input(f"Enter {name}'s attendance percentage: "))
        student_records[name] = {'grade': grade, 'attendance': attendance}
        print(f"{name} added successfully!")

def update_student():
    name = input("Enter student's name to update: ").strip().title()
    if name in student_records:
        grade = input(f"Enter {name}'s new grade (leave blank to keep unchanged): ").upper()
        attendance_input = input(f"Enter {name}'s new attendance percentage (leave blank to keep unchanged): ")

        if grade:
            student_records[name]['grade'] = grade
        if attendance_input:
            student_records[name]['attendance'] = float(attendance_input)

        print(f"{name}'s record updated successfully!")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student's name to remove: ").strip().title()
    if name in student_records:
        del student_records[name]
        print(f"{name} removed successfully!")
    else:
        print("Student not found.")

def student_menu():
    while True:
        print("\nStudent Record Management")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. Display Students")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

student_menu()

