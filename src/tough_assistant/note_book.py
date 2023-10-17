from collections import UserDict
from fields_classes import Field
from datetime import datetime
import re

# TODO remove in release
# class Note(Field):
#     def __init__(self, value: str) -> None:
#         super().__init__(value)

    # @Field.value.setter
    # def value(self, value):
    #     if re.match(r"^(.{10,100})$", value):
    #         self._value = value
    #     else:
    #         print("Note must be in range of 10-100 symbols.")


# TODO move class in Fields in release
# Class for Tags. Only for check correct input
# only words accepted due to technical assignment
class Tag(Field):
    # def __init__(self, value) -> None:
    #     super().__init__(value)
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


class NoteRecord:
    def __init__(self, text: str) -> None:
        self.note = Field(text)
        # set time when record is created
        self.edit_date = datetime.now()
        self.tags = []

    def __str__(self) -> str:
        return str(self.note)

    # return __repr__ as string
    def __repr__(self) -> str:
        return self.__str__()

    # add one tag per one call to one note
    def add_tag_record(self, tag: str) -> str:
        # checking length of tags[] to test if Tag setter allow value
        add_check = len(self.tags)
        self.tags.append(Tag(tag))
        if self.tags[add_check].value is None:
            self.tags.pop(add_check)
            return "Tag is not added."
        else:
            return "Tag is added successfully."

    # sorting tag in record
    def sort_tags(self) -> str:
        if len(self.tags) <= 1:
            return "No Tags to sort. Try to add it first."
        sorting_list = [itm.value for itm in self.tags]
        sorting_list.sort()
        self.tags = [Tag(itm) for itm in sorting_list]
        return "Tags is sorted."


class Notebook(UserDict):
    # using for calling iter with parameters
    def __init__(self, dict=None):
        super().__init__(dict)
        # notes counter
        self.counter = 0

    # using __call__ for show all.
    def __call__(self) -> str:
        if not self.counter:
            return "There are no notes."
        for i, key in enumerate(self.data.keys()):
            print(f"Note #{i + 1} : {self.data[key]}" if not self.data[key].tags
        else f"Note #{i + 1} : {self.data[key]}\n\tTags: {self.data[key].tags}")

        return f"End of Notes. {self.counter} notes were shown." if self.counter > 1 \
            else f"End of Notes. {self.counter} note was shown."

    # placeholder __getstate__
    def __getstate__(self):
        attributes = {**self.__dict__}
        return attributes

    # placeholder __setstate__
    def __setstate__(self, value):
        self.__dict__ = value

    # adding note
    # def add_note(self, record: NoteRecord) -> str:
    def add_note(self, *args) -> str:
        # set note number
        self.counter += 1
        self.data[self.counter] = NoteRecord(' '.join(map(str, args)))
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
        for i in range(id, self.counter + 1):
            self.data[i] = self.data.pop(i + 1)
        return f"Note with id {id} is successfully deleted."

    # edit notes with changing edit time
    # def edit_note(self, id: int, text: str) -> str:
    def edit_note(self, id: int, *args) -> str:
        # if there are no notes
        if not self.counter:
            return "There are no Notes. Try to add it first."
        # if select Note id out from range
        if id not in range(1, self.counter+1):
            return f"There are {self.counter} Notes. Enter valid id."
        self.data[id].note = ' '.join(map(str, args))
        
        # TODO change to datetime.now() after testing !
        
        self.data[id].edit_date = datetime(2022, 7, 21)
        return f"Note with id {id} is successfully changed."

    # TODO find note
    def find_note(self, keyword: str) -> str:
        return "Return from class Notebook function find_note"

    # TODO find note by tag
    def find_by_tag(self, tag: str) -> str:
        return "Return from class Notebook function find_by_tag"

    # sort notes by edit date
    def sort_by_date(self) -> str:
        if not self.counter:
            return "There are no Notes. Try to add it first."
        if self.counter == 1:
            print(f"Note #{self.counter} : {self.data[self.counter]}")
            return f"End of Notes. {self.counter} note was shown."
        sorted_dict = {}
        for key in self.data:
            sorted_dict[self.data[key].edit_date] = key
        sorted_dict = dict(sorted(sorted_dict.items()))
        for key in sorted_dict.keys():
            print(f"Change date: {key:%d-%m-%Y %H:%M:%S}\t Note id{sorted_dict[key]}\t Note: {self.data[sorted_dict[key]]}")
        # clear temp variables to prevent problems
        sorted_dict.clear()
        return f"End of Notes. {self.counter} Notes were sorted by create/edit time."

    # add tag to the note
    def add_tag(self, id: int, tag: str) -> str:
        msg = self.data[id].add_tag_record(tag)
        return msg

    # sort tags in record.
    def sort_tag(self, id: int) -> str:
        print("Test: ", self.data[id].tags)
        msg = self.data[id].sort_tags()
        print(f"Note id {id}.\tTags: {', '.join(str(itm) for itm in self.data[id].tags)} " if len(self.data[id].tags) > 0 else "")
        return msg




if __name__ == "__main__":
    print("Using for testing")

    book = Notebook()
    print(book.counter)
    print(book.add_note("obtain", "a.", "string", "from.", "the", "attributes"))
    print(book.counter)
    print(book.add_note("Lorem", "Ipsum"))
    print(book.counter)
    print(book.add_note("Why", "do", "we", "use", "it", "?"))
    print(book.counter)

    book()

    print(book.add_tag(1, "fish"))
    print(book.add_tag(1, "word 1 fdsfds"))
    print(book.add_tag(1, "word"))
    print(book.add_tag(1, "auto"))
    print(book.add_tag(2, "some"))

    print(book())

    print(book.edit_note(3, "new", "text", "for", "test"))

    print(book.sort_by_date())

    book()

    print(book.sort_tag(1))

    book()

    print(book.remove_note(2))

    book()
