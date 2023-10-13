import pickle

def save_address_book(address_book, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(address_book, file)
def load_address_book(file_name):
    try:
        with open(file_name, 'rb') as file:
            address_book = pickle.load(file)
        return address_book
    except FileNotFoundError:
        # Повернути новий об'єкт адресної книги, якщо файл не знайдено.
        return addressbook()
