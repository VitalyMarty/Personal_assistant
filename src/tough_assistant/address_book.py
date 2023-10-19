from backup import Backup, PickleStorage, VERSION, FILENAME_ADDRESSBOOK

from collections import UserDict
from fields_classes import Address, Birthday, Email, Name, Phone  


class AddressBook(UserDict):

    def __init__(self, version=VERSION):
        super().__init__()
        self.version = version

    def add_record(self, name):
        """Add new contact to the contacts. <name> """
        record = Record(name)
        self.data[record.name] = record
        return f'Added new contact {record.name} to contacts'
    
    def add_address_to_record(self, name, address: str) -> str:
        """Add address to the contact. <name> <address>"""
        record: Record = self.find_record(name)
        record.address = address
        return f'Added new address {record.address} to contact {record.name}'
    
    #TODO change code for phone
    def add_phone_to_record(self, name, phone: str) -> str:
        """Add phone to the contact. <name> <phone>"""
        record: Record = self.find_record(name)
        record.phones.append(Phone(phone))
        return f'Added new phone {record.phones[-1]} to contact {record.name}'
    
    def add_email_to_record(self, name, email: str) -> str:
        """Add email to the contact. <name> <email>"""
        record: Record = self.find_record(name)
        record.email = email
        return f'Added new email {record.email} to contact {record.name}'
    
    def add_birthday_to_record(self, name, birthday: str) -> str:
        """Add date of birthday to the contact. <name> <date>"""
        record: Record = self.find_record(name)
        record.birthday = birthday
        return f'Added new birthday {record.birthday} to contact {record.name}'
    
    def edit_address_in_record(self, name: str, new_address: str) -> str:
        """Edit address in the contact. <name> <old address> <new address>"""
        record: Record = self.find_record(name)
        old_address = record.address
        record.address = new_address
        return f"The old address '{old_address}' was changed to a new '{record.address}' in the contact '{record.name}'"

    def edit_phone_in_record(self, name: str, old_phone, new_phone: str) -> str:
        """Edit phone in the contact. <name> <old phone> <new phone>"""
        record: Record = self.find_record(name)
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        record.edit_phone(old_phone, new_phone)
        return f"The old phone '{old_phone.value}' was changed to a new '{new_phone.value}' in the contact '{record.name}'"
    
    def edit_email_in_record(self, name: str, new_email: str) -> str:
        """Edit email in the contact. <name> <old email> <new email>"""
        record: Record = self.find_record(name)
        old_email = record.email
        record.email = new_email
        return f"The old email '{old_email}' was changed to a new '{record.email}' in the contact '{record.name}'"
    
    def edit_birthday_in_record(self, name: str, new_birthday: str) -> str:
        """Edit date of birthday in the contact. <name> <old date> <new date>"""
        record: Record = self.find_record(name)
        old_birthday = record.birthday
        record.birthday = new_birthday
        return f"The old birthday '{old_birthday}' was changed to a new '{record.birthday}' in the contact '{record.name}'"
    
    def edit_name_in_record(self, name: str, new_name: str) -> str:
        """Edit name in the contact. <name> <new name>"""
        record: Record = self.find_record(name)
        old_name = record.name
        record.name = new_name
        self.data[record.name] = self.data.pop(old_name)
        return f"The old name '{old_name}' was changed to a new '{record.name}' in the contact '{record.name}'"

    def find_record(self, name: str):
        """Find contact by name. <name>"""
        record = self.data.get(name, None)
        if record is None:
            raise ValueError(f"There is no contact with name {name} in the book")
        return record

    def delete_record(self, name: str):
        """Remove a contact from the contacts. <name>"""
        record = self.find_record(name)
        del self.data[record.name]
        return f'Contact {record.name} was deleted from contacts'
    
    def delete_email_from_record(self, name):
        """Remove a email from the contact. <name> <email>"""
        record = self.find_record(name)
        old_email = record.email
        record.email = None
        return f'Email {old_email} was deleted from contact {record.name}'
    
    def delete_birthday_from_record(self, name):
        """Remove date of birthday from the contact. <name> <date>"""
        record = self.find_record(name)
        old_birthday = record.birthday
        record.birthday = None
        return f'Birthday {old_birthday} was deleted from contact {record.name}'

    def delete_address_from_record(self, name):
        """Remove an address from the contact. <name> <address>"""
        record = self.find_record(name)
        old_address = record.address
        record.address = None
        return f'Address {old_address} was deleted from contact {record.name}'
    
    def delete_phone_from_record(self, name, phone:str):
        """Remove a phone from the contact. <name> <phone> """
        record: Record = self.find_record(name)
        phone = Phone(phone)
        return record.remove_phone(phone)
                
    def _collect_recods_by_birthday(self, target_days: str):
        dict_contacts = {}
        for record in self.data.values():
            name, days = record.check_birthday_by_date(target_days)
            if name:
                dict_contacts[name] = days
        return dict_contacts 
    
    def find_birthdays_in_x_days(self, days: str):
        """Display a list of contacts whose birthday is a specified number of days from the current date """
        dict_contacts = contacts._collect_recods_by_birthday(days)
        if not dict_contacts:
            return f'Contacts has not birthdays within {days} days in contacts:'
        matching_contacts = f'Contacts has next birthdays within {days} days in contacts:'
        for name, through_days in dict_contacts.items():
            row = f'{name} - {through_days} days'
            matching_contacts = '\n'.join([matching_contacts, row])
            
        return matching_contacts

    def _search_contacts_by_name(self, name: str):
        found_contacts_by_name = []
        for record in self.data.values():
            if name.lower() in record.name.lower():
                found_contacts_by_name.append(record)
        return found_contacts_by_name

    def _search_contacts_by_phone(self, phone: str):
        found_contacts_by_phone = []
        for record in self.data.values():
            for contact_phone in record.phones:
                if phone in contact_phone.value:
                    found_contacts_by_phone.append(record)
        return found_contacts_by_phone
    
    def _search_contacts_by_email(self, email: str):
        found_contacts_by_email = []
        for record in self.data.values():
            if email.lower() in record.email.lower():
                found_contacts_by_email.append(record)
        return found_contacts_by_email
    
    def _search_contacts_by_address(self, address: str):
        found_contacts_by_address = []
        for record in self.data.values():
            if address.lower() in record.address.lower():
                found_contacts_by_address.append(record)
        return found_contacts_by_address

    def _search_contacts_by_birthday(self, birthday: str):
        found_contacts_by_birthday = []
        for record in self.data.values():
            if birthday in str(record.birthday):
                found_contacts_by_birthday.append(record)
        return found_contacts_by_birthday

    def find_in_records(self, search_data: str):
        """Find contact based on available information"""
        found_contacts = []
        found_contacts.extend(self._search_contacts_by_name(search_data))
        found_contacts.extend(self._search_contacts_by_phone(search_data))
        found_contacts.extend(self._search_contacts_by_email(search_data))
        found_contacts.extend(self._search_contacts_by_address(search_data))
        found_contacts.extend(self._search_contacts_by_birthday(search_data))

        if not found_contacts:
            return f'Not find contacts with search parameters "{search_data}"'
        else:
            str_result = f'The contacts has next records with search parameters "{search_data}":'
            for ind, record in enumerate(found_contacts, start=1):
                # Якщо менше ind < 10, то буде 01, 02, ..., 09, якщо більше, то 10, 11, ...
                ind = f'0{ind}' if ind <= 9 else str(ind)
                print(str_result)
                row = f'\n{ind}.\n{str(record)}'
                print(row)
                str_result = ''.join([str_result, row])  
            print(str_result)

        return str_result

    def show_contacts(self):
        """Show all contacts"""
        if not self.data:
            return 'Book no contacts yet'
        message = 'Book has next contacts:\n'
        for count, key_record in enumerate(self.data, start=1):
            message = '\n'.join([message, f'{count}.\n{self.data[key_record]}'])

        return message


class Record:
    def __init__(self, name:str):
        self._name = None
        self.phones = []
        self._address = None  
        self._email = None
        self._birthday = None
        self.name = name

        
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
        if address is None:
            self._address = None
        else:
            self._address = Address(address)

    @property
    def email(self):
        if self._email is None:
            return ''
        return self._email.value
    
    @email.setter
    def email(self, email: str):
        if email is None:
            self._email = None
        else:
            self._email = Email(email)

    @property
    def birthday(self):
        if self._birthday is None:
            return ''
        return self._birthday.value
    
    @birthday.setter
    def birthday(self, birthday: str):
        if birthday is None:
            self._birthday = None
        else:        
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
             
    def remove_phone(self, remove_phone)-> None:
        for index, phone in enumerate(self.phones):
            if phone == remove_phone:
                del self.phones[index]
                return f'Phone {phone.value} was deleted from contact {self.name}'
        return ValueError(f'Phone number - {remove_phone.value} is not exist in contact: {self.name}') 

    def check_birthday_by_date(self, target_days):
        if self._birthday is None:
            return None, None
        days = self._birthday.get_next_birthday()
        if days <= int(target_days):
            return self.name, days
        else:
            return None, None
        
    def __str__(self):
        phones = '; '.join([phone.value for phone in self.phones])
        return f'Contact: {self.name}\nBirthday: {self.birthday}\nAddress: {self.address}\nEmail: {self.email}\nPhones: {phones}\n'

    def __repr__(self) -> str:
        phones_repr = ', '.join([phone.value for phone in self.phones])
        return f'Record({self.name}, {self.birthday}, {self.address}, {self.email}, {phones_repr})'
    
    
# Створюємо сховище, де зберігається файл з контактами та нотатками
storage_addressbook = Backup(PickleStorage(FILENAME_ADDRESSBOOK))
# Завантажуємо контакти та нотатки з файлів. Якщо файли відсутні створюємо нові.
contacts = AddressBook() if storage_addressbook.load() is None else storage_addressbook.load()
       


