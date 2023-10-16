from AddressBook import AddressBook
from NoteBook import Notebook
from Backup import Backup, PickleStorage


# def main():
#     contacts = AddressBook("contacts.txt")
#     notes = Notebook("notes.txt")

#     print("Bot assistant is running.")
#     while True:
#         command = input("Type 'help' to view available commands. Type 'exit' to exit.\nEnter a command: ")
#         try:
#             command_name, command_args = parse_command(contacts, notes, command)
#             if command_name:
#                 result = execute_command(command_name, *command_args)
#                 if result:
#                     print(result)
#         except Exception as e:
#             print(f"Error: {str(e)}")

# def print_available_commands():
#     print("Available commands:")
#     print("hello: How can I help you?")
#     print("add: Add a contact to the address book (usage: add name phone birthday)")
#     print("change: Change contact information (usage: change name phone)")
#     print("phone: Get the phone number for a contact (usage: phone name)")
#     print("search: Search for contacts (usage: search query)")
#     print("add_note: Add a note to the notebook (usage: add_note title content tags)")
#     print("edit_note: Edit a note (usage: edit_note title content tags)")
#     print("delete_note: Delete a note (usage: delete_note title)")
#     print("list_contacts: List all contacts")
#     print("list_notes: List all notes")
#     print("goodbye: Exit the program")

# def parse_command(contacts, notes, command):
#     command = command.lower()
#     command_parts = command.split()

#     if command == 'hello':
#         return "hello", ()
    
#     elif command.startswith('add '):
#         _, data = command.split(' ', 1)
#         parts = data.split()
#         if len(parts) != 3:
#             return None, ()
#         name, phone, birthday = parts
#         return "add", (contacts, name, phone, birthday)
    
#     elif command.startswith('change '):
#         _, data = command.split(' ', 1)
#         if len(command_parts) != 3:
#             return None, ()
#         name, phone = data.split()
#         return "change", (contacts, name, phone)
    
#     elif command.startswith('phone '):
#         if len(command_parts) != 2:
#             return None, ()
#         name = command_parts[1]
#         return "phone", (contacts, name)
    
#     elif command.startswith('search '):
#         _, query = command.split(' ', 1)
#         return "search", (contacts, query)
    
#     elif command.startswith('add_note '):
#         _, data = command.split(' ', 1)
#         title, content, tags = data.split()
#         return "add_note", (notes, title, content, tags)
    
#     elif command.startswith('edit_note '):
#         _, data = command.split(' ', 1)
#         title, content, tags = data.split()
#         return "edit_note", (notes, title, content, tags)
    
#     elif command.startswith('delete_note '):
#         if len(command_parts) != 2:
#             return None, ()
#         title = command_parts[1]
#         return "delete_note", (notes, title)
    
#     elif command == 'list_contacts':
#         return "list_contacts", (contacts,)
    
#     elif command == 'list_notes':
#         return "list_notes", (notes,)
    
#     elif command in ['goodbye', 'close', 'exit']:
#         print("Good bye!")
#         AddressBook.backup_data(contacts)
#         Notebook.backup_data(notes)
#         exit()
        
#     elif command == 'help':
#         print_available_commands()
#         return None, ()
    
#     return "Unknown command.", ()

# def execute_command(command_name, *command_args):
#     if command_name == "hello":
#         return "How can I help you?"
    
#     elif command_name == "add":
#         contacts, name, phone, birthday = command_args
#         return AddressBook.add_contact(contacts, name, phone, birthday)
    
#     elif command_name == "change":
#         contacts, name, phone = command_args
#         return AddressBook.change_contact(contacts, name, phone)
    
#     elif command_name == "phone":
#         contacts, name = command_args
#         return AddressBook.get_phone(contacts, name)
    
#     elif command_name == "search":
#         contacts, query = command_args
#         return AddressBook.search_contacts(contacts, query)
    
#     elif command_name == "add_note":
#         notes, title, content, tags = command_args
#         return Notebook.add_note(notes, title, content, tags)
    
#     elif command_name == "edit_note":
#         notes, title, content, tags = command_args
#         return Notebook.edit_note(notes, title, content, tags)
    
#     elif command_name == "delete_note":
#         notes, title = command_args
#         return Notebook.delete_note(notes, title)
    
#     elif command_name == "list_contacts":
#         contacts = command_args[0]
#         return AddressBook.list_contacts(contacts)
    
#     elif command_name == "list_notes":
#         notes = command_args[0]
#         return Notebook.list_notes(notes)

def parse_input(user_input: str) -> str:



def main():

    storage_addressbook = Backup(PickleStorage('addressbook.pickle'))
    storage_notebook = Backup(PickleStorage('notebook.pickle'))

    contacts = AddressBook() if storage_addressbook.load() is None else storage_addressbook.load()
    notes = Notebook() if storage_addressbook.load() is None else storage_addressbook.load()

    try:
        while True:

            user_input = input("\nType 'help' to view available commands. Type 'exit' to exit.\n>>> ")
        
            result = None



            if result == 'Good Bye!':
                break
    except:
        pass
    finally:
        storage_addressbook.save(contacts)
        storage_notebook.save(notes)



if __name__ == "__main__":
    main()



# completer = WordCompleter(command_dict.keys())