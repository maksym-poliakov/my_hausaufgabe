# 1. Напишите функцию, которая принимает список кортежей от пользователя, где каждый кортеж содержит информацию
# о студенте (имя, возраст, средний балл). Программа должна вывести на экран имена студентов,
# чей средний балл выше заданного значения. Используйте методы кортежей и циклы для обработки данных.
# Выведите итоговый список на экран с помощью команды print.
# Пример списка кортежей:
#
# Пример вывода:
# Введите пороговое значение среднего балла: 90
# Студенты со средним баллом выше 90 : ['Charlie']
print(f'\033[35m+++++++++++++++++++++++++++++++++++')
print('+++++++++++ Задание № 1 +++++++++++')
print(f'+++++++++++++++++++++++++++++++++++\033[0m')
print('''\033[31mПримеры вводов просто скопировать и вставить:\033[0m 
\033[32m 80
100
76.3\033[0m''')

# Возвращает число без точки если было введено целое число
def get_int_float(bal):
    result = bal-int(bal)
    if result == 0 :
        return int(bal)
    else :
         return bal
# выводит текст в единственном числе если найден один студент
# и во множественном числе если студентов два и более
def get_print_text(list_name_bal) :
    letter =''
    if len(list_name_bal) < 2 :
        return f'Студенты с средним баллом выше {get_int_float(list_name_bal[0])} : не найдены'
    elif len(list_name_bal) > 2 :
        letter = 'ы'
    return f'Студент{letter} с средним баллом выше {get_int_float(list_name_bal[0])} : {list_name_bal[1 :]}'


# Возвращает список имен студентов попадающих под условие
# Нулевой индекс занимается значение того среднего бала который ввел пользователь
# Начиная с первого индекса в списке хранятся имена студентов
def get_avg_bal(bal,data_tuple) :
    len_tuple_data = len(data_tuple)
    len_list_data = 3
    return_name = []
    if len_tuple_data > 0:
        for item in range(len_tuple_data) :
            if len(data_tuple[item]) < len_list_data :
                return f' У одного или нескольких студентов недостаточно данных !!!'
            elif len(data_tuple[item]) > len_list_data :
                return f' У одного или нескольких студентов переизбыток данных !!!'
        return_name.append(float(bal)) # инициализируем список сразу данными о среднем бале который ввел пользователь
        for avg in data_tuple :
            if avg[len_list_data - 1] > bal :
                return_name.append(avg[0])
        return  get_print_text(return_name) # возвращает список

# можно использовать для примера закомментированный tuple_data в нем нехватает данных
tuple_data = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
#tuple_data = [("Alice", 20), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]

bal_input = float(input(f'\033[33mEnter avg bal : \033[0m'))
print(get_avg_bal(bal_input,tuple_data))

print(f'\033[35m+++++++++++++++++++++++++++++++++++')
print('+++++++++++ Задание № 2 +++++++++++')
print(f'+++++++++++++++++++++++++++++++++++\033[0m')
print('''\033[31mПримеры вводов просто скопировать и вставить:\033[0m 
\033[32m\'          \' - полностью пустая строка 
Программирование! №это$ интересно и пол56езно
Программирование это интересно и полезно\033[0m''')
# 2. Напишите программу, которая принимает строку от пользователя и разбивает ее на отдельные слова.
# Затем программа должна создать новый кортеж, содержащий длину каждого слова в исходной строке.
# Используйте методы строк и кортежей для обработки данных.
# Пример вывода:
# Введите предложение: Программирование это интересно и полезно
# Длины слов в предложении: (15, 3, 8, 2, 6)

# Функция уберет лишние пробелы
def get_clear_space(text) :
    text = ''.join(text.split())
    return text
# функция создает список спец символов
# Этот список нужен как для вывода на экран для выбора одного или нескольких символов путем их перечисления
def get_list_symbol() :
    list_symbol = []
    ord_start = 33
    ord_end = 127
    while ord_start != ord_end :
        if not chr(ord_start).isalpha() and not chr(ord_start).isnumeric() :
            list_symbol.append(chr(ord_start))
        ord_start += 1
    list_symbol.append(chr(8470))
    return list_symbol

# Функция возвращает True если 'Y' иначе False
def get_yes_no(string) :
    string = str(string).lower().strip()
    while True :
        if string == 'y' :
            return True
        elif string == 'n' :
            return False
        else :
            print("Вы должны ввести только 'Y' или 'N' : ")
            string = input("Слова могут начинаться со спец символов ? Y/N : ")


# Функция строит текст с символами и индексами с выравниванием
# Для более красивого вывода на экран
def get_print_string_index_symbol(symbol_index) :
    string_symbol =''
    index_tmp = ''
    for index,symbol in enumerate(symbol_index) :
        if index + 1 >= 10 :
            string_symbol += symbol + '  '
            index_tmp += str(index + 1)  + ' '
        else:
            string_symbol += symbol + ' '
            index_tmp += str(index + 1) + ' '
    return index_tmp,string_symbol # возвращает кортеж


# Функция возвращает список символов которые нужно удалить
# start_end параметр при значении s - удаляет сначала слова e - в конце слова
def get_symbol_input(start_end) :
    symbol_input = ''
    if start_end != 'null' :
        symbol_input = input('''Введите символы которые нужно исключить либо Enter  
                (0-исключить все
                1 - 10 исключить с 1 по 10 
                ! - %  исключить от ! и до % 
                !"?* - исключение перечисленных ) : ''')
    # Функция получит значения для удаления
    # вернет список символов для удаления
    return get_list_del_symbol(symbol_input, start_end)


# Функция непосредственно удаляет переданные списком символы
# list_symbol список удаляемых символов где index 0 имеет информацию о том откуда удаляем
# s -начало слова e - конец слова и возвращает по одному слову
def get_del_symbol(list_symbol,word) :
    word = str(word)
    index_word = 0
    if list_symbol[0] == 's' :
        index_word = 0
    elif list_symbol[0] == 'e' :
        index_word = -1
    elif list_symbol[0] == 'null':
        word = word
    else:
        print('list_symbol[0] - содержит не известный параметр в def get_del_symbol()')
        # удаляем символы
    for item in range(len(word)):
        for index,symbol in enumerate(list_symbol):
            if word[index_word] == symbol and index > 0 :
                tmp_word = word.replace(symbol, '', 1)
                word = tmp_word
    return word



# Функция создает список удаляемых символов в зависимости от введенных параметров
# второй параметр при значении s - удаляет сначала слова e - в конце слова
def get_list_del_symbol(list_symbol,start_end) :
    str_symbol =str(list_symbol).strip()
    int_symbol = []
    temp_param = ''
    del_symbol = get_list_symbol()

    if len(str_symbol) > 0 :
        # Нужно обработать входящие параметры и понять что в них введено
        if str_symbol[0].isnumeric() or str_symbol[-1].isnumeric() :
            str_symbol = get_clear_space(str_symbol)
            find_minus = str_symbol.find('-')
            len_str_symbol = len(str_symbol)
            # Скорее всего речь идет о цифровом вводе сейчас проверим,
            # узнаем это цифра и все ?
            if str_symbol.isnumeric() :
                int_symbol.extend(del_symbol[int(str_symbol)-1])
            else:
                # если присутствует '-' значит есть признак перечисления и нужно определить что перечисляем
                if str_symbol.count('-') == 1 :
                    # теперь нужен срез, что-бы определить что стоит перед минусом
                    # рассмотрим сначала цифры
                    if find_minus == 0 and str_symbol[1:-1].isnumeric() :
                        int_symbol.extend(del_symbol[ : int(str_symbol[1:])])
                    elif find_minus == len_str_symbol - 1 and str_symbol[-1].isnumeric():
                        int_symbol.extend(del_symbol[int(str_symbol[:find_minus])])
                    elif str_symbol[ : find_minus].isnumeric() and str_symbol[ find_minus + 1 : ].isnumeric():
                        int_symbol.extend(del_symbol[int(str_symbol[ : find_minus ] ) - 1 : int(str_symbol[find_minus + 1 : ])])
                    elif str_symbol[ : find_minus].isnumeric() and not str_symbol[ find_minus + 1 : ].isnumeric():
                        int_symbol.extend(
                            del_symbol[int(str_symbol[: find_minus]) - 1: len(del_symbol) - 1])
                    # Обработаем ситуацию если есть ошибка в воде и в числах есть лишние символы
                    elif not str_symbol[ : find_minus].isnumeric() or not str_symbol[ find_minus + 1 : ].isnumeric() :
                        for num in str_symbol :
                            if not num.isnumeric() and num != '-':
                                temp_param = str_symbol.replace(num,'')
                        int_symbol.extend(del_symbol[int(temp_param[ : temp_param.find('-') ]) : int(temp_param[ temp_param.find('-') + 1 : ])])
                    else :
                        print('Не обработанное исключение при обработке цифр в def get_list_del_symbol()')
        # обработаем ситуацию когда это не цифры
        elif not str_symbol.isalpha() :
            # Значит скорее всего здесь только символы ны нужно в этом убедиться
            # Здесь нужно пробежаться сначала по всей длине и убедиться что нет букв
            # и если есть буквы или цифры то их удалить
            for char in str_symbol :
                if not char.isalpha() and not char.isnumeric()   :
                    temp_param += char
            # переопределим temp_param снова в str_symbol
            str_symbol = temp_param
            find_minus = str_symbol.find('-')
            len_str_symbol = len(str_symbol)
            tmp_string_symbol = ''.join(get_list_symbol()) # для избежания ошибки выхода за пределы
            # массива сделаем из списка строку
            # если есть знак '-' минус и перед ним пробел значит это перечисление
            if str_symbol.count('-') >= 1 :
                # проверим есть ли перед минусом или после него пробел
                # если есть то это явное перечисление
                if len_str_symbol  > 1 :
                    if find_minus == 0 and len_str_symbol  > 1 and  str_symbol[find_minus + 1] == ' ' :
                        # нужно взять срез от этого пробела и почистить от лишних
                        # В этом случае берем только следующий символ после пробела
                        get_clear_space(str_symbol[find_minus])
                        len_str_symbol = len(str_symbol)
                        if len_str_symbol > 1 :
                            # Нужно найти индекс символа
                            tmp =list(tmp_string_symbol[ : tmp_string_symbol.find(str_symbol[-1]) + 1])
                            int_symbol.extend(tmp)
                    elif find_minus == len_str_symbol -1 and str_symbol[find_minus - 1 ] == ' ' :
                        # уберем все пробелы и возьмем нулевой символ если таковой будет не тем минусом который мы нашли
                        get_clear_space(str_symbol[ : find_minus])
                        if str_symbol.find('-') > 0 :
                            tmp = list(tmp_string_symbol[tmp_string_symbol.find(str_symbol[0]) : ])
                            int_symbol.extend(tmp)
                        else:
                            print(' Не обработанное исключение при обработке символов в def get_list_del_symbol() ')
                    elif ( 0 < find_minus < len_str_symbol and str_symbol[find_minus - 1] == ' '
                           and str_symbol[find_minus + 1] == ' ') :
                        # Нужно очистится от пробелов и взять с левой стороны символ от минуса, а с права +1 от минуса
                        str_symbol = get_clear_space(str_symbol)
                        tmp = list(tmp_string_symbol[tmp_string_symbol.find(str_symbol[0]) :
                                                tmp_string_symbol.find(str_symbol[-1]) + 1 ])
                        int_symbol.extend(tmp)
                    # Обработаем ситуацию когда минус не работает как перечисление
                    elif ((find_minus == 0 and str_symbol[find_minus + 1] != ' ') or
                          (find_minus == len_str_symbol - 1 and str_symbol[find_minus - 1] != ' ') or
                          (0 < find_minus < len_str_symbol - 1  and str_symbol[find_minus + 1] != ' ' and
                          str_symbol[find_minus - 1] != ' ' )) :
                        tmp = list(str_symbol)
                        int_symbol.extend(tmp)
                    else:
                        print('Не обработанное исключение при обработке символов как перечисление в get_list_del_symbol')
            # Обработаем ситуацию когда минус не работает как перечисление
            elif str_symbol.count('-') == 0 :
                tmp = list(str_symbol)
                int_symbol.extend(tmp)
            else :
                print('Не обработанное исключение при обработке символов без режима перечисления в get_list_del_symbol')
        else:
            print("Какое-то не обработанное исключение ни цифры не буквы в get_list_del_symbol ")
        if start_end != 's' and start_end != 'e' and start_end != 'null':
            print('В параметре start_end передается не верное значение')
    # Добавим в нулевой индекс значение 's' или 'e' чтоб понимать откуда удалять перечисленные символы сначала или с конца
    int_symbol.insert(0,start_end)
    return int_symbol

# Функция принимает кортеж с длинами слов и возвращает ответ во множественном или единственном числе
# если слово всего одно то кортеж не возвращаем так как получается не очень красивый вывод,
# а если слов больше одного то вернем уже кортеж
def get_return_text_correct(tuple_len_wort) :
    if len(tuple_len_wort) == 1 :
       return f'Найдено только одно слово его длина  : ({tuple_len_wort[0]})'
    elif len(tuple_len_wort) > 1 :
        return  f'Длины слов в предложении : {tuple_len_wort}'
    else:
        return f'Не найдено ни одного слова вы ввели пустую строку или строку содержащую только символы !!!!'



def get_len_list_input(string_inp):
    # разобьем строку на список слов по пробелам
    list_string_inp = str(string_inp).split()
    # узнаем длину списка
    len_list_string_inp = len(list_string_inp)
    if len_list_string_inp < 1 :
        return 0,''
    # вернем длину списка и сам список
    # вернется кортеж
    return len_list_string_inp , list_string_inp

# Функция принимает кортеж с длиной списка и сам список не очищенных от символов слов
# возвращая список уже очищенный от лишних символов
# Также удаляет если 'слово' состоит только из одних символов
def get_clear_symbol(data_tuple,list_del_symbol):
    # Распакуем кортеж и получим с него данные длина списка и сам список
    len_list_string_inp,list_string_inp = data_tuple
    # Начнем перебор по списку для определения является ли словом
    new_list = []
    list_return = []
    if len_list_string_inp < 1 :
        return ''
    else:
        # Проверим не состоит ли слово только из символов
        # Если состоит то исключим его из списка
        for word in list_string_inp :
            # Пробежимся по самому слову
            tmp_char = '' # Сюда пишем слово по символьно нужно для очистки если 'слово' только из символов
            for char in word :
                if not char.isalpha() and not char.isnumeric() :
                    tmp_char += char
            if len(tmp_char) != len(word) :
                new_list.append(word)
        # Теперь бежим по всем словам и удаляем лишнее
        for tmp_word in new_list:
            list_return.append(get_del_symbol(list_del_symbol, tmp_word))
    # Возвращает список слов для подсчета их длины уже без лишних символов
    return list_return


# Функция проверки символов которые могут использоваться в словах
# как пример это символ '-' и '`'
# принимает слово и проверяет его на содержание спец символа
# если после спец символа идет также буква значит это слово
# двух составное иначе нет. Также нужно проверять является ли слово сокращением типа 'т.д.'
# Функция вернет False или True
def get_wort_special_character(word) :
    pass

# Функция принимает список слов, считает количество букв в каждом из слов
# возвращает кортеж длин слов в предложении
# результирующая функция
def get_tuple_count_word(string_inp) :
    date_tmp = get_len_list_input(string_inp)
    len_inp,string_t = date_tmp
    if len_inp == 0 :
        return get_return_text_correct(tuple(range(0)))
    len_word = []
    if not get_yes_no(input("Слова могут начинаться со спец символов ? Y/N : ")) :
        index,symbol = get_print_string_index_symbol(get_list_symbol()) # Вывод символов с индексами на экран для выбора
        print(f'symbol = {symbol}',sep='')
        print(f'index  = {index}',sep='')
        list_word = get_clear_symbol(date_tmp,get_symbol_input('s'))
    else :
        list_word = get_clear_symbol(date_tmp, get_symbol_input('null'))
    # обновим данные так как они могли измениться
    date_tmp = get_len_list_input(' '.join(list_word))
    if not get_yes_no(input("Слова могут заканчиваться на спец символы ? Y/N : ")) :
        index, symbol = get_print_string_index_symbol(
            get_list_symbol())  # Вывод символов с индексами на экран для выбора
        print(f'symbol = {symbol}', sep='')
        print(f'index  = {index}', sep='')
        list_word = get_clear_symbol(date_tmp, get_symbol_input('e'))

    else:
        list_word = get_clear_symbol(date_tmp, get_symbol_input('null'))
    # Посчитаем длины и сохраним их в список
    for l_word in list_word :
        len_word.append(len(l_word))
    return get_return_text_correct(tuple(len_word))


string_input = input(f'\033[33mВведите предложение : \033[0m')
print(get_tuple_count_word(string_input))


# добавить в список символ №
