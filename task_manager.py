
# TASK MANAGER PROGRAM

# Default Admin login   Username: admin     Password: password

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Creates user register on program start if does not already exist
def create_user_file():
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as user_file:
            user_file.write("testuser;notone2")
            print("User register file created and will be stored as users.txt")

# Creates admin register on program start if does not already exist
def create_admin_file():
    if not os.path.exists("admin.txt"):
        with open("admin.txt", "w") as admin_file:
            admin_file.write("admin;password")
            print("Admin register file created and will be stored as admin.txt")

# Creates tasks file on program start if does not already exist
def create_tasks_file():
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as task_file:
            print("Task file has been created and will be stored as tasks.txt.")

# Removes error created by blank lines at top of txt file, when retrieving data  
def no_blank_lines(file):
    for l in file:
        line = l.rstrip()
        if line:
            yield line

# Loads normal users into a dictionary for adding/removing users with other functions
def normal_user_store():
    normal = {}
    with open("user.txt", "r") as user_dict:
        for line in no_blank_lines(user_dict):
            username, password = line.strip().split(";")
            normal[username.lower()] = password
        return normal

# Loads admin users into a dictionary for adding/removing users with other functions
def admin_user_store():
    admins = {}
    with open("admin.txt", "r") as admin_user_dict:
        for line in no_blank_lines(admin_user_dict):
            username, password = line.strip().split(";")
            admins[username.lower()] = password
        return admins

# Retrieves tasks from tasks.txt into 'clean_list' of dictionaries with
# 'completed' as 'yes' or 'no'
# Needed for editing tasks via 'View my tasks' to work,
# Other True/False not recognised as iterables?
def retrieve_tasks():
    try:
        clean_list = []
        with open("tasks.txt", "r") as all_task_file:
            content = no_blank_lines(all_task_file.readlines())
            for line in content:
                tasks_file = line.strip().split(",")
                task = {
                    (tasks_file[0]) : (tasks_file[1]),
                    (tasks_file[2]) : (tasks_file[3]),
                    (tasks_file[4]) : (tasks_file[5]),
                    (tasks_file[6]) : (tasks_file[7]),
                    (tasks_file[8]) : (tasks_file[9]),
                    (tasks_file[10]): (tasks_file[11])
                }
                clean_list.append(task)
        return clean_list
    except FileNotFoundError:
        print("File not found")

# Retrieves tasks from tasks.txt into 'clean_list' of dictionaries with
# 'completed' as 'True' or 'False'
# Needed for generating reports
def retrieve_tasks_status():
    try:
        clean_list = []
        with open("tasks.txt", "r") as all_task_file:
            content = no_blank_lines(all_task_file.readlines())
            for line in content:
                tasks_file = line.strip().split(",")
                task = {
                    (tasks_file[0]) : (tasks_file[1]),
                    (tasks_file[2]) : (tasks_file[3]),
                    (tasks_file[4]) : (tasks_file[5]),
                    (tasks_file[6]) : (tasks_file[7]),
                    (tasks_file[8]) : (tasks_file[9]),
                    (tasks_file[10]): True if (tasks_file[11]) == 'yes' else False
                }
                clean_list.append(task)
        return clean_list
    except FileNotFoundError:
        print("File not found")

# Login function
def login():
    normal_users_dict = normal_user_store()
    admin_users_dict = admin_user_store()
    print("\nEnter your username and password to login")
    global current_user
    while True:
        current_user = input("\nEnter Username: ").lower()
        if len((current_user).strip()) == 0:
            print("You have not entered anything. Please try again")
            continue
        else:
            if current_user in normal_users_dict or current_user in admin_users_dict:
                current_password = input("\nEnter Password: ").lower()
                if current_password in normal_users_dict.values() or \
                    current_password in admin_users_dict.values():
                    print("Login succesful!")
                    return current_user
                elif len((current_password).strip()) == 0:
                    print("You haven't entered anything")
                else:
                    print("Unsuccessful. Wrong password")
                    continue
            else:
                print("That user name does not exist")
                continue
                
# Logout function
def logout():
    global current_user
    current_user = None
    login()

# Task manager function
# Creates each of the three base .txt files before logging in the user and proceeding to main menu
def task_manager():
   create_user_file()
   create_admin_file()
   create_tasks_file()
   login()
   main_menu()

# Main menu loop with all options for regular users and admin menu entry for admins
def main_menu():
    while True:
        menu_option = input('''\n\t\tSelect one of the following Options below:\n
                                r - Registering a new user
                                a - Adding a task
                                va - View all tasks
                                vm - View my task
                                ad - Admin menu
                                e - Exit
                                : ''').lower()
    
        if menu_option == "r":
            reg_user()
        elif menu_option == "a":
            add_task()
        elif menu_option == "va":
            view_all_tasks()
            break
        elif menu_option == "vm":
            view_my_tasks()
            break
        elif menu_option == "ad":
            admin_options()
        elif menu_option == "e":
            logout()
        else:
            print("That was an invalid entry, please try again")
            continue

# Admin menu options accessed from main menu options            
def admin_options():
    user_type_normal = normal_user_store()
    if current_user in user_type_normal:
        print("You are not authorised to access admin options")
        main_menu()
    else:
        while True:
            admin_menu = input('''\n\t\tWelcome to the Admin menu. Select one of the following Options below:\n
                                    ds - Display statistics
                                    gr - Generate reports
                                    du - Delete user
                                    r - Register a new admin
                                    e - Exit admin menu
                                    : ''').lower()

            if admin_menu == "ds":
                display_statistics()
            elif admin_menu == "gr":
                generate_reports()
            elif admin_menu == "du":
                delete_user()
            elif admin_menu == "r":
                reg_admin_user()
            elif admin_menu == "e":
                main_menu()
            else:
                print("That was an invalid entry, please try again")
                continue

# Register a new regular user
def reg_user():
    normal = normal_user_store()
    username = validate_new_user()
    password = validate_new_pass()
    normal[username] = password
    file_write_users(normal)
    print(f"{username} has been registered successfully")
    main_menu()

# Writes user dictionary to user.txt, wipes out previous entries, re-writes file
def file_write_users(normal):
    with open("user.txt", "w") as user_file:
        for username, password in normal.items():
            user_file.write(f"\n{username};{password}")

# Register a new admin user, only through admin menu
def reg_admin_user():
    admins = admin_user_store()
    new_admin = validate_new_user()
    new_pass = validate_new_pass()
    admins[new_admin] = new_pass
    file_write_admin(admins)
    print(f"{new_admin} has been registered successfully")
    admin_options()

# Writes admin dictionary to admin.txt, wipes out previous entries, re-writes file
def file_write_admin(admins):
    with open("admin.txt", "w") as admin_file:
        for username, password in admins.items():
            admin_file.write(f"\n{username};{password}")

# Validate a new username, check not currently in normal user store or admin user store
# Adds some criteria for valid username
def validate_new_user():
    while True:
        normal = normal_user_store()
        admin = admin_user_store()
        new_user = input("Enter a new username: ").lower()
        if len(new_user) < 5 or len(new_user) > 20:
            print("Usernames must be between 10 and 20 characters long")
            continue
        elif new_user in normal.keys() or new_user in admin.keys():
            print("That user already exists. Please choose another username")
            continue
        new_user_check = input("Enter again the same username to verify ").lower()
        if new_user == new_user_check:
            print("Awesome! Those match")
            return new_user

# Validate new password, checking some criteria for making a "stronger" password
def validate_new_pass():
    while True:
        print("Passwords must be between 5 and 20 characters and contain at least one number")
        new_user_pass = input("Enter a password ").lower().replace(" ", "")
        if new_user_pass == 0:
            print("Error. You have not entered anything")
            continue
        elif len(new_user_pass) < 5 or len(new_user_pass) > 20:
            print("Password must be between 5 and 20 characters")
            continue
        elif not any(character.isdigit() for character in new_user_pass):
            print("Your password must contain at least one number")
            continue
        new_user_pass_check = input("Enter your password again to verify ").lower()
        if new_user_pass == new_user_pass_check:
            print("Awesome! Those match")
            return new_user_pass

# Deletes a user, only admin can access this through admin options function
def delete_user():
    normal_users = normal_user_store()
    user_type_admin = admin_user_store()
    username = input("Enter the user to delete ")
    if username in user_type_admin.keys():
        print("You can't delete an admin, only a normal user")
        return
    elif username not in normal_users:
        print(f"{username} does not exist")
        return
    else:
        validate = input(f"Proceed to delete {username}? (y/n)").lower()
        while True:
            if validate == "y":
                del normal_users[username]
                file_write_users(normal_users)
                print(f"{username} has been deleted")
                admin_options()
            elif validate == "n":
                print("Deletion cancelled")
                admin_options()
            else:
                print("That was an invalid entry, please try again")
                continue
        
# Allows user to add a new task with task title, description, due date
def add_task():
    admin_users = admin_user_store()
    normal_users = normal_user_store()
    while True:
        task_username = input("Name of person assigned to task or '-1' to return to the main menu: ").lower()
        if len(task_username) == 0:
            print("You didn't enter anything, try again")
            continue
        elif task_username == '-1':
            main_menu()
            break
        elif task_username in normal_users.keys() or task_username in admin_users.keys():
            print("User name recognised")
            task_title = input("Title of Task: ")
            if len(task_title) < 10 or len(task_title) > 50:
                print("Title must be between 10 and 50 characters long")
                continue
            task_description = input("Description of Task: ")
            break
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            break
        except ValueError:
                print("Invalid datetime format. Please use the format specified")
    
    curr_date = date.today()
    new_task = (f"title,{task_title},assigned to,{task_username},description,{task_description},\
due date,{task_due_date},assigned date,{curr_date},completed,no")

    with open("tasks.txt", 'a+') as tasks_file:
        tasks_file.write(f"{new_task}\n")

# Allows a user to view all tasks assigned to everybody
def view_all_tasks():
    tasks_file = retrieve_tasks()
    while len(tasks_file) == 0:
        print("There are no registered tasks currently\
              go back to main menu and add tasks")
        answer = input("Press 'y' to go back to main menu").lower()
        if answer == "y":
            main_menu()
        elif answer != "y":
            print("Incorrect, press 'y' to continue back to main menu")
            continue
    print("\t----------Viewing all tasks----------")    
    print(*[(f"\t{key}\t\t\t{value}") for item in tasks_file for (key, value) in item.items()], sep = "\n")
    while True:
        answer = input("\n\tPress 'y' to go back to main menu").lower()
        if answer == "y":
            main_menu()
        elif answer != "y":
            print("\n\tIncorrect, press 'y' to continue back to main menu")
            continue
    
# Allows a user to view all of their own assigned tasks
# Then presents options to edit/mark as complete or return to main menu
# Options to edit include due date and assigned user
# Task edit saved to main list and then passed to function to update file save
def view_my_tasks():
    global current_user
    tasks_file = retrieve_tasks()
    admins = admin_user_store()
    normal_users = normal_user_store()
    
    enumerate_list = [(f"\n\t{list_number}\t{dictionary['title']}") for list_number, dictionary\
                      in enumerate(tasks_file) if dictionary["assigned to"] == current_user][:]
    print(*enumerate_list)

    while True:
        try:
            action = int(input("\n\tWould you like to edit or mark a task as complete (2)\
                            \n\tOr return to the main menu (-1)? "))
            if action == (-1):
                main_menu()
            elif action == 2:
                try:
                    task_selection = int(input("\n\t\t\
    Enter the number associated with the task you would like to modify: "))
                    task_edit = tasks_file[task_selection]
                    if tasks_file[task_selection]['completed'] == 'yes':
                        print("\n\t\tThis task has already been marked as complete\
                              \n\t\tYou can no longer edit this task")
                        view_my_tasks()
                        break
                    if tasks_file[task_selection]['assigned to'] != current_user:
                        print("\n\t\tThat number was not assosciated with any of your tasks")
                        print("\n\t\tPlease try again")
                    else:
                        tasks_file.pop((task_selection))
                        try:
                            choice = int(input(f"\n\t\tYou have selected Task: {task_selection}\
                                                \n\t\tWould you like to edit the task(1),\
                                                \n\t\tOr to mark task as complete (2)?.\
                                                \n\t\tNote: you can only edit assigned user or due date "))
                            if choice == 1:
                                try:
                                    edit_choice = int(input(f"\n\t\tYou have opted to edit Task: {task_selection}.\
                                                            \n\t\tWould you like to edit the assigned user (3)?,\
                                                            \n\t\tWould you like to edit the task due date (4)? "))
                                    if edit_choice == 3:
                                        print("\n\t\tYou have opted to edit the task's assigned user")
                                        print(f"\n\t\tThe user is currently: {task_edit['assigned to']}")
                                        new_user = input("\n\t\tEnter the username who will now be assigned this task: ")
                                        if new_user in admins.keys() or new_user in normal_users.keys():
                                            task_edit['assigned to'] = new_user
                                            tasks_file.append(task_edit)
                                            update_tasks_file(tasks_file)
                                            print("\n\t\tYour edit was saved successfully")
                                            break
                                        else:
                                            print("\n\t\tInvalid username. This username does not exist")
                                            continue
                                    elif edit_choice == 4:
                                        print("\n\t\tYou have opted to edit the task due date")
                                        print(f"\n\t\tYour task due date is currently: {task_edit['due date']}")
                                        new_due_date = input("\n\t\tEnter your task's new due date in the format YYYY-MM-DD: ")
                                        try:
                                            task_edit['due date'] = new_due_date
                                            tasks_file.append(task_edit)
                                            update_tasks_file(tasks_file)
                                            print("\n\t\tYour edit was saved successfully")
                                            break
                                        except ValueError:
                                            print("\n\n\t\tInvalid datetime format. Please use the format specified")
                                            continue
                                    elif edit_choice != 3 or edit_choice != 4:
                                        print("\n\t\tInvalid entry")
                                        continue
                                except ValueError:
                                    print("\n\t\tThat was not an integer")
                            elif choice == 2:
                                validate = input(f"\n\t\tYou have chosen to mark the task as complete.\
                                                \n\t\tAre you sure you would like to continue? (Y/N) ").lower()
                                if validate == "y":
                                    task_edit['completed'] = 'yes'
                                    tasks_file.append(task_edit)
                                    update_tasks_file(tasks_file)
                                    print("\n\t\tYour task has been marked as complete")
                                    break
                                else:
                                    print("\n\t\tError. This task has already been marked as complete")
                                    continue
                            elif choice != 1 or choice != 2:
                                print("\n\t\tInvalid Entry.")
                        except ValueError:
                            print("\n\t\tThat was not an integer")
                except ValueError:
                    print("\n\t\tThat was not an integer")    
            elif action != (-1) or action != 2:
                print("\n\tInvalid entry. Please enter either option '-1' or option '2'")
                continue
        except ValueError:
            print("\n\t\tThat was not an integer")
    while True:
        return_question = int(input("\n\t\tWould you like to return to the main menu (5)?\
                            \n\t\tOr would you like to edit another task (6)?"))
        if return_question == 5:
            main_menu()
            break
        elif return_question == 6:
            view_my_tasks()
        else:
            print("\n\t\tInvalid Entry")
            continue

# Updates file save from task edits
def update_tasks_file(tasks_file):
    with open("tasks.txt", 'w') as new_task_file:
        for dictionary in tasks_file:
            new_task_file.write("\n")
            for key, val in dictionary.items():
                new_task_file.write("{},{},".format(key, ''.join(val)))

# Allows admin only to display statistics through admin menu
def display_statistics():
    tasks_file = retrieve_tasks()
    num_users = (len(normal_user_store().keys()) + len(admin_user_store().keys()))
    num_tasks = len(tasks_file)
    print("\n\t\t------------Statistics-------------")
    print("\n\t\t-----------------------------------")
    print(f"\n\t\tNumber of users: \t\t {num_users}")
    print(f"\n\t\tNumber of tasks: \t\t {num_tasks}")
    print("\n\t\t-----------------------------------")  
    admin_options()  

# Allows admin only to generate reports through admin menu
# Reports generated to two .txt files "task_overview" and "user_overview"
def generate_reports():
    global current_user
    admins = admin_user_store()
    normal_users = normal_user_store()
    all_users = dict(normal_users, **admins)
    tasks_list = retrieve_tasks_status()

    if len(tasks_list) == 0:
        print("\n\tThere are currently no tasks.\
              \n\tPlease assign some tasks through the main main")
        main_menu()

    today = datetime.today()
    task_total = len(tasks_list)
    completed_tasks = sum(task['completed'] for task in tasks_list)
    incompleted_tasks = task_total - completed_tasks
    tasks_overdue = sum(datetime.strptime(task['due date'], DATETIME_STRING_FORMAT) < today and not task['completed'] for task in tasks_list)
    
    percent_incomplete = (incompleted_tasks / task_total) * 100
    percent_overdue = (tasks_overdue / task_total) * 100
    total_count = len(all_users)

    with open("task_overview.txt", 'w') as task_overview:
        task_overview.write(f"\n----------TASK OVERVIEW----------")
        task_overview.write(f"\n\n\nTotal Tasks managed: {task_total}")
        task_overview.write(f"\n\nTotal Completed tasks: {completed_tasks}")
        task_overview.write(f"\n\nTotal Incomplete tasks: {incompleted_tasks}")
        task_overview.write(f"\n\n\nTotal Overdue tasks: {tasks_overdue}")
        task_overview.write(f"\n\nIncomplete tasks (%): {percent_incomplete}")
        task_overview.write(f"\n\nTasks Overdue (%): {percent_overdue}")
        task_overview.write(f"\n\n\n----------END OF REPORT----------")

    print("Report generated successfully")

    with open("user_overview.txt", 'w') as user_overview:
        
        user_overview.write(f"\n----------USER OVERVIEW REPORT----------")
        user_overview.write(f"\n\n\nTotal number of registered users: {total_count}")
        user_overview.write(f"\n\nTotal number of registered tasks: {task_total}")
        
        for user, i in all_users.items():
            users_tasks = [task for task in tasks_list if task['assigned to'] == user]
            users_all_tasks = len(users_tasks)
            users_incompleted_tasks = sum(not task['completed'] for task in users_tasks)
            users_completed_tasks = users_all_tasks - users_incompleted_tasks
            users_overdue_tasks = sum(datetime.strptime(task['due date'], DATETIME_STRING_FORMAT) < today\
                                       and not task['completed'] for task in users_tasks)
            percent_users_tasks = (users_all_tasks / task_total) * 100 if task_total > 0 else 0
            percent_users_completed = (users_completed_tasks / users_all_tasks) * 100 if users_all_tasks > 0 else 0
            percent_users_incompleted = (users_incompleted_tasks / users_all_tasks) * 100 if users_all_tasks > 0 else 0
            percent_users_overdue = (users_overdue_tasks / users_all_tasks) * 100 if users_all_tasks > 0 else 0

            user_overview.write(f"\n\n\n\nUser: {user}")
            user_overview.write(f"\n\nTotal of tasks assigned: {users_all_tasks}\t\t{percent_users_tasks}% of all tasks")
            user_overview.write(f"\n\nCompleted tasks: {percent_users_completed}%")
            user_overview.write(f"\n\nIncomplete tasks: {percent_users_incompleted}%")
            user_overview.write(f"\n\nOverdue tasks: {percent_users_overdue}%")
        
        user_overview.write(f"\n\n\n----------END OF REPORT----------")

# Starts the program
task_manager()
