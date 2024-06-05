# Contact Book by updating,deleting,searching and displaying contacts using python
contacts = {}
def add_contact(name, phone, email, address):
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully!")

def display_contacts():
    if not contacts:
        print("No contacts to display!")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

def search_contact(name):
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print(f"No contact found with the name {name}.")

print('\n-----------------------------------------------------')
while True:
        print("\nContact Book Menu")
        print("\n1. Add Contact")
        print("2. Display Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif option == '2':
            display_contacts()
        elif option == '3':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif option == '4':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)
        elif option == '5':
            print("Exiting Contact Book. See you soon!")
            break
        else:
            print(" Please try a valid option again!")
            print('\n----------------------------------------------------')
print('\n--------------------------------------------------------------')
