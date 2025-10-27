import os
import sys

tasks = []

def show_tasks():
    if tasks:
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task_number):
    try:
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' removed.")
    except IndexError:
        print("Invalid task number.")

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())

def main():
    load_tasks()

    while True:
        print("\nOptions:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save & Exit")
        option = input("Choose an option: ")

        if option == '1':
            show_tasks()
        elif option == '2':
            task = input("Enter task: ")
            add_task(task)
        elif option == '3':
            show_tasks()
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid task number.")
        elif option == '4':
            save_tasks()
            print("Tasks saved. Exiting...")
            sys.exit(0)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
