# The while True -> loop keeps running indefinitely
while True:
    # Ask the user to enter their age
    age = int(input("Enter your age (or type -1 to exit): "))
    
    # Exit condition
    if age == -1:
        print("Goodbye!")
        break

    # Check for negative numbers
    if age < 0:
        print("Invalid age! Age cannot be negative.")
    else:
        # Check age conditions
        if age == 18:
            print("You are exactly 18 years old.")
        elif age > 18:
            print("You are older than 18.")
        else:
            print("You are younger than 18.")

        # Check if the user is a teenager using logical operator 'and'
        if age >= 13 and age <= 19:
            print("You are a teenager.")

    print("-" * 30)  # Separator for clarity
