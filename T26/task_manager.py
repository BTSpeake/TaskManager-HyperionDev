#=====importing libraries===========
from datetime import date, datetime
import os

def userLogin():
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
                userMenu(username)
            else:
                print("Incorrect Pasword! Please try again...")
        else:
            print("Incorrect username! Please try again...")

def userMenu(username):
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
        gr - generate reports
        ds - Display statistics
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
            # Regisster a new user 
            reg_user(username)
        elif menu == 'a':
            # Add a new task 
            add_task()
        elif menu == 'va':
            # view all tasks
            view_all()
        elif menu == 'vm':
            # view all my tasks 
            view_mine(username)
        elif menu == "gr":
            # Generate reports 
            genReports()
        elif menu == 'ds':
            # Statistics menu option
            if username == "admin":
                stat_menu()
        elif menu == 'e':
            # Exit the program
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")
    return


def reg_user(username):
    if username != "admin":
        print("Error: Must be logged in as 'admin' to enter a new user!")
        return
    # Get usre to enter new username and password
    print("\nRegister New User")
    print(  "-----------------")
    user = input(        "Username:          ")
    with open("user.txt", 'r') as f:
        for line in f:
            if line.split()[0].strip(',') == user:
                print("Invalid input. Username already exists! ")
                return
    password = input(        "Password:          ")
    # Confirm the password
    password_confirm = input("Confirm Password:  ")
    if password == password_confirm:
        print("\nNew user succsefully created.\n")
        with open("user.txt", 'a') as f:
            f.write(f"\n{user}, {password}")
    else:
        print("\nPasswords do not match!\n")
    return

def add_task():
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
    return

def view_all():
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
    return

def view_mine(username):
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
    
    # Select tasks to mark them as complete
    while True:
        c=0
        print("\n Select Task (Enter -1 to cancel)")
        print(  "---------------------------------")
        task_num = int(input(" Task No.: "))
        if task_num == -1:
            print("Returning to main menu")
            break
        with open("tasks.txt", 'r') as f:
            lines = f.readlines()
            print(lines)
            for i, line in enumerate(lines):
                # Split the line into the individual values
                l = line.split(", ")
                # Check if task is assigned to current user
                if l[0] == username:
                    c += 1
                    print(c)
                    if c != task_num:
                        continue
                    # Check how the user wants to edit the task
                    print("\nEdit Options:")
                    print("-------------")
                    opt = int(input(''' 1. Mark task as complete\n2. Edit task \n3. Cancel \n '''))
                    if opt == 1: 
                        l[-1] = "Yes\n"
                        lines[i] = ", ".join(l)
                    if opt == 2:
                        newLine = editTask(l)
                        lines[i] = newLine
        with open("tasks.txt", 'w') as f:
            f.write("".join(lines))
    return

def editTask(l):
    """  Change either the asigned usser or date of the given task"""
    if "Yes" in l[-1]:
        print("Task already complete so can't be changed.")
        return ", ".join(l)
    opt = 0
    while opt != 3:
        opt = int(input('''\nWhat would you like to edit?
        1. user 
        2. due date 
        3. cancel 
        '''))
        if opt == 1:
            newUser = input("Enter new user: ")
            l[0] = newUser
            break
        elif opt == 2:
            newDate = input("Enter new date (dd month yyyy): ")
            l[4] = newDate
            break
    return ", ".join(l)

def stat_menu_old():
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
    return

def stat_menu():
    print("\nStatistics")
    print(  "-=--------")
    # Check if stat files exist
    if not os.path.isfile("task_overview.txt"):
        genReports()
    
    # Print out the contents of the stat files 
    with open("task_overview.txt", 'r') as f:
        for line in f:
            print(line)
    with open("user_overview.txt", 'r') as f:
        print("\nUser Overview")
        print(  "-------------")
        for line in f:
            print(line)

    return

def genReports():
    # Generate the task/user overview 
    cur_date = date.today()
    ntasks = 0 
    ntasks_complete = 0 
    ntasks_overdue = 0
    userTasks = {}
    userTasks_completed = {}
    userTasks_overdue = {}
    with open("tasks.txt", 'r') as f:
        for line in f:
            # count tasks
            ntasks += 1
            l = line.split(", ")
            # Check assigned user 
            if l[0] in userTasks.keys():
                userTasks[l[0]] += 1 
            else:
                userTasks[l[0]] = 1
            # Check if complete
            if "Yes" in l[-1]:
                ntasks_complete += 1
                if l[0] in userTasks_completed.keys():
                    userTasks_completed[l[0]] += 1 
                else:
                    userTasks_completed[l[0]] = 1
            else:
                # if incomplete check if overdue 
                due_date = datetime.strptime(l[4], "%d %b %Y").date()
                if cur_date > due_date:
                    ntasks_overdue += 1
                    if l[0] in userTasks_overdue.keys():
                        userTasks_overdue[l[0]] += 1 
                    else:
                        userTasks_overdue[l[0]] = 1

    nUsers = 0
    with open("user.txt", 'r') as f:
        for line in f:
            # count users
            nUsers += 1

    # Write results to task_overview file 
    with open("task_overview.txt", 'w') as f:
        f.write(  "Total number of tasks:            {0:d}".format(ntasks))
        f.write("\nTotal number completed tasks:     {0:d}".format(ntasks_complete))
        f.write("\nTotal number of incomplete tasks: {0:d}".format(ntasks - ntasks_complete))
        f.write("\nTotal number of overdue tasks:    {0:d}".format(ntasks_overdue))
        f.write("\nPercentage of incomplete tasks:   {0:.2f}".format(100*(ntasks - ntasks_complete)/ntasks))
        f.write("\nPercentage of overdue tasks:      {0:.2f}".format(100*ntasks_overdue/ntasks))   

    # write results to usser overview file
    with open("user_overview.txt", 'w') as f:
        f.write(  "Total number of users:            {0:d}".format(nUsers))
        f.write("\nTotal number of tasks:            {0:d}".format(ntasks))
        f.write("\nSee below for information on assigned tasks, if user information is not present then no tasks have been asigned.")
        for key in userTasks:
            f.write("\n\nUser: {0:s}".format(key))
            f.write(  "\n-------------------")
            f.write("\nUser tasks:                    {0:d}".format(userTasks[key]))
            f.write("\nPercentage of total tasks:     {0:.2f}".format(100*userTasks[key]/ntasks))
            
            try:
                pComplUserTasks = 100*userTasks_completed[key]/userTasks[key]
            except:
                pComplUserTasks = 0.00
            f.write("\nPercentage of completed tasks: {0:.2f}".format(pComplUserTasks))
            f.write("\nPercentage incomplete tasks:   {0:.2f}".format(100-pComplUserTasks))

            try: 
                pOverDueUserTasks = 100*userTasks_overdue[key]/userTasks[key]
            except:
                pOverDueUserTasks = 0.00
            f.write("\nPercentage of overdue tasks:   {0:.2f}".format(pOverDueUserTasks))

            

if __name__ == '__main__':
    userLogin()