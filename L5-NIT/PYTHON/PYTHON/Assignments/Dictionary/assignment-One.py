# Student Grade Management System

# Create an empty dictionary to store all students
# Structure:
# {
#   "StudentName": {
#       "class": "ClassName",
#       "modules": {
#           "Math": 80,
#           "Science": 75
#       }
#   }
# }
students = {}

# Function to add a new student
def add_student():
    # Ask user for student name
    name = input("Enter student name: ")
    
    # Ask user for class name
    class_name = input("Enter class: ")
    
    # Create empty dictionary to store modules and marks
    modules = {}
    
    # Ask how many modules the student has
    num_modules = int(input("How many modules? "))
    
    # Loop to enter each module and its mark
    for i in range(num_modules):
        module_name = input(f"Enter module {i+1} name: ")
        mark = float(input(f"Enter mark for {module_name}: "))
        
        # Store module and mark inside modules dictionary
        modules[module_name] = mark
    
    # Add student to main dictionary
    students[name] = {
        "class": class_name,
        "modules": modules
    }
    
    print("Student added successfully!\n")


# Function to display all students
def display_students():
    # Use keys() to display all student names
    print("All Students:")
    for name in students.keys():
        print(name)
    print()


# Function to calculate highest, lowest, and class average
def calculate_statistics():
    all_marks = []  # List to store all marks
    
    # Use values() to access student data
    for student_data in students.values():
        # Get modules dictionary
        modules = student_data.get("modules")
        
        # Use values() again to get marks
        for mark in modules.values():
            all_marks.append(mark)
    
    # Check if there are marks
    if len(all_marks) > 0:
        print("Highest Mark:", max(all_marks))
        print("Lowest Mark:", min(all_marks))
        print("Class Average:", sum(all_marks) / len(all_marks))
    else:
        print("No marks available.")
    print()


# Function to update a student's mark
def update_mark():
    name = input("Enter student name to update: ")
    
    # Use get() to safely check if student exists
    student = students.get(name)
    
    if student:
        module_name = input("Enter module name to update: ")
        
        # Check if module exists
        if module_name in student["modules"]:
            new_mark = float(input("Enter new mark: "))
            
            # Use update() to update module mark
            student["modules"].update({module_name: new_mark})
            
            print("Mark updated successfully!")
        else:
            print("Module not found.")
    else:
        print("Student not found.")
    print()


# Function to delete a student
def delete_student():
    name = input("Enter student name to delete: ")
    
    # Use pop() to remove student safely
    removed = students.pop(name, None)
    
    if removed:
        print("Student deleted successfully!")
    else:
        print("Student not found.")
    print()


# Main program loop
while True:
    print("===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Show Statistics")
    print("4. Update Student Mark")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Choose an option: ")
    
    # Call functions based on user choice
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_statistics()
    elif choice == "4":
        update_mark()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")