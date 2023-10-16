from collections import UserDict
from Fields import Field
from datetime import datetime
import re


class Note(Field):
    def __init__(self, value: str) -> None:
        # TODO restore super when fix in Fields
        super().__init__(value)
        # self._value = None
        # self.value = value


    # @Field.value.setter
    # def value(self, value):
    #     if re.match(r"^(.{10,100})$", value):
    #         self._value = value
    #     else:
    #         print("Note must be in range of 10-100 symbols.")


# Class for Tags. Only for check correct input
# only words accepted due to technical assignment
class Tag(Field):
    def __init__(self, value) -> None:
        # TODO restore super when fix in Fields
        super().__init__(value)
        # self._value = None
        # self.value = value

    # check input
    @Field.value.setter
    def value(self, value) -> None:
        if re.match(r"^[A-Za-z]{3,10}$", value):
            self._value = value
        else:
            print("Incorrect Tag format. 3-10 letters, without digits, spaces and special symbols accepted.")


class NoteRecord:
    def __init__(self, text: str) -> None:
        self.note = Note(text)
        # set time when record is created
        self.edit_date = datetime.now()
        self.tags = []

    def __str__(self) -> str:
        return str(self.note)

    # return __repr__ as string
    def __repr__(self) -> str:
        return self.__str__()

    # add one tag per one call to one note
    def add_tag(self, tag: str) -> str:
        # checking length of tags[] to test if Tag setter allow value
        add_check = len(self.tags)
        self.tags.append(Tag(tag))
        if len(self.tags) > add_check:
            return "Tag is added successfully."
        else:
            return "Tag is not added."


class Notebook(UserDict):
    # using for calling iter with parameters
    def __init__(self, dict=None):
        super().__init__(dict)
        # notes counter
        self.counter = 0

    # placeholder __getstate__
    def __getstate__(self):
        attributes = {**self.__dict__}
        return attributes

    # placeholder __setstate__
    def __setstate__(self, value):
        self.__dict__ = value

    # adding note
    def add_note(self, record: NoteRecord) -> str:
        # set note number
        self.counter += 1
        self.data[self.counter] = record
        return f"Note #{self.counter} is successfully added"

    # remove note
    def remove_note(self, id: int) -> str:
        if id <= 0 or id > self.counter:
            return f"Incorrect note number. Note number must be in range 1 to {self.counter}" if self.counter \
                else f"You have {self.counter} notes. Nothing to delete."
        # del note record
        self.data.pop(id)
        # decrease notes counter
        self.counter -= 1
        # recalculate notes ID (dict keys)
        for i in range(id, self.counter+1):
            self.data[i] = self.data.pop(i+1)
        return f"Note with id {id} is successfully deleted."

    # TODO edit notes
    def edit_note(self, *args, **kwargs) -> str:
        return "Return from class Notebook function edit_note"

    # TODO find note
    def find_note(self, *args, **kwargs) -> str:
        return "Return from class Notebook function find_note"

    # TODO find note by tag
    def find_by_tag(self, *args, **kwargs) -> str:
        return "Return from class Notebook function find_by_tag"

    # TODO sort notes by tag
    def sort_by_tag(self, *args, **kwargs) -> str:
        return "Return from class Notebook function sort_by_tag"

if __name__ == "__main__":
    print("Using for testing")
    record1 = NoteRecord("some text1")
    print(record1)
    record2 = NoteRecord("some text2")
    print(record2)
    record3 = NoteRecord("some text3")
    print(record3)

    print(record1.add_tag("aaa"))
    print(record1.tags[0])

    print(record1.edit_date)

    book = Notebook()
    print(book.add_note(record1))
    print(book.add_note(record2))
    print(book.add_note(record3))
    print("Count of notes: ", book.counter)
    print(book.remove_note(1))
