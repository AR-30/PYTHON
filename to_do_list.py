import json

# Global tasks list
tasks = []

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f'{i}. {task["task"]} [{status}]')

# Function to remove a task
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed["task"]}" removed.')
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f'Task "{tasks[task_number - 1]["task"]}" marked as completed.')
    else:
        print("Invalid task number.")

# Function to save tasks to a JSON file
def save_tasks(filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved.")

# Function to load tasks from a JSON file
def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")

# Main function to run the application
def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to mark as completed: "))
            complete_task(task_number)
        elif choice == '5':
            save_tasks()
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the application
if __name__ == "__main__":
    main()
