import json

# Function to load existing contacts from a file
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

# Function to save contacts to a file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

# Function to add a new contact
def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)

# Function to view all contacts
def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        add_contact(name, phone)
        print("Contact added successfully!")

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please try again later.")
