import os

from address_book import storage_addressbook, contacts
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


    completer = WordCompleter(command_dict, ignore_case=True)
    try:
        while True:
            
            # Запит у користувача, що зробити
            user_input = prompt("\nType 'help' to view available commands. Type 'exit' to exit.\n>>> ", completer=completer)

            # Обробка команди від користувача
            result = parse_input(user_input)

            #TODO Прибрати коментар та включити функцію очищення екрану перед виведенням іншого результату
            # os.system('cls')
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
