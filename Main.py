from AddressBook import AddressBook, Record
from NoteBook import NoteBook, Note
from Fields import Name, Phone, Email, Birthday, Address
from Backup import backup_data

def main():
    contacts = AddressBook()
    notes = NoteBook()

    print("Bot assistant is running. Type 'exit' to exit.")
    while True:
        command = input("Enter a command: ")
        try:
            result = parse_command(contacts, notes, command)
            if result:
                print(result)
        except Exception as e:
            print(f"Error: {str(e)}")

def parse_command(contacts, notes, command):
    command = command.lower()
    
    if command == 'hello':
        return "How can I help you?"
    elif command.startswith('add '):
        _, data = command.split(' ', 1)
        parts = data.split()
        if len(parts) != 3:
            return "Provide name, phone, and birthday (if applicable)"
        name, phone, birthday = parts
        contacts.add_record(Record(name, birthday))
        contacts.data[name].add_phone(phone)
        return f"Added contact: {name}, {phone}, Birthday: {birthday}"
    elif command.startswith('change '):
        _, data = command.split(' ', 1)
        if ' ' not in data:
            return "Provide name and phone please"
        name, phone = data.split()
        contact = contacts.find(name)
        if contact:
            contact.edit_phone(contact.phones[0].value, phone)
            return f"Updated contact: {name}, {phone}"
        else:
            raise ValueError(f"Contact '{name}' not found.")
    elif command.startswith('phone '):
        *_, name = command.split(' ')
        contact = contacts.find(name)
        if contact:
            return f"Phone number for {name}: {contact.phones[0].value}"
        else:
            raise ValueError(f"Contact '{name}' not found.")
    elif command.startswith('search '):
        _, query = command.split(' ', 1)
        results = contacts.search(query)
        if results:
            return "\n".join([str(record) for record in results])
        else:
            return "No matching contacts found."
    elif command.startswith('add contact '):
        _, data = command.split(' ', 2)
        name, phone, birthday = data.split()
        contacts.add_record(Record(name, birthday))
        contacts.data[name].add_phone(phone)
        return f"Added contact: {name}, {phone}, Birthday: {birthday}"
    elif command.startswith('add note '):
        _, data = command.split(' ', 2)
        title, content, tags = data.split()
        note = Note(title, content)
        note.add_tags(tags.split(','))
        notes.add_note(note)
        return f"Added note: {title}, Tags: {', '.join(note.tags)}"
    elif command.startswith('edit note '):
        _, title, content, tags = command.split(' ', 3)
        note = notes.find(title)
        if note:
            note.edit_content(content)
            note.clear_tags()
            note.add_tags(tags.split(','))
            return f"Updated note: {title}, Tags: {', '.join(note.tags)}"
        else:
            return f"Note '{title}' not found."
    elif command.startswith('delete note '):
        _, title = command.split(' ', 1)
        notes.delete(title)
        return f"Deleted note: {title}"
    elif command.startswith('list contacts'):
        return "\n".join([str(record) for record in contacts])
    elif command.startswith('list notes'):
        return "\n".join([str(note) for note in notes])
    elif command in ['good bye', 'close', 'exit']:
        print("Good bye!")
        backup_data(contacts, notes)
        exit()
    elif command in ['add', 'change']:
        return "Provide name and phone please"
    elif command == 'phone':
        return "Provide name please"
    else:
        return "Unknown command."

if __name__ == "__main__":
    main()



# command_dict = {
#     'hello': "How can I help you?",
#     'add contact': "Add a contact to the address book",
#     'add note': "Add a note to the notebook",
#     'change contact': "Change contact information",
#     'edit note': "Edit a note",
#     'delete note': "Delete a note",
#     'list contacts': "List all contacts",
#     'list notes': "List all notes",
#     'good bye': "Exit the program",
# }

# completer = WordCompleter(command_dict.keys())