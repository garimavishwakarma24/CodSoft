#defining empty list
tasks = []

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")
#taking input
        choice = input("Enter your choice: ")
#check cases
        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == "2":
            if tasks:
                print("Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks available!")

        elif choice == "3":
            if tasks:
                print("Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                task_number = int(input("Enter the task number to delete: ")) - 1
                if task_number < len(tasks):
                    task = tasks.pop(task_number)
                    print(f"Task '{task}' deleted successfully!")
                else:
                    print("Invalid task number!")
            else:
                print("No tasks available!")

        elif choice == "4":
            if tasks:
                print("Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                task_number = int(input("Enter the task number to update: ")) - 1
                if task_number < len(tasks):
                    new_task = input("Enter the new task: ")
                    tasks[task_number] = new_task
                    print(f"Task updated to '{new_task}' successfully!")
                else:
                    print("Invalid task number!")
            else:
                print("No tasks available!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


