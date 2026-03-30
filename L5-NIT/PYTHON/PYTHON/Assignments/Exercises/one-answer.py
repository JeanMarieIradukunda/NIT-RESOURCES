# Function to calculate total marks
def calculate_total(mark1, mark2, mark3):
    return mark1 + mark2 + mark3

# Ask how many students
num_students = int(input("Enter the number of students: "))

# Loop through each student
for i in range(num_students):
    name = input(f"\nEnter the name of student {i + 1}: ")
    
    # Get marks for three subjects
    mark1 = float(input(f"Enter marks for subject 1 for {name}: "))
    mark2 = float(input(f"Enter marks for subject 2 for {name}: "))
    mark3 = float(input(f"Enter marks for subject 3 for {name}: "))
    
    # Calculate total
    total = calculate_total(mark1, mark2, mark3)
    
    # Display result
    print(f"Total marks for {name}: {total}")
