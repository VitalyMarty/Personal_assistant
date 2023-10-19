import pickle
from contextlib import suppress


VERSION = 'v.0.0.1'
FILENAME_ADDRESSBOOK = 'test_addressbook.pickle'
FILENAME_NOTEBOOK = 'test_notebook.pickle'


class Storage:
    def save(self):
        pass

    def load(self):
        pass


class PickleStorage(Storage):

    def __init__(self, filename: str) -> str:
        self.filename = filename

    def save(self, object):
        with open(self.filename, 'wb') as fh:
            pickle.dump(object, fh)
    
    def load(self) -> object:
        with suppress(FileNotFoundError):
            with open(self.filename, 'rb') as fh:
                object = pickle.load(fh)
                return object


class Backup(Storage):

    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def save(self, object):
        return self.storage.save(object)
    
    def load(self):
        return self.storage.load()
       




       

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




