from collections import UserDict


class Note:
    def __init__(self, text):
        self._text = None
        self.text = text

    def __str__(self):
        return str(self.text)

    @property
    def text(self):
        return self._text

    # checking input (if needed)
    @text.setter
    def text(self, text):
        self._text = text


# Class for Tags. Only for check correct input
# only words accepted due to technical assignment
class Tag(Note):
    def __init__(self, text):
        super().__init__(text)

#TODO add input check
    @Note.text.setter
    def text(self, text):
        self._text = text


class NoteRecord:
    def __init__(self, text):
        self.note = Note(text)
        self.tag = []

    def __str__(self):
        return "Class NoteRecord str method"

    # return __repr__ as string
    def __repr__(self):
        return self.__str__()


class Notebook(UserDict):
    # using for calling iter with parameters
    def __init__(self, dict=None):
        super().__init__(dict)

    # not needed for this class. there are no problematic attributes
    # placeholder __getstate__
    def __getstate__(self):
        attributes = {**self.__dict__}
        return attributes

    # not needed too
    # placeholder __setstate__
    def __setstate__(self, value):
        self.__dict__ = value

    # TODO adding note
    def add_note(self, *args, **kwargs) -> str:
        return "Return from class Notebook function add_note"

    # TODO remove note
    def remove_note(self, *args, **kwargs) -> str:
        return "Return from class Notebook function remove_note"

    # TODO edit notes
    def edit_note(self, *args, **kwargs) -> str:
        return "Return from class Notebook function edit_note"

    # TODO find note
    def find_note(self, *args, **kwargs) -> str:
        return "Return from class Notebook function find_note"

    # TODO add tag|tags to note
    def add_tag(self, *args, **kwargs) -> str:
        return "Return from class Notebook function add_tag"

    # TODO find note by tag
    def find_by_tag(self, *args, **kwargs) -> str:
        return "Return from class Notebook function find_by_tag"

    # TODO sort notes by tag
    def sort_by_tag(self, *args, **kwargs) -> str:
        return "Return from class Notebook function sort_by_tag"

if __name__ == "__main__":
    print("Using for testing")
    