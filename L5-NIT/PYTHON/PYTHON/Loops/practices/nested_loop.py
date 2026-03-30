# Number of students and subjects
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

# Outer loop → for each student
for s in range(1, num_students + 1):
    print(f"\n🏫 Student #{s}:")
    
    # Inner loop → for each subject of that student
    for sub in range(1, num_subjects + 1):
        mark = float(input(f"  ➤ Enter mark for Subject #{sub}: "))
        
        # Optional: check performance
        if mark >= 50:
            print("     ✅ Passed")
        else:
            print("     ❌ Failed")
