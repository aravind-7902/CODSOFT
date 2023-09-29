# Define a dictionary to store tasks
tasks = {}

# Function to add a task to the To-Do list
def add_task():
    task_name = input("Enter task name: ")
    tasks[task_name] = False  # False represents that the task is not completed yet
    print("Task added!")

# Function to mark a task as completed
def complete_task():
    task_name = input("Enter task name to mark as completed: ")
    if task_name in tasks:
        tasks[task_name] = True
        print("Task marked as completed!")
    else:
        print("Task not found!")

# Function to display the To-Do list
def display_tasks():
    print("To-Do List:")
    for task, completed in tasks.items():
        status = "Completed" if completed else "Not Completed"
        print(f"{task}: {status}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Display Tasks")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        complete_task()
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")