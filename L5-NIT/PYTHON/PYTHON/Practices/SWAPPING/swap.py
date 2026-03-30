while True:
    number = input("Enter any number please: \n")

    if number.lower() == "exit":
        print("Bye!! \n")
        print("Program Terminated.")
        break

    number = int(number)

    if number % 2 == 0:
        print(number, "is even \n")
    else:
        print(number, "is odd \n")
