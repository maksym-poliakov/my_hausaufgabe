# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.
# Пример переданного списка слов:
# ['cat', 'dog', 'tac', 'god', 'act']
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']
# Шапка для отделения заданий
def print_task_number(task_numb) :
    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text


words = ['cat', 'dog', 'tac', 'god', 'act','dog','bof']
def anagrams(list_wort) :
    set_tmp = set() # создадим множество для хранения уже проверенных слов
    result = []
    set_list = set(list_wort) # уберем дубликаты если такие есть
    for wort in set_list:
        wort_tmp = ''.join(sorted(wort))
        if wort_tmp not in set_tmp :
            new_wort = [nw for nw in set_list if set(nw) == set(wort) and len(nw) == len(wort)]
            if len(new_wort) > 1 :
                result.append(new_wort)
            set_tmp.add(wort_tmp) # запишем слова что-бы не проверялись повторно
    return ','.join(map(str,result))

# print(print_task_number(1))
# print(f'\033[33mПолучаемые данные : {words}\033[0m')
# print(f'\033[32mРезультат : {anagrams(words)}\033[0m')

# Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет,
# является ли set1 подмножеством set2. Функция должна возвращать True, если все элементы из set1 содержатся в set2,
# и False в противном случае. Функция должна быть реализована без использования встроенных методов issubset или <=.
# Пример множеств
# {1, 2, 3}
# {1, 2, 3, 4, 5}
# Пример вывода:
# True
def is_subset(set_1,set_2) :
    set_1_tmp = set(map(int,set_1))
    set_2_tmp = set(map(int, set_2))
    # Пробежимся по set_1_tmp и проверим есть ли все эти данные в set_2_tmp
    # если нет то вернем False
    for item in set_1_tmp :
        if not item in set_2_tmp :
            return False
    return True


print(print_task_number(2))
set1 = input('введите первое множество через запятую : ').split(',')
set2 = input('введите первое второе через запятую : ').split(',')
print(f'\033[32mРезультат :{is_subset(set1,set2)}\033[0m')
