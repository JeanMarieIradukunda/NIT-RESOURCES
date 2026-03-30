# Receive user details
names = input("Enter your names: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality:  ")

# check if the user is allowed to take an ID
if age >= 16 and nationality.lower() == "rwandan" :
    print("✅", names, "is allowed to take an ID.")
elif age < 16 :
        print("❌", names, "is not allowed to take an ID bcz is under age.")
else:
    print("❌", names, "is NOT allowed to take an ID because he/she is not a citizen.")
    
