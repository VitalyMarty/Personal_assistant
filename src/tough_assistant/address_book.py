from backup import Backup, PickleStorage

from collections import UserDict
from fields_classes import Address, Birthday, Email, Name, Phone  


class AddressBook(UserDict):

    def add_record(self, name):
        record = Record(name)
        self.data[record.name] = record
        return f'Added new contact {record.name} to contacts'
    
    def add_address_to_record(self, name, address: str) -> str:
        record: Record = self.find_record(name)
        record.address = address
        return f'Added new address {record.address} to contact {record.name}'
    
    #TODO change code for phone
    def add_phone_to_record(self, name, phone: str) -> str:
        record: Record = self.find_record(name)
        record.phones.append(Phone(phone))
        return f'Added new phone {record.phones[-1]} to contact {record.name}'
    
    def add_email_to_record(self, name, email: str) -> str:
        record: Record = self.find_record(name)
        record.email = email
        return f'Added new email {record.email} to contact {record.name}'
    
    def add_birthday_to_record(self, name, birthday: str) -> str:
        record: Record = self.find_record(name)
        record.birthday = birthday
        return f'Added new birthday {record.birthday} to contact {record.name}'
    
    def edit_address_in_record(self, name: str, new_address: str) -> str:
        record: Record = self.find_record(name)
        old_address = record.address
        record.address = new_address
        return f"The old address '{old_address}' was changed to a new '{record.address}' in the contact '{record.name}'"

    def edit_phone_in_record(self, name: str, old_phone, new_phone: str) -> str:
        record: Record = self.find_record(name)
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        record.edit_phone(old_phone, new_phone)
        return f"The old phone '{old_phone.value}' was changed to a new '{new_phone.value}' in the contact '{record.name}'"
    
    def edit_email_in_record(self, name: str, new_email: str) -> str:
        record: Record = self.find_record(name)
        old_email = record.email
        record.address = new_email
        return f"The old email '{old_email}' was changed to a new '{record.email}' in the contact '{record.name}'"
    
    def edit_birthday_in_record(self, name: str, new_birthday: str) -> str:
        record: Record = self.find_record(name)
        old_birthday = record.birthday
        record.birthday = new_birthday
        return f"The old birthday '{old_birthday}' was changed to a new '{record.birthday}' in the contact '{record.name}'"
    
    def edit_name_in_record(self, name: str, new_name: str) -> str:
        record: Record = self.find_record(name)
        old_name = record.name
        record.name = new_name
        self.data[record.name] = self.data.pop(old_name)
        return f"The old name '{old_name}' was changed to a new '{record.name}' in the contact '{record.name}'"

    def find_record(self, name: str):
        record = self.data.get(name, None)
        if record is None:
            raise ValueError(f"There is no contact with name {name} in the book")
        return record

    def delete_record(self, name: str):
        record = self.find_record(name)
        del self.data[record.name]
        return f'Contact {record.name} was deleted from contacts'
    
    def delete_email_from_record(self, name):
        record = self.find_record(name)
        old_email = record.email
        record.email = None
        return f'Email {old_email} was deleted from contact {record.name}'
    
    def delete_birthday_from_record(self, name):
        record = self.find_record(name)
        old_birthday = record.birthday
        record.birthday = None
        return f'Email {old_birthday} was deleted from contact {record.name}'

    def delete_address_from_record(self, name):
        record = self.find_record(name)
        old_address = record.address
        record.address = None
        return f'Email {old_address} was deleted from contact {record.name}'
    
    def delete_phone_from_record(self, name, phone:str):
        record: Record = self.find_record(name)
        phone = Phone(phone)
        return record.remove_phone(phone)
    


    
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
        
        for record in self.data.values():
            name, days = record.days_to_birthday(target_days)  
            if name:
                dict_contacts[name] = days
                
        return dict_contacts 

    def _search_contacts_by_name(self, name):
        found_contacts_by_name = []
        for record in self.data.values():
            if name.lower() in record.name.lower():
                found_contacts_by_name.append(record)
        return found_contacts_by_name

    def _search_contacts_by_phone(self, phone):
        found_contacts_by_phone = []
        for record in self.data.values():
            for contact_phone in record.phones:
                if phone in contact_phone.value:
                    found_contacts_by_phone.append(record)
        return found_contacts_by_phone
    
    def find_in_records(self, search_data: str):
        found_contacts = []
        found_contacts.extend(self._search_contacts_by_name(search_data))
        found_contacts.extend(self._search_contacts_by_phone(search_data))

        if not found_contacts:
            return f'Not find contacts with search parameters "{search_data}"'
        else:
            str_result = f'The contacts has next records with search parameters "{search_data}":'
            for ind, record in enumerate(found_contacts, start=1):
                # Якщо менше ind < 10, то буде 01, 02, ..., 09, якщо більше, то 10, 11, ...
                ind = f'0{ind}' if ind <= 9 else str(ind)
                print(str_result)
                row = f'\n{ind}.\n {str(record)}'
                print(row)
                str_result = ''.join([str_result, row])  
            print(str_result)

        return str_result

            
    def show_contacts(self):
        message = 'Book has next records:\n'
        for count, key_record in enumerate(self.data, start=1):
            message = '\n'.join([message, f'{count}.\n{self.data[key_record]}'])

        return message

class Record:
    def __init__(self, name:str):
        self._name = Name(name)
        self.phones = []
        self._address = None  
        self._email = None
        self._birthday = None
        
    # Реалізація класу
    @property
    def name(self):
        return self._name.value
    
    @name.setter
    def name(self, name: str):
        self._name = Name(name)

    @property
    def address(self):
        if self._address is None:
            return ''
        return self._address.value
    
    @address.setter
    def address(self, address: str):
        self._address = Address(address)

    @property
    def email(self):
        if self._email is None:
            return ''
        return self._email.value
    
    @email.setter
    def email(self, email: str):
        self._email = Email(email)

    @property
    def birthday(self):
        if self._birthday is None:
            return ''
        return self._birthday.value
    
    @birthday.setter
    def birthday(self, birthday: str):
        self._birthday = Birthday(birthday)

    def edit_phone(self, old_phone: Phone, new_phone: Phone)-> None:
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone.value:
                edit_phone_i = i
                break
        else:
            raise ValueError(f'Phone number - {old_phone.value} is not exist in contact: {self.name}') 
        self.phones[edit_phone_i] = new_phone

    def find_phone(self, find_phone: Phone)-> Phone:
        for index, phone in enumerate(self.phones):
            if phone == find_phone:
                return self.phones[index]
        return ValueError(f'Phone number - {find_phone.value} is not exist in contact: {self.name}') 
            
    # def find_address(self, find_address: str):
    #     if self.address == find_address:
    #         return self.address

    # def find_email(self, find_email: str):
    #     if self.email == find_email:
    #         return self.email
            
    def remove_phone(self, remove_phone)-> None:
        for index, phone in enumerate(self.phones):
            if phone == remove_phone:
                del self.phones[index]
                return f'Phone {phone.value} was deleted from contact {self.name}'
        return ValueError(f'Phone number - {remove_phone.value} is not exist in contact: {self.name}') 


    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)
        return f'Birthday added'


    def edit_birthday(self, new_birthday: str):
        self.birthday.value = new_birthday
        return f'Birthday edited'

    def remove_birthday(self):
        self.birthday = None

    def days_to_birthday(self, target_days):
        days = self.birthday
        if days <= target_days:
            return self.name.value, days
            
    # def __str__(self) -> str:
    #     days = str(self.days_to_birthday())
    #     return f" Contact name: {self.name.value:<10} birthday: {str(self.birthday):<11}({days:<4} days) phones: {'; '.join(p.value for p in self.phones)}"
    
    def __str__(self):
        phones = '; '.join([phone.value for phone in self.phones])
        return f'Contact: {self.name}\nBirthday: {self.birthday}\nAddress: {self.address}\nEmail: {self.email}\nPhones:{phones}\n'

    
    # def __repr__(self) -> str:
    #     self._phones_repr = ', '.join([phone.value for phone in self.phones])
    #     return f'Record({self._name.value}, {self._phones_repr}, {self._birthday.value})'
    
    
# Створюємо сховище, де зберігається файл з контактами та нотатками
storage_addressbook = Backup(PickleStorage('test_addressbook.pickle'))
# Завантажуємо контакти та нотатки з файлів. Якщо файли відсутні створюємо нові.
contacts = AddressBook() if storage_addressbook.load() is None else storage_addressbook.load()
       


