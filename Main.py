tasks = []
print("Welcome to The Task Manager!!")
print("=" * 30)
print()
print("This program allows you to create, read, update, and delete files.")
# Creates a loop to return to main menu when user is done with updating task.
while True:
    print()
    print("\nWelcome to the Main Menu")
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
        continue
    elif choice == 1:
        while True:
            print("You selected to Add a task")
            Name = (input("What task would you like to Add and Name?: "))
            Due = (input("When is the due date for this task? (YYYY-MM-DD): "))
            Priority = input("Enter priority (High/Medium/Low: ")
            task = {
                "Name": Name,
                "Due": Due,
                "Priority": Priority,
                "Completed": False
            }
            tasks.append(task)
            print("Task added successfully!!")
            add_another = input("Would you like to add another task? (y/n): ").lower()
            if add_another != "y":
                print("Returning to Main Menu..")
                break
    elif choice == 2:
        if not tasks:
            print("No tasks Yet!")
        else:
            print("You selected to View Your tasks.:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["Completed"] else "Not Completed"
                # f string so that i can recall variables in a string
                print(f"{i}. {task['Name']} {task['Due']} {task['Priority']} {status}")
    elif choice == 3:
        if not tasks:
            print("No tasks available to Complete.")
        else:
            print("You selected to Complete a task!")
            print("Here are your current tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
        task_to_complete = int(input("Enter the number of the task you would like to complete: "))
        if 1 <= task_to_complete <= len(tasks):
            tasks[task_to_complete - 1]["Completed"] = True
            print(f"Task '{tasks[task_to_complete - 1]['Name']}' Marked as Complete!")
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    elif choice == 4:
        print("You selected to Delete a task!")
        print("Here are your current tasks:")
        print(tasks)
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
