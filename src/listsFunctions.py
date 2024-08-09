tasks = []

def createTask():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task {task} was added!\n")

def listTask():
    if not tasks:
        print("There are no tasks.")
    else:
        print("Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task {index}. {task}")

def deleteTask():
    for i, task in enumerate(tasks):
        print(f"{i}: {task}")
    taskToDelete = int(input("\nWhich task would you like to delete?\n"))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
        tasks.pop(taskToDelete)
        print(f"Task {taskToDelete} was deleted.\n")
    else:
        print(f"Task {taskToDelete} not found. Please enter a valid item.")

    