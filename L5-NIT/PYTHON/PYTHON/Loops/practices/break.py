while True:
    students = ["Alice", "John", "Peter", "Maria", "David", "Aimme"]
    search_name = input("Search by names: ")
    for name in students:
       if name == search_name:
           print("\n Searching ...", name)
           print(f"{search_name} found in list")
           break
       elif name != search_name :
           print(f" {search_name} is not found")
           break
       else:
           print("name was not found")
           break
        