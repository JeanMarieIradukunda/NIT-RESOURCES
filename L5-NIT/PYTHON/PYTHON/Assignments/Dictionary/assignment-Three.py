# Employee Records System

# Create empty dictionary to store employees
# Structure:
# {
#    "EmployeeID": {
#        "name": "Employee Name",
#        "department": "Department Name",
#        "salary": amount
#    }
# }
employees = {}


# Function to add a new employee
def add_employee():
    # Ask for employee ID
    emp_id = input("Enter Employee ID: ")
    
    # Ask for employee details
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    
    # Use update() to add employee into dictionary
    employees.update({
        emp_id: {
            "name": name,
            "department": department,
            "salary": salary
        }
    })
    
    print("Employee added successfully!\n")


# Function to update employee salary
def update_salary():
    emp_id = input("Enter Employee ID to update salary: ")
    
    # Use get() to safely retrieve employee data
    employee = employees.get(emp_id)
    
    if employee:
        new_salary = float(input("Enter new salary: "))
        
        # Update salary inside nested dictionary
        employee.update({"salary": new_salary})
        
        print("Salary updated successfully!\n")
    else:
        print("Employee not found.\n")


# Function to search employee by ID
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    
    # Use get() to safely retrieve employee
    employee = employees.get(emp_id)
    
    if employee:
        print("Employee Found:")
        print("Name:", employee.get("name"))
        print("Department:", employee.get("department"))
        print("Salary:", employee.get("salary"))
    else:
        print("Employee not found.")
    
    print()


# Function to remove employee
def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    
    # Use pop() to safely remove employee
    removed = employees.pop(emp_id, None)
    
    if removed:
        print("Employee removed successfully!\n")
    else:
        print("Employee not found.\n")


# Function to display all employees
def display_all():
    print("All Employee Records:")
    
    # Use items() to iterate through dictionary
    for emp_id, details in employees.items():
        print("Employee ID:", emp_id)
        print("  Name:", details.get("name"))
        print("  Department:", details.get("department"))
        print("  Salary:", details.get("salary"))
        print("-" * 30)
    
    print()


# Main program loop (Menu-driven system)
while True:
    print("===== Employee Records System =====")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Display All Employees")
    print("6. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        update_salary()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        remove_employee()
    elif choice == "5":
        display_all()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")