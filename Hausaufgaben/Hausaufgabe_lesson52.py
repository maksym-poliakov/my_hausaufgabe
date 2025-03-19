from functools import reduce
from decimal import Decimal
import functools
#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

# Напишите функцию, которая принимает на вход список чисел и возвращает сумму
# квадратов только четных чисел из списка, используя функциональные подходы
# (например, map, filter и reduce).
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72
list_number =[4, 6, 3, 4, 2, 3, 9, 0, 7]

def square_even_numbers(list_num:list) -> int :
    return reduce(lambda x,y : x + y,map(lambda x : x ** 2,filter(lambda x : x % 2 == 0,list_num)))


print(print_task_number(1))
print(f'Пример ввода списка чисел : {list_number}')
print(f"Результат: {square_even_numbers(list_number)}")
# Напишите функцию, которая принимает на вход список функций и значение,
# а затем применяет композицию этих функций к значению, возвращая конечный результат.
# Пример использования:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) должно вывести 9


add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3
functions = [add_one, double, subtract_three]

def compose_functions(func:list[functools],num: int | Decimal) -> int | Decimal :
    result = num
    for f in func :
        result = f(result)
    return result

print(print_task_number(2))
print(compose_functions(functions,5))