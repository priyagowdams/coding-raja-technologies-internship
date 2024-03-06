import json
from datetime import datetime

tasks = []

def show_menu():
    print("\nCommand Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")
    print()

def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"task": task_name, "priority": priority, "due_date": due_date, "completed": False})
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        del tasks[task_index]
        print("Task removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_task_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
        tasks[task_index]["completed"] = True
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def view_tasks():
    print("\nTasks:")
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']} - Priority: {task['priority']} - Due Date: {task['due_date']}")

def save_tasks_to_file():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks_from_file():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():
    global tasks
    tasks = load_tasks_from_file()

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
            save_tasks_to_file()
        elif choice == "2":
            remove_task()
            save_tasks_to_file()
        elif choice == "3":
            mark_task_completed()
            save_tasks_to_file()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            save_tasks_to_file()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
