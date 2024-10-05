#To-Do List Application

tasks = []  # List to store tasks

while True:
    print("\n--- To-Do List Application ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)  # Add the task to the list
        print(f"Task '{task}' added successfully!")

    elif choice == '2':
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks to show!")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    elif choice == '3':
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)  # Remove the task from the list
                    print(f"Task '{removed_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
