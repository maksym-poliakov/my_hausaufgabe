
# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей
# в качестве аргументов и возвращает новый словарь, объединяющий все входные словари.
# Если ключи повторяются, значения должны быть объединены в список.
# Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
# Пример ввода:
# {'a': 1, 'b': 2}
# {'b': 3, 'c': 4}
# {'c': 5, 'd': 6}
# Пример вывода:
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}

# Шапка для отделения заданий
def print_task_number(task_numb) :
    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

def merge_dicts(*args) :
    new_dict = {}
    # преобразуем в список
    list_args = list(args)
    # Получим данные с первого словаря
    for item in list_args :
        # Пробежимся по словарю и если нет такого ключа - или значения добавим - или ключ или значение,
        # ну или то и другое
        for key,value in item.items() :
            if not key in new_dict  :
                new_dict[key] = [value]
            else:
                new_dict[key].append(value)
    return new_dict



print(print_task_number(1))
print(f"Входные данные : {{'a': 1, 'b': 2}},{{'b': 3, 'c': 4}},{{'c': 5, 'd': 6}}")
print(f'Результат : {merge_dicts(*[{'a': 1, 'b': 2},{'b': 3, 'c': 4},{'c': 5, 'd': 6},{1: 'a'}])}')


# 2. Напишите программу, которая принимает строку от пользователя и подсчитывает количество
# уникальных символов в этой строке. Создайте функцию count_unique_chars, которая принимает строку
# и возвращает количество уникальных символов. Выведите результат на экран.
# Пример вывода:
# Введите строку: hello
# Количество уникальных символов: 4
def count_unique_chars(text):
    return len(set(text))

print(print_task_number(2))
string_inp = input('Введите строку : ').strip()
print(f'Количество уникальных символов : {count_unique_chars(string_inp)}')



# 3. Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках.
# Ключами словаря являются имена студентов, а значениями - списки оценок.
# Создайте функцию calculate_average_grade, которая принимает словарь с оценками студентов и
# вычисляет средний балл для каждого студента.
# Функция должна возвращать новый словарь, в котором ключами являются имена студентов,
# а значениями - их средний балл. Выведите результат на экран.
# Пример словаря с оценками
# grades = {
#
#     'Alice': [85, 90, 92],
#
#     'Bob': [78, 80, 84],
#
#     'Carol': [92, 88, 95]
#
# }
# Пример вывода:
# {'Alice': 89.0, 'Bob': 80.66666666666667, 'Carol': 91.66666666666667}

def get_yes_no(y_n) :
    while True:
        if y_n.lower() == 'y' or y_n.lower() == 'н' :
            return True
        elif y_n.lower() == 'n' or y_n.lower() == 'т' :
            return False
        else :
            y_n = input('Введите только Y or N : ')
            continue


def get_dict_student() :
    data_student = {}
    while True :
        name_student = input('Введите имя студента : ').strip().capitalize()
        bal_student = list(map(int,input('Введите балы студента через пробел : ').split()))
        # Добавим данные студента в словарь
        data_student[name_student] = bal_student
        if get_yes_no(input('Добавить данные еще одного студента ? Y/N : ')) :
            continue
        else:
            return data_student

def calculate_average_grade(dict_data) :
    new_dict = {}
    for key ,value in dict_data.items() :
        new_dict[key] = sum(value)/len(value)
    return new_dict

print(print_task_number(3))
print(f'Результат среднего бала для студентов :\n{calculate_average_grade(get_dict_student())}')
