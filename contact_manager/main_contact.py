# TODO: Import ContactManager and Contact classes

from manager import ContactManager
from contact import Contact

def main():
    manager = ContactManager()
    manager.load_from_file("contacts.txt")

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search\n4. Delete \n5. Save & Exit")
        choice = input("Option: ")

        if choice == "1":
            # TODO: Get input and add contact
            # contact = "Jane Doe", "123-456-7890", "jane@example.com")
            manager.add_contact(
                input("Enter Name: "),
                input("Enter Phone: "), 
                input("Enter Email: ")
            )

        elif choice == "2":
            # TODO: Print all contacts
            contact_list = manager.list_contacts()

            if contact_list:
                print("Contact List: ")
                for contact in contact_list:
                    print(contact)
                
        elif choice == "3":
            # TODO: Search contacts
            search_input = input("Enter search name: ")
            search_query = manager.find_contact(search_input)
            
            
            if search_query:
                for contact_name in search_query:
                    print(contact_name)
            else:
                print("Contact not found. Thank you")        


        elif choice == "4":
            # TODO: Delete contact

            search_input = input("Enter search name: ")
            search_delete_query = manager.delete_contact(search_input)

            if search_delete_query:
                print(f"{search_input.capitalize()} has been removed from list")
                print("\nUpdated contact list: ")

                for contact_name in search_delete_query:
                    print(contact_name)

            else:
                print("Contact not found. Thank you")

        elif choice == "5":
            manager.save_to_file("contacts.txt")
            print("Saved. Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
