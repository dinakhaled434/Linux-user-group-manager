import subprocess

# Function to add a new user
def add_user():
    username = input("Enter username: ")
    subprocess.run(["sudo", "useradd", username])

# Function to modify an existing user by changing the username
def modify_user():
    username = input("Enter username: ")
    newname = input("Enter new username: ")
    subprocess.run(["sudo", "usermod", "-l", newname, username])

# Function to delete a user from the system
def delete_user():
    username = input("Enter username: ")
    subprocess.run(["sudo", "userdel", username])

# Function to list all system users
def list_users():
    subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"])

# Function to add a new group
def add_group():
    group = input("Enter group name: ")
    subprocess.run(["sudo", "groupadd", group])

# Function to modify group members
def modify_group():
    group = input("Enter group name: ")

    print("Current group members:")
    subprocess.run(["getent", "group", group])

    user = input("Enter username to add to group: ")
    subprocess.run(["sudo", "usermod", "-aG", group, user])

# Function to delete a group
def delete_group():
    group = input("Enter group name: ")
    subprocess.run(["sudo", "groupdel", group])

# Function to list all groups
def list_groups():
    subprocess.run(["cut", "-d:", "-f1", "/etc/group"])

# Function to disable (lock) a user account
def disable_user():
    username = input("Enter username: ")
    subprocess.run(["sudo", "usermod", "-L", username])

# Function to enable a user account using -p option
def enable_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    subprocess.run(["sudo", "usermod", "-p", password, username])

# Function to change the password of a user
def change_password():
    username = input("Enter username: ")
    subprocess.run(["sudo", "passwd", username])

# Function to display information about the program
def about():
    print("\nUser and Group Management Tool")
    print("This program allows administrators to manage Linux users and groups.")
    print("You can add, modify, delete users and groups,")
    print("enable or disable user accounts, and change passwords.")

# Main program loop
while True:

    # Display the menu
    print("\nMain Menu")
    print("1. Add User")
    print("2. Modify User")
    print("3. Delete User")
    print("4. List Users")
    print("5. Add Group")
    print("6. Modify Group")
    print("7. Delete Group")
    print("8. List Groups")
    print("9. Disable User")
    print("10. Enable User")
    print("11. Change Password")
    print("12. About")
    print("0. Exit")

    # Read user choice
    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        modify_user()

    elif choice == "3":
        delete_user()

    elif choice == "4":
        list_users()

    elif choice == "5":
        add_group()

    elif choice == "6":
        modify_group()

    elif choice == "7":
        delete_group()

    elif choice == "8":
        list_groups()

    elif choice == "9":
        disable_user()

    elif choice == "10":
        enable_user()

    elif choice == "11":
        change_password()

    elif choice == "12":
        about()

    elif choice == "0":
        break

    else:
        print("Invalid choice")