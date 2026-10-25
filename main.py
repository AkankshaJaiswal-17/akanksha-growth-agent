import json

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def  save_completed_tasks():
    with open("completed_tasks.json" , "w") as file:
        json.dump(completed_tasks, file, indent = 4)

def load_completed_tasks():
    try:
        with open("completed_task.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

import os
print("Current Folder:", os.getcwd())
print("JSON file path:", os.path.abspath("tasks.json"))

def save_feedback():
    with open("feedback.json", "w") as file:
        json.dump(feedback, file, indent=4)

def load_feedback():
    try:
        with open("feedback.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

print("Welcome to Akanksha's Growth Agent")



tasks = load_tasks()
feedback = load_feedback()
completed_tasks = [] = load_completed_tasks()

def add_task(task_name):
    task_name = task_name.strip()

    if not task_name:
        print("Task cannot be empty ! ")

    elif task_name.lower() in [task.lower() for task in tasks]: 
        print("Task already exists !")

    else:
        tasks.append( task_name )
        save_tasks()
        print("Task Added:", task_name)

def list_tasks():
    if not tasks:
        print("No tasks added yet.")

    else:
        print("Tasks:",tasks)
    

def complete_task(task_name):
    task_name = task_name.strip()

    for task in tasks:
        if task.lower() == task_name.lower():
            tasks.remove(task)
            save_tasks()

            completed_tasks.append(task)
            save_completed_tasks()

            print("Task Completed:", task)

            while True:
                try:
                    rating = int(input("Rate your experience (1-5): "))

                    if 1 <= rating <= 5:
                        feedback.append({
                            "task": task,
                            "rating": rating
                        })
                        save_feedback()
                        print("Feedback Saved:", rating)
                        break
                    else:
                        print("Invalid Rating !!!")

                except ValueError:
                    print("Please Enter a valid number!")

            return

    print("Task Not Found !!!")

while True:

    try:
        print("\n===== Akanksha's Growth Agent =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. View Feedback")
        print("5.View Completed Tasks")
        print("6. Exit")
    
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task_name = input("Enter task name: ")
            add_task(task_name)

        elif choice == 2:
            list_tasks()

        elif choice == 3:
            task_name = input("Enter task to complete: ")
            complete_task(task_name)

        elif choice == 4:
            print("Feedback:", feedback)

        elif choice == 5:
            print("Completed Tasks:", completed_tasks)

        elif choice == 6:
            print("Exiting Akanksha's Growth Agent...")
            break

        else:
            print("Invalid Choice !!!")

    except ValueError:
        print("Please enter a valid number !")
        