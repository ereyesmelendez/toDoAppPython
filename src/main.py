from listsFunctions import createTask, listTask, deleteTask

if __name__ == "__main__":

    while True:
        print("\nWhat would you like to do today?\n")
        print("\n1. Add a New Task")
        print("\n2. See Saved Task")
        print("\n3. Delete Task")
        print("\n4. Quit")

        choice = input("Enter the number of the choice you would like to do: ")

        if choice == "1":
            createTask()

        elif choice == "2":
            listTask() 
        
        elif choice == "3":
            deleteTask()

        elif choice == "4":
            print("Have a magical day!")
            break
        else:
            print("Invalid entry. Please select a valid entry.")