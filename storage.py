import json

def save_contacts(contacts):
    with open('contact.json','w') as file:
        json.dump(contacts,file, indent=1)

def load_contacts():
    with open('contact.json','r') as file:
        return json.load(file)
