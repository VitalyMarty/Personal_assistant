from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog

commands = [
    'hello',
    'add',
    'change',
    'phone',
    'search',
    'add_note',
    'edit_note',
    'delete_note',
    'list_contacts',
    'list_notes',
    'goodbye',
]

def main():
    completer = WordCompleter(commands, ignore_case=True)
    while True:
        user_input = prompt("Enter a command: ", completer=completer)
        if user_input.strip().lower() == 'exit':
            break


# pip install prompt_toolkit
