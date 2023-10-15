import AddressBook
import NoteBook

get_help = {
    'hello': "How can I help you?",
    'add': "Add a contact to the address book (usage: add name phone birthday)",
    'change': "Change contact information (usage: change name phone)",
    'phone': "Get the phone number for a contact (usage: phone name)",
    'search': "Search for contacts (usage: search query)",
    'add_note': "Add a note to the notebook (usage: add_note title content tags)",
    'edit_note': "Edit a note (usage: edit_note title content tags)",
    'delete_note': "Delete a note (usage: delete_note title)",
    'list_contacts': "List all contacts",
    'list_notes': "List all notes",
    'goodbye': "Exit the program",
}

def main():
    contacts = AddressBook()
    notes = NoteBook()

    print("Bot assistant is running. Type 'help' to view commands. Type 'exit' to exit.")
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
    command_parts = command.split()

    if command == 'hello':
        return "How can I help you?"
    
    elif command.startswith('add '):
        _, data = command.split(' ', 1)
        parts = data.split()
        if len(parts) != 3:
            return "Provide name, phone, and birthday (if applicable)"
        name, phone, birthday = parts
        return AddressBook.add_contact(contacts, name, phone, birthday)
    
    elif command.startswith('change '):
        _, data = command.split(' ', 1)
        if len(command_parts) != 3:
            return "Provide name and phone please"
        name, phone = data.split()
        return AddressBook.change_contact(contacts, name, phone)
    
    elif command.startswith('phone '):
        if len(command_parts) != 2:
            return "Provide name please"
        name = command_parts[1]
        return AddressBook.get_phone(contacts, name)
    
    elif command.startswith('search '):
        _, query = command.split(' ', 1)
        return AddressBook.search_contacts(contacts, query)
    
    elif command.startswith('add_note '):
        _, data = command.split(' ', 1)
        title, content, tags = data.split()
        return NoteBook.add_note(notes, title, content, tags)
    
    elif command.startswith('edit_note '):
        _, data = command.split(' ', 1)
        title, content, tags = data.split()
        return NoteBook.edit_note(notes, title, content, tags)
    
    elif command.startswith('delete_note '):
        if len(command_parts) != 2:
            return "Provide the title of the note to delete"
        title = command_parts[1]
        return NoteBook.delete_note(notes, title)
    
    elif command == 'list_contacts':
        return AddressBook.list_contacts(contacts)
    
    elif command == 'list_notes':
        return NoteBook.list_notes(notes)
    
    elif command in ['goodbye', 'close', 'exit']:
        print("Good bye!")
        AddressBook.backup_data(contacts)
        NoteBook.backup_data(notes)
        exit()
        
    elif command == 'help':
        return get_help_text()

    return "Unknown command."

def get_help_text():
    help_text = "Available commands:\n"
    for command, description in get_help.items():
        help_text += f"{command}: {description}\n"
    return help_text

if __name__ == "__main__":
    main()


# completer = WordCompleter(command_dict.keys())