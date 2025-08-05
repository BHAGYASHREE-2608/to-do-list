# todo_oop.py

class Task:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        task = Task(task_description)
        self.tasks.append(task)
        print(f"Added: {task_description}")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            task = input("Enter task description: ")
            todo.add_task(task)
        elif choice == "3":
            try:
                task_num = int(input("Enter task number to remove: "))
                todo.remove_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
