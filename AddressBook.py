from Fields import Address, Email, Fields, Birthday, Name, Phone  
from datetime import date
import pickle


class AddressBook(Fields):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.load_data()

    def add_record(self, record):
        self.data[record.name.value] = record
        self.save_data()

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            self.save_data()

    def iterator(self, chunk_size=10):
        record_names = list(self.data.keys())
        num_records = len(record_names)
        current_index = 0

        while current_index < num_records:
            end_index = current_index + chunk_size
            records_chunk = [self.data[record_name] for record_name in record_names[current_index:end_index]]
            yield records_chunk
            current_index = end_index

    def save_data(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            self.data = {}



class Record:
    def __init__(self, name:str, phone:str=None, birthday:str=None):
        self.name = Name(name)
        self.phones = []
        self.address = None  
        self.email = None  

        if phone is not None:
            self.add_phone(phone)

        if birthday is not None:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = Birthday(None)
        
    # Реалізація класу
    def add_address(self, address: str):
        self.address = Address(address)

    def edit_address(self, new_address: str):
        if self.address is not None:
            self.address.value = new_address
        else:
            raise ValueError("No address to edit.")

    def remove_address(self):
        self.address = None

    def add_email(self, email: str):
        self.email = Email(email)

    def edit_email(self, new_email: str):
        if self.email is not None:
            self.email.value = new_email
        else:
            raise ValueError("No email to edit.")

    def remove_email(self):
        self.email = None
        
    def add_phone(self, number: str)-> None:
        self.phones.append(Phone(number))

    def edit_phone(self, old_phone: str, new_phone: str)-> None:
        is_edited = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                is_edited = True

        # Якщо номера не існує, то викликається помилка  
        if not is_edited:
            raise ValueError(f'Phone number - {old_phone} is not exist in contact: {self.name}')    

    def find_phone(self, find_phone: str)-> Phone:
        for indx, phone in enumerate(self.phones):
            if phone.value == find_phone:
                return self.phones[indx]
            
    def find_address(self, find_address: str):
        if self.address == find_address:
            return self.address

    def find_email(self, find_email: str):
        if self.email == find_email:
            return self.email
            
    def remove_phone(self, remove_phone)-> None:
        for indx, phone in enumerate(self.phones):
            if phone.value == remove_phone:
                del self.phones[indx]

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def edit_birthday(self, new_birthday: str):
        self.birthday.value = new_birthday

    def remove_birthday(self):
        self.birthday.value = None

    def days_to_birthday(self):
        if self.birthday.value == '':
            return None
        today = date.today()
        actual_birthday = self.birthday.value.replace(year=today.year)
        if actual_birthday < today:
            actual_birthday = self.birthday.value.replace(year=today.year+1)
        time_to_birthday = abs(actual_birthday - today)

        return time_to_birthday.days
    
    def __str__(self) -> str:
        days = str(self.days_to_birthday())
        return f" Contact name: {self.name.value:<10} birthday: {str(self.birthday):<11}({days:<4} days) phones: {'; '.join(p.value for p in self.phones)}"
    
    def __repr__(self) -> str:
        self.phones_repr = ', '.join([phone.value for phone in self.phones])
        return f'Record({self.name.value}, {self.phones_repr}, {self.birthday.value})'
    


