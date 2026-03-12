tasks = []
while True:
    print("Welcome to The File Manager!!")
    print("=" * 30)
    print()
    print("This program allows you to create, read, update, and delete files.")
    print()
    print("Welcome to the Main Menu")
    print("""
        1. Add Task
        2. View tasks
        3. Complete task
        4. Delete task
        5. Exit
        """)
    menu_selection = int(input("Please select a option from the menu: "))
    if menu_selection < 1 or menu_selection > 5:
        print("Invalid input. Please select a menu option.")
        menu_selection = int(input("Please select a option from the menu: "))
    elif menu_selection == 1:
        print("You selected to Add a task")
        task = (input("What task would you like to Add?: "))
        tasks.append(task)
        print("Task added successfully!!")
        while True:
            add_another = input("Would you like to add another task? (y/n): ").lower()
            if add_another == "y":
                task = (input("What task would you like to Add?: "))
                tasks.append(task)
                print("Task added successfully!!")
            else:
                print("Returning to menu...")
                break
    elif menu_selection == 2:
        print("You selected to View Your tasks.:")
        for task in tasks:
            print(tasks.index(task) + 1, task)
    elif menu_selection == 3:
        print("You selected to Complete a task!")
        print(input("What task would you like to update?"))
    elif menu_selection == 4:
        print("You selected to Delete a task!")
        print(input("What task would to like to Delete?"))
    else:
        print("You selected to Exit the program!")
        print("Have a Great Day!!")
        break
