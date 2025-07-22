todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added!")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
