import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Todo List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Quit")

def view_tasks(todo_list):
    print("\nTasks:")
    if not todo_list:
        print("No tasks.")
    else:
        for index, task in enumerate(todo_list, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{index}. {task['description']} - {status}")

def add_task(todo_list):
    description = input("Enter task description: ")
    todo_list.append({'description': description, 'completed': False})
    print("Task added successfully!")

def mark_completed(todo_list):
    view_tasks(todo_list)
    try:
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    todo_list = []

    while True:
        clear_screen()
        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
