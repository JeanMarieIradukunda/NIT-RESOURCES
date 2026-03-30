
std_number = int(input("How many students: "))

def calculate_total(Maths, English, Python):
    return Maths + English + Python

for number in range(std_number):
    std_names = input(f"Enter the names of student - {number+1}: ")
    Maths = float(input("Enter marks obtained in Maths: "))
    English = float(input("Enter marks obtained in English: "))
    Python = float(input("Enter marks obtained in Python: "))

    totalMarks = calculate_total(Maths, English, Python)
    print("----------------------");
    print(f"{std_names}'s marks obtained in All subjects are: ", totalMarks)