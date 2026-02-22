from datetime import datetime

class Task:
    def __init__(self, title):
        self.title = title
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔ Completed" if self.completed else "⏳ Pending"
        return f"{self.title} | {status} | Created: {self.created_at}"


class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ").strip()
        if title:
            self.tasks.append(Task(title))
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_completed(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to mark completed: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].mark_completed()
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                deleted = self.tasks.pop(index)
                print(f"Deleted task: {deleted.title}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            print("\n====== TO-DO LIST MENU ======")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_completed()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting application...")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = TodoApp()
    app.run()