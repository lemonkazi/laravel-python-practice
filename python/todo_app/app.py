# Import functions from all modules from utilities package
from colorama import Fore, Back, Style, init
from utilities.todo_ops import load_tasks, save_tasks, add_task, list_tasks, complete_task

# Initialize colorama
init(autoreset=True)
# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO APP ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print(Fore.GREEN + "📝 Tasks saved. Goodbye!")
            break
        else:
            print(Fore.YELLOW + "⚠️ Invalid choice. Try again.")

if __name__ == "__main__": # pragma: no cover
    # This block is for running the app directly, not during tests.
    main()
