
from storage import*

def add_contact(name,phone,email,address):
    contacts =load_contacts()
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    save_contacts(contacts)

def view_contacts():
    contacts=load_contacts()
    print("\n Contact List")
    for i,contact in enumerate (contacts,start=1):
        print((f"{i}, Name : {contact['name']}, Phone : {contact['phone']}, Email : {contact['email']}, Address : {contact['address']}"))


def remove_contact(index):
    contacts=load_contacts()
    if 0< index <= len(contacts):
        del contacts[index-1]
        save_contacts(contacts)



def search_contact(query):
    contacts=load_contacts()
    results=[]
    for contact in contacts:
        if query.lower() in contact['name']:
            results.append(contact)
    print("\n search result")
    for i, contact in enumerate(results, start=1):
        print((f"{i}, Name : {contact['name']}, Phone : {contact['phone']}, Email : {contact['email']}, Address : {contact['address']}"))
def update_contact(index):
    contacts=load_contacts()
    if 0< index <= len(contacts):
        contact = contacts[index]

        print(f"\nUpdating {contact['name']} by {contact['phone']}")

        contact['name'] = input(f"Enter new name (current: {contact['name']}): ")
        contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ")
        contact['email'] = input(f"Enter new email Address (current: {contact['email']}): ")
        contact['address'] = input(f"Enter new address (current: {contact['address']}): ")

        save_contacts(contacts)
    else:
        print("Invalid Input")