

def input_error(func):
    """
    Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
    Цей декоратор відповідає за повернення користувачеві повідомлень виду 
        "Enter user name", 
        "Give me name and phone please" і т.п. 
    Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler 
    (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
    """

    def wrapper(*args, **kwargs):
        
        try:
            return func(*args, **kwargs)

        except TypeError as e:
            return e
                    
        except KeyError as e:
            return e
        
        except ValueError as e:
            return e
        
    return wrapper




                                                                                            #TODO Видалити вкінці
# Приклад використання полів.
if __name__ == "__main__":

    @input_error
    def test():
        raise TypeError('Some Error')
    
    a = test()
    print(a)
