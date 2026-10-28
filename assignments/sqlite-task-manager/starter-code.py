import sqlite3

DATABASE_FILE = "tasks.db"


def initialize_database():
    # TODO: Create the tasks table if it does not already exist.
    pass


def add_task(title):
    # TODO: Insert a non-empty task title using a parameterized query.
    pass


def list_tasks():
    # TODO: Fetch and display all tasks, including their completion status.
    pass


def complete_task(task_id):
    # TODO: Mark the task with this ID as complete.
    pass


def delete_task(task_id):
    # TODO: Delete the task with this ID.
    pass


def main():
    initialize_database()

    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(input("Task title: "))
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task(input("Task ID: "))
        elif choice == "4":
            delete_task(input("Task ID: "))
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()