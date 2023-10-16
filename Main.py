from AddressBook import AddressBook
from Backup import Backup, PickleStorage
from Commands import command_dict
from NoteBook import Notebook

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog


def parse_input(user_input: str) -> str:
    new_input = user_input
    data = ''
    for key in command_dict:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):].split()
            break
    if data:
        return handler(new_input)(data)
    return handler(new_input)()


def break_func():
    """
    Якщо користувач ввів команду якої немає в command_dict, то повертаємо повідомлення
    """
    return 'Wrong command!'


def handler(command):
    return command_dict.get(command, break_func)


def main():

    # Створюємо сховище, де зберігається файл з контактами та нотатками
    storage_addressbook = Backup(PickleStorage('test_addressbook.pickle'))
    storage_notebook = Backup(PickleStorage('test_notebook.pickle'))


    # Завантажуємо контакти та нотатки з файлів. Якщо файли відсутні створюємо нові.
    contacts = AddressBook() if storage_addressbook.load() is None else storage_addressbook.load()
    notes = Notebook() if storage_addressbook.load() is None else storage_addressbook.load()

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



if __name__ == "__main__":
    main()
