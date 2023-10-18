import re
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.validate(self.normalize(value))

    def normalize(self, value: str) -> str:
        return value
    
    def validate(self, value: str) -> str:
        return value

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Phone({self._value})'


class Name(Field):

    def normalize(self, name: str) -> str:
        return name.title()


class Phone(Field):

    def normalize(self, value: str) -> str:
        new_value = (
            value.removeprefix("+")
                .replace("(", "")
                .replace(")", "")
                .replace("-", "")
                .replace(" ", "")
        )
        return new_value
    
    def validate(self, value: str) -> str:
        if len(value) < 10 or len(value) > 12:
                raise ValueError(f"Phone '{value}' must contains 10 symbols.")
        if not value.isnumeric():
                raise ValueError(f"Phone '{value}' is wrong.")
        return value
    
    def __eq__(self, phone):
        return self._value == phone.value


class Birthday(Field):

    def normalize(self, birthday: str) -> str:
        normal_birthday = datetime.strptime(birthday, '%Y-%m-%d').date()                    # TODO Якщо дата не в правильному форматі викличеться ValueError. Її треба якось обробити
        return normal_birthday

    def validate(self, birthday: str) -> str:
        today = datetime.now().date()
        if birthday > today:
            raise ValueError(f"Birthday '{birthday}' must be less than current year and date.")
        return birthday
    
    def get_next_birthday(self):
        today = datetime.now().date()
        next_birthday = self._value.replace(year=today.year)
        if next_birthday < today:
            next_birthday - self._value.replace(year = today.year+1)
        return abs(next_birthday - today).days    
            


class Address(Field):
    pass


class Email(Field):
    
    def validate(self, email: str) -> str:
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu|ua|net]{3}$)"
        is_valid = re.search(pattern, email)
        if not is_valid:
            return ValueError(f"Email '{email}' is not valid.")
        return email
    

class Date(Field):
    pass


# Class note for Notebook
class Note(Field):

    @Field.value.setter
    def value(self, value):
        if re.match(r"^(.{3,250})$", value):
            self._value = value
        else:
            print("Note must be in range of 3-250 symbols.")


# Class for Tags. Only for check correct input
# only words accepted due to technical assignment
class Tag(Field):
    # return __repr__ as string
    def __repr__(self) -> str:
        return self.__str__()

    # check input
    @Field.value.setter
    def value(self, value) -> None:
        if re.match(r"^[A-Za-z]{3,10}$", value):
            self._value = value
        else:
            print("Incorrect Tag format. Only 3-10 letters, without digits, spaces and special symbols accepted.")

                                                                                            
                                                                                            #TODO Видалити вкінці
# Приклад використання полів.
if __name__ == '__main__':
    field_name = Name('taras shevchenko')
    print(field_name)                           # Taras Shevchenko

    field_phone = Phone('+38(063)-500-12-40')   # 380635001240
    print(field_phone)

    field_birthday = Birthday('1990-05-12')
    print(field_birthday)                       # 1990-05-12

    field_date = Date(datetime.now())           
    print(field_date)                           # 2023-10-16 09:35:22.222808

    field_email_valid = Email('test.email@gmail.com')  
    print(field_email_valid)                          # test.email@gmail.com 

    field_email_not_valid = Email('test:!@email@gmail.com')  
    print(field_email_not_valid)                          # Email 'test:!@email@gmail.com' is not valid.
    
    