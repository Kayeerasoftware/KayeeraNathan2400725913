contacts = []


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    print("Contact Added Successfully!")


def view_contacts():

    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 20)


def search_contact():

    search_name = input("Enter name to search: ")

    for contact in contacts:

        if contact["name"].lower() == search_name.lower():
            print("\nContact Found")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return

    print("Contact not found.")


def delete_contact():

    name = input("Enter name to delete: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def menu():

    while True:

        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Try again.")


menu()
print()
print()