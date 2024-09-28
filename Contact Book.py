# Simple Contact Book Application

# A list to store contacts
contacts = []

def display_contacts():
    # Display the list of contacts
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}")

def add_contact():
    # Add a new contact
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    # Create a contact dictionary and append it to the contacts list
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def search_contact():
    # Search for a contact by name or phone number
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [c for c in contacts if search_term in c['name'] or search_term in c['phone']]
    
    if found_contacts:
        print("\n--- Search Results ---")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found matching that search term.")

def update_contact():
    # Update an existing contact
    display_contacts()
    if not contacts:
        return  # No contacts to update

    try:
        index = int(input("Enter the number of the contact to update: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return
        
        # Get new details
        name = input("Enter new name (leave blank to keep current): ")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")

        # Update contact details if not blank
        if name:
            contacts[index]['name'] = name
        if phone:
            contacts[index]['phone'] = phone
        if email:
            contacts[index]['email'] = email
        if address:
            contacts[index]['address'] = address

        print("Contact updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact():
    # Delete a contact
    display_contacts()
    if not contacts:
        return  # No contacts to delete

    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return

        deleted_contact = contacts.pop(index)
        print(f"Contact {deleted_contact['name']} deleted successfully!")

    except ValueError:
        print("Invalid input. Please enter a number.")

def main_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the Contact Book application
main_menu()
