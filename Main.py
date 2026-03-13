tasks = []
print("Welcome to The File Manager!!")
print("=" * 30)
print()
print("This program allows you to create, read, update, and delete files.")
# Creates a loop to return to main menu when user is done with updating task.
while True:
    print()
    print("Welcome to the Main Menu")
    print("""
        1. Add Task
        2. View tasks
        3. Complete task
        4. Delete task
        5. Exit
        """)
    choice = int(input("Please select a option from the menu: "))
    if choice < 1 or choice > 5:
        print("Invalid input. Please select a menu option.")
        choice = int(input("Please select a option from the menu: "))
    elif choice == 1:
        print("You selected to Add a task")
        Name = (input("What task would you like to Add and Name?: "))
        Due = (input("When is the due date for this task? (YYYY-MM-DD): "))
        Priority = input("Enter priority (High/Medium/Low): ")
        task = {
            "Name": Name,
            "Due": Due,
            "Priority": Priority,
            "Completed": False
        }
        tasks.append(task)
        print("Task added successfully!!")
        while True:
            add_another = input("Would you like to add another task? (y/n): ").lower()
            if add_another == "y":
                task = (input("What task would you like to Add?: "))
                tasks[len(tasks) + 1] = task
                print("Task added successfully!!")
            else:
                print("Returning to menu...")
                break
    elif choice == 2:
        print("You selected to View Your tasks.:")
        for task in tasks:
            print(tasks.index(task) + 1, task)
    elif choice == 3:
        print("You selected to Complete a task!")
        print("Here are your current tasks:")
        print(tasks)
        task_to_complete = int(input("Enter the number of the task you would like to complete: "))
        if 0 < task_to_complete <= len(tasks):
            tasks[task_to_complete - 1] = "[Completed] " + tasks[task_to_complete - 1]
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    elif choice == 4:
        print("You selected to Delete a task!")
        task_to_delete = int(input("Enter the number of the task you would like to delete: "))
        if 0 < task_to_delete <= len(tasks):
            tasks.pop(task_to_delete - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    else:
        print("You selected to Exit the program!")
        print("Have a Great Day!!")
        break
