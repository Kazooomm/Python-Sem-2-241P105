'''
Mohd Qazim Ansari
Fe-D
241P105/36
'''

tasks = []

def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTask List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

while True:
    print("Task Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Sort Tasks")
    print("5. Display Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        display_tasks()
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")

    elif choice == '3':
        display_tasks()
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        tasks.sort()
        print("Tasks sorted successfully!")

    elif choice == '5':
        display_tasks()

    elif choice == '6':
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

