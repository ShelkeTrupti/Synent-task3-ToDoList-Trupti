def display_menu():
    print("\n--- 📝 CLI Task Manager ---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task(tasks):
    task = input("\nEnter the task description: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Success: '{task}' has been added.")
    else:
        print("⚠️ Error: Task description cannot be empty!")

def delete_task(tasks):
    if not tasks:
        print("\n📭 No tasks available to delete.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"🗑️ Success: '{removed}' has been deleted.")
        else:
            print("⚠️ Error: Invalid task number!")
    except ValueError:
        print("⚠️ Error: Please enter a valid numerical choice.")

def view_tasks(tasks):
    print("\n📋 Current Tasks:")
    if not tasks:
        print("   No tasks found. Your list is empty!")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"  {index}. {task}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("\nGoodbye! Have a productive day! 👋")
            break
        else:
            print("⚠️ Invalid Choice! Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
