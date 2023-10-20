import os

from address_book import storage_addressbook, contacts, VERSION
from note_book import storage_notebook, notes
from commands import command_dict
from decorators import input_error


from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog

@input_error
def parse_input(user_input: str) -> str:
    new_input = user_input
    data = ''
    for key in command_dict:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):].split()
            break
    if data:
        return handler(new_input)(*data)
    return handler(new_input)()


def break_func():
    """
    Якщо користувач ввів команду якої немає в command_dict, то повертаємо повідомлення
    """
    return 'Wrong command!'


def handler(command):
    return command_dict.get(command, break_func)


def main():

    print('{:<15} {}\n{:<15} {}\n{:<15} {}\n'.format('Tough Assistant', VERSION, 'AddressBook', contacts.version, 'NoteBook', notes.version))


    completer = WordCompleter(command_dict, ignore_case=True)
    try:
        while True:
            
            # User request for action
            user_input = prompt("Type 'help' to view available commands. Type 'exit' to exit.\n>>> ", completer=completer)

            # Processing user command
            result = parse_input(user_input)

            # os.system('cls')
            # Displaying the result of command processing
            print(f'{result}\n------\n')
            # Termination condition. The user should enter a command: close | exit | good bye
            if result == 'Good Bye!':
                break
    finally:
        # Upon completion, we save the contacts and notes.
        storage_addressbook.save(contacts)
        storage_notebook.save(notes)
        print(f'Contacts saved to file: {storage_addressbook.storage.filename}')
        print(f'Notes saved to file: {storage_addressbook.storage.filename}')



if __name__ == "__main__":
    main()
