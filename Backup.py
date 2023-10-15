import pickle

# def save_address_book(address_book, file_name):
#     with open(file_name, 'wb') as file:
#         pickle.dump(address_book, file)
# def load_address_book(file_name):
#     try:
#         with open(file_name, 'rb') as file:
#             address_book = pickle.load(file)
#         return address_book
#     except FileNotFoundError:
#         # Повернути новий об'єкт адресної книги, якщо файл не знайдено.
#         return addressbook()

class Storage:
    def save(self):
        pass

    def load(self):
        pass


class PickleStorage(Storage):

    def __init__(self, filename: str) -> str:
        self.filename = filename

    def save_object(self, object):
        with open(self.filename, 'wb') as fh:
            pickle.dump(object, fh)
    
    def load_object(self) -> object:
        with open(self.filename, 'rb') as fh:
            object = pickle.load(fh)
        return object
    

class Backup(Storage):

    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def save(self, object):
        return self.storage.save_object(object)
    def load(self):
        return self.storage.load_object()
    

"""
Що необхідно зробити:
1. Модуль main
    1.1. Замінити

            contacts = AddressBook("contacts.txt")
            notes = Notebook("notes.txt")

        на
            storage_addressbook = Backup(PickleStorage('addressbook.pickle'))
            storage_notebook = Backup(PickleStorage('notebook.pickle'))

            try:
                contacts = storage_addressbook.load()
                notebook = storage_notebook.load()
            except FileNotFoundError:
                contacts = AddressBook()
                notes = Notebook()
    
    1.2. До try-except в циклі while додати:

            finally:
                storage_addressbook.save(contacts)
                storage_notebook.save(notes) 
"""

    

# TODO Видалити коли буде не потрібно   
# Це тестовий if для перевірки працездатності коду. 
if __name__ == "__main__":

    class Test:
        def __init__(self):
            self.test = 10

    storage_addressbook = Backup(PickleStorage('addressbook.pickle'))
    storage_notebook = Backup(PickleStorage('notebook.pickle'))

    object1 = Test()
    object2 = Test()
    object2.test = 20

    print(object1.test)
    print(object2.test)

    storage_addressbook.save(object1)
    storage_notebook.save(object2)

    copy_object1 = storage_addressbook.load()
    copy_object2 = storage_notebook.load()

    print(copy_object1.test)
    print(copy_object2.test)




