# Inventory Control Program

# Create an empty dictionary to store products
# Structure:
# {
#    "ProductName": quantity
# }
inventory = {}


# Function to add a new product
def add_product():
    # Ask user for product name
    product = input("Enter product name: ")
    
    # Ask user for quantity (integer)
    quantity = int(input("Enter quantity: "))
    
    # Use update() to add product to dictionary
    # If product already exists, it will overwrite the quantity
    inventory.update({product: quantity})
    
    print("Product added/updated successfully!\n")


# Function to update existing product quantity
def update_product():
    product = input("Enter product name to update: ")
    
    # Check if product exists using keys()
    if product in inventory.keys():
        quantity = int(input("Enter new quantity: "))
        
        # Use update() to modify quantity
        inventory.update({product: quantity})
        
        print("Product quantity updated!\n")
    else:
        print("Product not found.\n")


# Function to remove a product
def remove_product():
    product = input("Enter product name to remove: ")
    
    # Use pop() to remove product safely
    removed = inventory.pop(product, None)
    
    if removed is not None:
        print("Product removed successfully!\n")
    else:
        print("Product not found.\n")


# Function to check if a product exists
def check_product():
    product = input("Enter product name to check: ")
    
    # Check using keys()
    if product in inventory.keys():
        print(f"{product} exists with quantity {inventory[product]}\n")
    else:
        print("Product does not exist.\n")


# Function to display all products sorted alphabetically
def display_products():
    print("Inventory List (Sorted Alphabetically):")
    
    # sorted() is used on keys() to sort product names
    for product in sorted(inventory.keys()):
        print(product, ":", inventory[product])
    
    print()


# Function to clear entire inventory
def clear_inventory():
    # Use clear() to remove all items
    inventory.clear()
    print("Inventory cleared successfully!\n")


# Main program loop
while True:
    print("===== Inventory Control Program =====")
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Remove Product")
    print("4. Check Product Exists")
    print("5. Display All Products")
    print("6. Clear Inventory")
    print("7. Exit")
    
    choice = input("Choose an option: ")
    
    # Call functions based on user choice
    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        remove_product()
    elif choice == "4":
        check_product()
    elif choice == "5":
        display_products()
    elif choice == "6":
        clear_inventory()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")