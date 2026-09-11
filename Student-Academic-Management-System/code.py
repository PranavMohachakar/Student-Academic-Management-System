# Student Record and Academic Management System
# Unit 1 Project

students = []


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to add student
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    python_marks = float(input("Enter Python marks: "))
    maths_marks = float(input("Enter Maths marks: "))
    chemistry_marks = float(input("Enter Chemistry marks: "))

    attendance = float(input("Enter attendance percentage: "))

    average = (python_marks + maths_marks + chemistry_marks) / 3
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "department": department,
        "semester": semester,
        "python": python_marks,
        "maths": maths_marks,
        "chemistry": chemistry_marks,
        "attendance": attendance,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("\nStudent record added successfully!")


# Function to display students
def display_students():
    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("\n------------------------------")
        print("Name       :", student["name"])
        print("Roll No.   :", student["roll"])
        print("Department :", student["department"])
        print("Semester   :", student["semester"])
        print("Python     :", student["python"])
        print("Maths      :", student["maths"])
        print("Chemistry  :", student["chemistry"])
        print("Attendance :", student["attendance"], "%")
        print("Average    :", round(student["average"], 2))
        print("Grade      :", student["grade"])


# Function to search student
def search_student():
    print("\n--- Search Student ---")

    roll = input("Enter roll number to search: ")

    for student in students:

        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("Roll No.   :", student["roll"])
            print("Department :", student["department"])
            print("Semester   :", student["semester"])
            print("Average    :", round(student["average"], 2))
            print("Grade      :", student["grade"])
            print("Attendance :", student["attendance"], "%")
            return

    print("Student not found.")


# Function to display average marks
def display_average():
    print("\n--- Average Marks ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:
            print("Student Name :", student["name"])
            print("Average Marks:", round(student["average"], 2))
            return

    print("Student not found.")


# Function to display grade
def display_grade():
    print("\n--- Student Grade ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:
            print("Student Name :", student["name"])
            print("Grade        :", student["grade"])
            return

    print("Student not found.")


# Main menu
while True:

    print("\n====================================")
    print(" STUDENT ACADEMIC MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Add Student")
    print("2. Display Student Records")
    print("3. Search Student")
    print("4. Calculate / Display Average")
    print("5. Display Grade")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_average()

    elif choice == "5":
        display_grade()

    elif choice == "6":
        print("\nThank you!")
        print("Program closed successfully.")
        break

    else:
        print("Invalid choice. Please enter 1 to 6.")