#APCSP 2024
#Mr. Jaramillo
#Hong + Nichols
#January 11th
#To-Do list

#Intialize 
print("Welcome to OOg To-Do List please choose from the following task commands and enjoy your To-Do lists! Below is your list.")
mylist = ["bananas", "cherries", "apples"]
print(mylist)

#Functions
def add_task():
    new_item = input("Please type new item: ")
    mylist.append(new_item)
    print(mylist)

def delete_task():
    delete_item = input("Please type item: ")
    x=mylist.index(delete_item)
    mylist.pop(x)
    print(mylist)

def mark_task():
    mark_item = input("Please indicate the item to mark completed: ")
    x = mylist.index(mark_item)
    mylist.pop(x)
    mylist.insert(x, mark_item + " ✓")
    print(mylist)

def view_task():
    print(mylist)

def exit_task():
    quit()

def clear_list():
    mylist.clear()
    print(mylist)

def sort_list():
    mylist.sort()
    print(mylist)

def count():
    length_list = len(mylist)
    print(length_list)

def task_commands():
    print("\nAdd")
    print("Delete")
    print("Complete")
    print("Overview")
    print("Quit")
    print("Clear")
    print("Sort")
    print("Count")
    ans = input("\nChoose which task: ")
    if ans == "Add":
        add_task()

    elif ans == "Delete":
        delete_task()

    elif ans == "Complete":
        mark_task()

    elif ans == "Overview":
        view_task()

    elif ans == "Quit":
        exit_task()
    
    elif ans == "Clear":
        clear_list()

    elif ans == "Sort":
        sort_list()

    elif ans == "Count":
        count()

    task_commands()


#Main
task_commands()

