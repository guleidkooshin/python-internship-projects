import json

FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save tasks to JSON file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a task
def add_task():
    title = input("Enter a task: ") 

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks()

    print("Task added successfully!")


# View tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")

    for i, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Not completed"

        print(f"{i}. {task['title']} - {status}")


# Delete a task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks.pop(number - 1)
        save_tasks()

        print("Task deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Mark task as completed
def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["completed"] = True
        save_tasks()

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


# Load tasks when program starts
tasks = load_tasks()


# Main menu
while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")