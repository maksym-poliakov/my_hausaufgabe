import logging
import os
#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

# 1. Напишите декоратор validate_args, который будет проверять типы аргументов
# функции и выводить сообщение об ошибке, если переданы аргументы неправильного типа.
# Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.
# Пример использования:
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
# greet(25, "Анна")  # Все аргументы имеют правильные типы
# greet("25", "Анна")  # Возникнет исключение TypeError
# Ожидаемый вывод:
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.

def validate_args(inp_int,inp_str) :
    def decorator(func) :
        def wrapper(*args,**kwargs):
            try:
                if not isinstance(args[0],inp_int) :
                    raise TypeError(f"Аргумент {args[0]} имеет неправильный тип {type(args[0])}. Ожидается {inp_int}.")
                if not isinstance(args[1],inp_str) :
                    raise TypeError(f"Аргумент {args[1]} имеет неправильный тип {type(args[1])}. Ожидается {inp_str}.")
            except TypeError as e :
                return e
            return func(*args,**kwargs)
        return  wrapper
    return decorator


@validate_args(int,str)
def greet(age, name):
     return f"Привет, {name}! Тебе {age} лет."

print(print_task_number(1))
print(greet('25', "Анна"))

# 2. Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции
# в лог-файл. Каждый вызов функции должен быть записан на новой строке в
# формате "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
# Пример использования:
# @log_args
# def add(a, b):
#     return a + b
# add(2, 3)
# add(5, 7)
# Ожидаемый вывод в файле log.txt:
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории,
# где находится скрипт Python.
file_name = "log.txt"
logging.basicConfig(filename=file_name,format="%(message)s",
                    level=logging.DEBUG)
def log_args(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        arg_str = ','.join(map(str,args)) if args else ''
        kwargs_str = ','.join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else ''
        logging.info(f"Аргументы: {arg_str} {kwargs_str } ; Результат: {result }")
        print(f"данные успешно записаны в файл {file_name}")
        return result
    return wrapper

@log_args
def add(a, b):
     return a + b
print(print_task_number(2))

add(2, 3)
add(5, 7)