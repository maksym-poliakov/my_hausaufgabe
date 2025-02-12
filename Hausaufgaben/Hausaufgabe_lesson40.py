from collections import Counter,namedtuple

# Шапка для отделения заданий
def print_task_number(task_numb) :
    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит
# на экран наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter из модуля collections.
# Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с
# количеством вхождений каждого слова. Выведите наиболее часто встречающиеся слова и их количество.
# Пример вывода:
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1

# функция возвращает очищенную строку от символов
def clear_text(text) :
    # Получим строку и удалим все символы из нее
    # символы будем заменять пробелами чтоб не вычислять стоит символ в конце, середине или начале слова
    text_tmp = text.lower().split()
    for index, word in enumerate(text_tmp):
        word_tmp = []
        # Слово может состоять как из букв так и из цифр, а также буквенно-цифровых комбинаций
        # прийдется некоторые слова перебирать по символьно (дробные числа в данной задаче не обрабатываем)
        if not (word.isalpha() or word.isdigit()) :
            # В этом случае прийдется пробежаться посимвольно
            for symbol in word :
                if not(symbol.isalpha() or symbol.isdigit()):
                    word_tmp.append(' ')
                else:
                    word_tmp.append(symbol)
            # удалим слово и вместо него добавим новое или новые (новые могут появиться если знак препинания был не
            # в конце или начале слова)
            text_tmp.remove(word)
            text_tmp.insert(index,''.join(word_tmp))
    return ' '.join(text_tmp)

# Возвращает словарь с количеством вхождения каждого слова
def count_words(text) :
    # Привел к типу dict как указано в ТЗ дальше прийдется снова приводить к counter
    return  dict(Counter(text.lower().split()))


# Функция возвращает результат слов с наибольшим вхождениям.
# Вывод результата согласно показанному в задании
# будет выведен результат в конце которого будет в любом случае один ключ который имеет значение 1
# sed: 2
# Lorem: 1
def get_result (dict_count) :
    dict_count = Counter(dict_count)
    string_tmp = ''
    count = 1
    # Если есть слова, которые встречаются больше 1 раза,
    # то создадим для них список ключей
    for key,value in dict(dict_count).items():
        new_key = []
        if value > 1 :
            for k,v in dict(dict_count).items():
                if v > 1 and v == value:
                    if not k in new_key :
                        new_key.append(k)
                        dict_count.pop(k)
        if new_key:
            # сбросим сформированный список ключей в словарь
            dict_count[','.join(new_key)] = value
    # Посчитаем сколько значений необходимо вывести
    for value in dict_count.values() :
        if value > 1 :
            count += 1
    # Соберем вывод как показан в ТЗ с выводом одного ключа со значением 1
    dict_result = dict(Counter(dict_count).most_common(count))
    print(dict_result)
    for key,value in dict_result.items():
        string_tmp += key + ': ' + str(value) + '\n'
    return string_tmp


print(print_task_number(1))
print('\033[33mПример строки для ввода : \n str1 : Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
      'Sed sed lacinia est.\n str2: Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
      'Sed sed lacinia est. consectetur est\033[0m')
string_input = input('Введите строку : ')
print(f'\033[31mРезультат : \n{get_result(count_words(clear_text(string_input)))}\033[0m')



# 2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке,
# включающий поля name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.
# Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris



Person = namedtuple('Person',['Name','Age', 'City'])

menchen = [
    Person('Ivan',23,'Munchen'),
    Person('David',38,'Berlin'),
    Person('Kirill',42,'Dresden')
]

def print_mench(list_menchen) :
    str_tmp = ''
    for mench in list_menchen :
        str_tmp += f'Name: {mench.Name}, Age: {mench.Age}, City: {mench.City} \n'
    return str_tmp


print(print_task_number(2))
print(print_mench(menchen ))

# 3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для
# указанного ключа с использованием метода get или setdefault. Создайте функцию get_value_from_dict,
# которая принимает словарь и ключ в качестве аргументов, и возвращает значение для указанного ключа,
# используя метод get или setdefault в зависимости от выбранного варианта. Выведите полученное значение на экран.
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)?y
# Значение для ключа 'banana': 6

def yes_no(y_n) :
    y_n = y_n.lower()
    while True :
        if y_n == 'y' or y_n == 'н' :
            return True
        elif y_n == 'n' or y_n == 'т' :
            return False
        else :
            y_n = input('Введите только y или n : ')
            continue

my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

def get_value_from_dict(dict_data) :
    key = input('введите ключ : ')
    if yes_no(input('Использовать метод get (y/n)? ')) :
        return f'Значение для ключа \'{key}\': {dict(dict_data).get(key)}'
    else:
        return f'Значение для ключа \'{key}\': {dict(dict_data).setdefault(key,'0')}'

print(print_task_number(3))
print("'apple': 5, 'banana': 6, 'cherry': 7")
print(get_value_from_dict(my_dict))


