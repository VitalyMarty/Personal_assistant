from collections import UserDict
from fields_classes import Address, Birthday, Email, Name, Phone  
from datetime import date
import pickle


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, chunk_size=10):
        record_names = list(self.data.keys())
        num_records = len(record_names)
        current_index = 0

        while current_index < num_records:
            end_index = current_index + chunk_size
            records_chunk = [self.data[record_name] for record_name in record_names[current_index:end_index]]
            yield records_chunk
            current_index = end_index
            
    def check_birthday(self, target_days):
        dict_contacts = {}
        
        for contact in self.data:
            name, days = contact.days_to_birthday(target_days)  
            if name:
                dict_contacts[name] = days
                
        return dict_contacts  

    def search_contacts_by_name(self, name):
        found_contacts_by_name = []
        for record in self.data.values():
            if record.name.value.lower() == name.lower():
                found_contacts_by_name.append(record)
        return found_contacts_by_name

    def search_contacts_by_phone(self, phone):
        found_contacts_by_phone = []
        for record in self.data.values():
            for contact_phone in record.phones:
                if contact_phone.value == phone:
                    found_contacts_by_phone.append(record)
                    break
        return found_contacts_by_phone
            


class Record:
    def __init__(self, name:str, phone:str=None, birthday:str=None):
        self.name = Name(name)
        self.phones = []
        self.address = None  
        self.email = None  

        if phone:
            self.add_phone(phone)

        if birthday:
            self.add_birthday(birthday)
        
    # Реалізація класу
    def add_address(self, address: str):
        self.address = Address(address)

    def edit_address(self, new_address: str):
        if self.address:
            self.address.value = new_address
        else:
            raise ValueError("No address to edit.")

    def remove_address(self):
        self.address = None

    def add_email(self, email: str):
        self.email = Email(email)

    def edit_email(self, new_email: str):
        if self.email:
            self.email.value = new_email
        else:
            raise ValueError("No email to edit.")

    def remove_email(self):
        self.email = None
        
    def add_phone(self, number: str)-> None:
        self.phones.append(Phone(number))

    def edit_phone(self, old_phone: str, new_phone: str)-> None:
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError(f'Phone number - {old_phone} is not exist in contact: {self.name}')    

    def find_phone(self, find_phone: str)-> Phone:
        for index, phone in enumerate(self.phones):
            if phone.value == find_phone:
                return self.phones[index]
            
    def find_address(self, find_address: str):
        if self.address == find_address:
            return self.address

    def find_email(self, find_email: str):
        if self.email == find_email:
            return self.email
            
    def remove_phone(self, remove_phone)-> None:
        for index, phone in enumerate(self.phones):
            if phone.value == remove_phone:
                del self.phones[index]

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)
        return f'Birthday added'


    def edit_birthday(self, new_birthday: str):
        self.birthday.value = new_birthday
        return f'Birthday edited'

    def remove_birthday(self):
        self.birthday = None

    def days_to_birthday(self, target_days):
        days = self.birthday.get_days_to_next_birthday()
        if days <= target_days:
            return self.name.value, days
            
    def __str__(self) -> str:
        days = str(self.days_to_birthday())
        return f" Contact name: {self.name.value:<10} birthday: {str(self.birthday):<11}({days:<4} days) phones: {'; '.join(p.value for p in self.phones)}"
    
    def __repr__(self) -> str:
        self.phones_repr = ', '.join([phone.value for phone in self.phones])
        return f'Record({self.name.value}, {self.phones_repr}, {self.birthday.value})'
    
    
        


