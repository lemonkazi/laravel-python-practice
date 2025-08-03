import json
import os

FILE = "todo_app/todo.json"  # Path to the JSON file where tasks are stored

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    if tasks is None:
        tasks = []
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Display all tasks
def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
        return
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i + 1}. {status} {task['title']}")

# Add a task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("✅ Task added.")
    else:
        print("⚠️ Task title can't be empty.")

# Mark task as done
def complete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("✅ Task marked as completed.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")
