print("------WELCOME TO PYTHON------")

attempts_times = 3
correct_username = "admin"
correct_password = "123"

for attemps in range(attempts_times):

    username =input("Enter the username: ")
    password =input("Enter the password: ")

    if username == correct_username and password == correct_password:
        print(" == WELCOME TO PYHTON 🐍 MODULE ==")
        print(" == ----------------------------==")
        print(f"U had right choice dear {username}")
        break
    else:
        print("❌ - Incorrect Credentials - ❌ Try again: ")
        print(f"Remains {attemps + 1} of {attempts_times}")
        