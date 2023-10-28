import json

# Initialize an empty dictionary to store passwords
passwords = {}

# Function to add a new password
def add_password(account, username, password):
    if account in passwords:
        print(f"An entry for {account} already exists.")
    else:
        passwords[account] = {'username': username, 'password': password}
        save_passwords()
        print(f"Password for {account} added successfully.")

# Function to retrieve a password
def get_password(account):
    if account in passwords:
        return passwords[account]['password']
    else:
        return None

# Function to list all stored accounts
def list_accounts():
    if passwords:
        print("Stored Accounts:")
        for account in passwords.keys():
            print(account)
    else:
        print("No accounts stored.")

# Function to save passwords to a file
def save_passwords():
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

# Function to load passwords from a file
def load_passwords():
    global passwords
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

# Load existing passwords on startup
load_passwords()

# Main loop for command-line interface
while True:
    print("\nMenu:")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. List Accounts")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        account = input("Enter the account name: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        add_password(account, username, password)
    elif choice == '2':
        account = input("Enter the account name: ")
        password = get_password(account)
        if password:
            print(f"The password for {account} is: {password}")
        else:
            print(f"No entry found for {account}.")
    elif choice == '3':
        list_accounts()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Save passwords before exiting
save_passwords()
