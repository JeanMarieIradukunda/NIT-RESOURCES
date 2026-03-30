# ==========================================
# SCHOOL LIBRARY MANAGEMENT SYSTEM
# Demonstrates:
# 1. Stack  (LIFO - Last In, First Out)
# 2. Queue  (FIFO - First In, First Out)
# ==========================================


# -------------------------------
# PART A: STACK (Book Returns)
# -------------------------------

# We create an empty list.
# This list will behave like a STACK.
# A stack follows LIFO (Last In, First Out).
returned_books = []


# -------------------------------
# PART B: QUEUE (Borrow Requests)
# -------------------------------

# We create another empty list.
# This list will behave like a QUEUE.
# A queue follows FIFO (First In, First Out).
borrow_requests = []


# --------------------------------
# MAIN PROGRAM LOOP
# --------------------------------

# This loop runs forever until the user chooses to exit.
while True:

    # Display menu options to the user
    print("\n====== LIBRARY SYSTEM ======")
    print("1. Add Returned Book (Stack)")
    print("2. Process Returned Book (Stack)")
    print("3. Display Returned Books")
    print("4. Add Borrow Request (Queue)")
    print("5. Process Borrow Request (Queue)")
    print("6. Display Borrow Requests")
    print("7. Exit")

    # Ask the user to choose an option
    choice = input("Choose an option: ")


    # =====================================
    # STACK OPERATIONS (BOOK RETURNS)
    # =====================================

    # OPTION 1: Add returned book to stack
    if choice == "1":

        # Ask user to enter book name
        book = input("Enter book name: ")

        # append() adds the book to the END of the list
        # In a stack, adding is called PUSH
        returned_books.append(book)

        print("Book added to stack.")


    # OPTION 2: Process returned book
    elif choice == "2":

        # First check if the stack is NOT empty
        # If list has items, Python treats it as True
        if returned_books:

            # pop() removes the LAST item in the list
            # This follows LIFO (Last In, First Out)
            book = returned_books.pop()

            # Display which book was processed
            print("Processed returned book:", book)

        else:
            # If stack is empty, nothing to process
            print("No returned books to process.")


    # OPTION 3: Display all returned books
    elif choice == "3":

        print("Returned Books (Stack):")

        # Display the entire list
        # Shows books in the order they were added
        print(returned_books)



    # =====================================
    # QUEUE OPERATIONS (BORROW REQUESTS)
    # =====================================

    # OPTION 4: Add borrow request
    elif choice == "4":

        # Ask user to enter book name
        request = input("Enter borrow request (book name): ")

        # append() adds request to END of list
        # In a queue, this is called ENQUEUE
        borrow_requests.append(request)

        print("Borrow request added.")


    # OPTION 5: Process borrow request
    elif choice == "5":

        # Check if queue is not empty
        if borrow_requests:

            # pop(0) removes the FIRST item in the list
            # This follows FIFO (First In, First Out)
            request = borrow_requests.pop(0)

            print("Processed borrow request:", request)

        else:
            print("No borrow requests to process.")


    # OPTION 6: Display all borrow requests
    elif choice == "6":

        print("Borrow Requests (Queue):")

        # Display the queue list
        print(borrow_requests)



    # =====================================
    # EXIT OPTION
    # =====================================

    # OPTION 7: Exit the program
    elif choice == "7":

        print("Exiting system...")

        # break stops the while loop
        # The program ends here
        break


    # If user enters something invalid
    else:
        print("Invalid choice! Try again.")