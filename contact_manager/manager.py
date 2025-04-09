# TODO: Import Contact class

from math import remainder
from contact import Contact

class ContactManager:
    def __init__(self):
        # TODO: Create a list to store contacts
        self.contact_list = []

    def add_contact(self, name, phone, email):
        # TODO: Add contact to the list
        contacts = Contact(name, phone, email)
        self.contact_list.append(contacts)

    def list_contacts(self):
        # TODO: Return list of all contacts
        
        return self.contact_list

    def find_contact(self, name):
        # TODO: Return contacts matching search query
        result_found = []

        for contact in self.contact_list:
            if name.lower() in contact.name.lower():
                result_found.append(contact.name)
        
        return result_found

    def delete_contact(self, name):
        # TODO: Remove contacts matching the name

        for contact in self.contact_list:
            if name.lower() in contact.name.lower():
                self.contact_list.remove(contact)
                return self.contact_list


    def save_to_file(self, filename):
        # TODO: Write contacts to file

        with open(filename, "w") as file:
            for contacts in self.contact_list:

                file.write(f"{contacts.name} | Phone: {contacts.phone} | Email: {contacts.email}\n")

    def load_from_file(self, filename):
        # TODO: Load contacts from file
        try:

         with open(filename, "r") as file:
            for existing_contact in file:
                existing_contact = existing_contact.strip()
                parts = existing_contact.split('|')

                if len(parts) == 3:
                    name_part = parts[0].strip()
                    phone_part = parts[1].replace("Phone:", "").strip()
                    email_part = parts[2].replace("Email:", "").strip()
                    contact = Contact(name_part, phone_part, email_part)
                    self.contact_list.append(contact)

        except FileNotFoundError:
            print(f'No previous contact list foudn at {filename}. Starting with an empty list')
        except Exception as e:
            print(f'An error occured while loading contacts: {e}')


