from address_book import contacts
from note_book import notes


def add():
    """
    add phone <name> <phone>
    add birthday <name> <date>
    add address <name> <address>
    add email <name> <email>
    add note <note>
    add tag <note> <tag>
    
    Функція повертає:
    - Повідомлення, що <об'єкт> було добавлено в <місце>
    - повідомлення про помилку
    """
    pass


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


# def get_next_birthday():
#     """
#     birthday <name (можна частково)>
    
#     Функція повертає:
#     - Кількість днів до наступного дня народження, якщо в записі вказано день народження.
#     - Повідомлення, що для такого запису еднь народження не задано
#     - Повідомлення, що такого запису <name> не існує.
    
#     Якщо реалізовувати частковий пошук, то мабуть треба щоб виводило перелік записів, що відповідають критерію.
#     """
#     pass

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


def show_all():
    """
    Користувач вводить наступні команди через пробіл:
    show all
    
    Функція повертає:   
    - всі збереженні контакти з номерами телефонів у консоль.
    """
    pass


command_dict ={
    'hello': hello,
    'exit': goodbye,
    'close': goodbye,
    'good bye': goodbye,
    'help': get_help,
    'find in contacts': contacts.find_in_records,
    'congratulate': find_birthdays_in_x_days,
    'add contact': contacts.add_record,
    'add address': contacts.add_address_to_record,
    'add phone': contacts.add_phone_to_record,
    'add email': contacts.add_email_to_record,
    'add birthday': contacts.add_birthday_to_record,
    'edit address': contacts.edit_address_in_record,
    'edit phone': contacts.edit_phone_in_record,
    'edit email': contacts.edit_email_in_record,
    'edit birthday': contacts.edit_birthday_in_record,
    'edit name': contacts.edit_name_in_record,
    'find contact': contacts.find_record,
    'delete contact': contacts.delete_record,
    'delete address': contacts.delete_address_from_record,
    'delete phone': contacts.delete_phone_from_record,
    'delete email': contacts.delete_email_from_record,
    'delete birthday': contacts.delete_birthday_from_record,
    'show contacts': contacts.show_contacts,
    'add note': None,
    'find note': None,
    'change note': None,
    'delete note': None,
    'add tag': None,
    'sort notes': None,
    'sort dir': None,
    'make file': None
}
