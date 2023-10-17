from AddressBook import Record, contacts
from NoteBook import notes

def add_contact(name):
    """'add phone <name>' Добавити контакт"""
    record = Record(name)
    contacts.add_record(record)
    return f'Added contact {name} to contacts'


def change():
    """
    change phone <name> <phone>
    change birthday <name> <date>
    change address <name> <address>
    change email <name> <email>
    change note <note>
    change tag <note> <tag>

    Функція повертає:
    - Повідомлення, що <об'єкт> було змінено з <old_value> на <new_value>
    - повідомлення про помилку
"""
    pass


def delete():
    """
    delete phone <name> <phone>
    delete birthday <name> <date>
    delete address <name> <address>
    delete email <name> <email>
    delete record <name>
    delete note <note>
    delete tag <note> <tag>
    
    Функція повертає:
    -Повідомлення, що <об'єкт> було з <місце>
    -повідомлення про помилку
    """
    pass


def find():
    """
    find record <name (можна частково)>
    find record <phone (можна частково)>
    find record <birthday (можна частково)>
    find record <address (можна частково)>
    find record <email (можна частково)>
    find note <що знайти>
    find tag <tag (можна частково)>
    
    Функція повертає:
    - Записи, що відповідають критеріям пошуку.
    - Нотатки, що відповідають критеріям пошуку.
    - Повідомлення, що по таким критеріям нічого не знайдено.
    - повідомлення про помилку
    """
    pass


def get_help():
    """Show available commands"""
    message = 'I can do next commands:\n'
    for count, command in enumerate(command_dict, start=1):
        if count <= 9:
            count = f'0{count}'
        message = '\n'.join([message, f'{count}. {command:<17}-{command_dict[command].__doc__}'])

    return message


def find_birthdays_in_x_days(days):
    matching_contacts = ''
    dict_contacts = contacts.check_birthday(days)
    for name in dict_contacts:
        row = f'{name} - {dict_contacts[name]} days'
        '\n'.join([matching_contacts, row])
        
    return matching_contacts

    

def goodbye():
    """Exit the program"""
    return f'Good Bye!'


def hello():
    """How can I help you?"""
    return f'How can I help you?'


def sort_dir():
    """
    sort <path dir>

    Функція виконує:
    - Сортує <path dir>

    Функція повертає:
    - Повідомлення про те що <path dir> відсортовано
    - Повідомлення, що такої папки не існує
    """
    pass


def show_contacts():
    """Вивести всі збереженні контакти"""
    return contacts.show_contacts()


command_dict ={
    'hello': hello,
    'exit': goodbye,
    'close': goodbye,
    'good bye': goodbye,
    'help': get_help,
    'congratulate': find_birthdays_in_x_days,
    'add contact': add_contact,
    'add address': None,
    'add phone': None,
    'add email': None,
    'add birthday': None,
    'change address': None,
    'change phone': None,
    'change email': None,
    'change birthday': None,
    'change name': None,
    'find contact': contacts.find,
    'delete contact': contacts.delete,
    'show contacts': None,
    'add note': None,
    'find note': None,
    'change note': None,
    'delete note': None,
    'add tag': None,
    'sort notes': None,
    'sort dir': None,
    'make file': None
}
