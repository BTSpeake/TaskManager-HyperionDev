#=====importing libraries===========
from datetime import date

#====Login Section====
# First read in the valid usernames and paswords
user_list = []
pasword_list = []
with open("user.txt", 'r') as f:
    for line in f:
        l = line.strip("\n").split(", ")
        user_list.append(l[0])
        pasword_list.append(l[1])

# Get the user to login checking against the list of valid options
login = False 
while not login:
    print("")
    username = input("Username:  ")
    pasword = input("Pasword:   ")
    if username in user_list:
        if pasword in pasword_list:
            print("Login Succesfull!\n")
            login = True 
        else:
            print("Incorrect Pasword! Please try again...")
    else:
        print("Incorrect username! Please try again...")


#====Menu Section====
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    print("\n-------------------------------------------")
    if username == "admin":
        menu = input('''Please select one of the following options:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - Statistics
    e - Exit
    ''').lower()
    else:
        menu = input('''Please select one of the following options:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    ''').lower()


    if menu == 'r':
        if username != "admin":
            print("Error: Must be logged in as 'admin' to enter a new user!")
            continue
        # Get usre to enter new username and password
        print("\nRegister New User")
        print(  "-----------------")
        user = input(        "Username:          ")
        password = input(        "Password:          ")
        # Confirm the password
        password_confirm = input("Confirm Password:  ")
        if password == password_confirm:
            print("\nNew user succsefully created.\n")
            with open("user.txt", 'a') as f:
                f.write(f"\n{user}, {password}")
        else:
            print("\nPasswords do not match!\n")

    elif menu == 'a':
        print("\nAdd New Task")
        print(  "------------")
        # Get user input for the required values 
        user        = input("Asigned user:     ")
        title       = input("Task Title:       ")
        description = input("Task Description: ")
        due_date    = input("Task Due Date:    ")
        # Get the current date 
        cur_date = date.today().strftime("%d %b %Y")
        # Write the new task to the tasks file 
        with open("tasks.txt", 'a') as f:
            f.write(f"\n{user}, {title}, {description}, {cur_date}, {due_date}, No")

    elif menu == 'va':
        print("\nView All Tasks")
        print(  "--------------")
        # Read in each task and print it to the screen 
        with open("tasks.txt", 'r') as f:
            for i, line in enumerate(f):
                # Split the line into the individual values
                l = line.strip("\n").split(", ")
                # Create a formated print for the task 
                print(f"\nTask {i+1}")
                print("______________________________________")
                print(f"Task:            {l[1]}")
                print(f"Assigned to:     {l[0]}")
                print(f"Date Assigned:   {l[3]}")
                print(f"Due date:        {l[4]}")
                print(f"Task Complete?   {l[5]}")
                print(f"Task description: \n   {l[2]}")
                print("______________________________________")


    elif menu == 'vm':
        print("\nView My Tasks")
        print(  "--------------")
        # Read in each task and print it to the screen 
        with open("tasks.txt", 'r') as f:
            c = 0
            for line in f:
                # Split the line into the individual values
                l = line.strip("\n").split(", ")
                # Check if task is assigned to current user
                if l[0] == username:
                    c += 1
                    # Create a formated print for the task 
                    print(f"\nTask {c}")
                    print("______________________________________")
                    print(f"Task:            {l[1]}")
                    print(f"Assigned to:     {l[0]}")
                    print(f"Date Assigned:   {l[3]}")
                    print(f"Due date:        {l[4]}")
                    print(f"Task Complete?   {l[5]}")
                    print(f"Task description: \n   {l[2]}")
                    print("______________________________________")

    # Statistics menu option
    elif menu == 's':
        print("\nStatistics")
        print(  "----------")
        # Count the number of users
        nUsers = 0
        with open("user.txt", 'r') as f:
            for line in f:
                nUsers += 1
        # Count the number of tasks 
        nTasks = 0 
        with open("tasks.txt", 'r') as f:
            for line in f:
                nTasks += 1
        # Print options 
        print(f"Number of Users:   {nUsers}")
        print(f"Number of Tasks:   {nTasks}")        


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")