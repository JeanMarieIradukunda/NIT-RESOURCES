print()
print("-------------------------------------------------")
print("📗📘 == WELCOME TO THE PVC LIBRARY SYSTEM == 📗📘")
print("-------------------------------------------------")

print("Choose one of the following options")
print()
print("   1️⃣  View all Books 📖")
print("   2️⃣  Borrow a book 📖")
print("   📤  Terminate the Program")

option = int(input("Enter your option: "))

books = {
    'English': {'name': "Englih at Work place" , 'Author': 'Claudine', 'copies': 5},
    'Python': {'name': "Basics of Python" , 'Author': 'Babou', 'copies': 5}
}

def all_books():
    print("   1️⃣  List of Books 📖")
    print("book name: ",books["English"]['name'], "Author: ", books["English"]['Author'], "number of copy is: ",books["English"]['copies'])
    print("book name: ",books["Python"]['name'], "Author: ",books["English"]['Author'], "number of copy is: ",books["English"]['copies'])

def borrow_books():
    names = input("enter your names: ")
    trades = input("enter your class: ")
    std_borrowed = { }

    std_borrowed['name'] = names
    std_borrowed['tade'] = trades

    for i in books["English"].items():
        for j in books["Python"].items():
            print("hii")
while True:
    if option == 1:
        all_books()
        break
        


