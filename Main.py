from AddressBook import storage_addressbook, contacts
from NoteBook import storage_notebook, notes
from Commands import command_dict
from Parser import parse_input


from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog


def main():


    completer = WordCompleter(command_dict, ignore_case=True)
    try:
        while True:
            
            # Запит у користувача, що зробити
            user_input = prompt("\nType 'help' to view available commands. Type 'exit' to exit.\n>>> ", completer=completer)

            # Обробка команди від користувача
            result = parse_input(user_input)

            # Вивід результату обробки команди
            print(result)

            # Умова завершення роботи. Користувач повинен ввести команду: close | exit | good bye
            if result == 'Good Bye!':
                break
    finally:
        # При завершенні роботи зберігаємо contacts та notes
        storage_addressbook.save(contacts)
        storage_notebook.save(notes)
        print(f'Contacts saved to file: {storage_addressbook.storage.filename}')
        print(f'Notes saved to file: {storage_addressbook.storage.filename}')



if __name__ == "__main__":
    main()
