#First let's make print options: Add task, List task, Mark task as completed, Exit.
task = []

def menu():
    print ("1. Add task")
    print ("2. List task")
    print ("3. Mark task as completed")
    print ("4. Exit")
    print ("")

# then we make variables for each case, excluding "Exit" which will be broken from the loop
def add_task ():
    new_task = input("What task would you like to add? ")
    task.append(new_task)

def list_task ():
    print ("These are all your current tasks")
    print (task)
    print ("")

def mark_task ():
    while True: 
        remove_task = input ("What task would you like to mark as completed? ")
        if remove_task in task:
            task.remove(remove_task)
            print ("Task marked as completed ✅")
        else: 
            print("Task not found ❌")

        again = input("Is there another task you want to mark as completed (Yes or No)? ")
        if again.lower() != "Yes":
           break 

#Then we provide the choices.
while True: 
    menu ()
    choice = int(input("What would you like to do? "))
    
    if choice == 1: 
        add_task()
    elif choice == 2: 
        list_task()
    elif choice == 3: 
        mark_task()
    elif choice == 4: 
        break 
    else: 
        print ("Wrong input") 

