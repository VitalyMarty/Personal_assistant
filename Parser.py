from Decorators import input_error
from Commands import command_dict

@input_error
def parse_input(user_input: str) -> str:
    new_input = user_input
    data = ''
    for key in command_dict:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):].split()
            break
    if data:
        return handler(new_input)(data)
    return handler(new_input)()


def break_func():
    """
    Якщо користувач ввів команду якої немає в command_dict, то повертаємо повідомлення
    """
    return 'Wrong command!'


def handler(command):
    return command_dict.get(command, break_func)
