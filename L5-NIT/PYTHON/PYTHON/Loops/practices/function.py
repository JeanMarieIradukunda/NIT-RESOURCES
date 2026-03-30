
usernames = ["Martine", "Preston", "Salomon" ,"Clarisse"]
passwords = ["123", "321"]

uname = input("Enter username: ")
passwd = input("Enter password: ")

def authentication():
    if uname in usernames and passwd in passwords:
        print(f"{uname}, loggged in successfuly")
    else:
        print("Invalid credentials")
authentication()
