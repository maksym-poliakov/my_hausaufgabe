import os
from datetime import datetime

# 1. Напишите программу, которая запрашивает у пользователя число N и выводит на экран
# таблицу умножения от 1 до N. Используйте вложенный цикл for для создания таблицы умножения.
# Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите число N: 5
print ('ЗАДАНИЕ № 1')
int_inp = int(input('Enter integer number : '))
int_range = int_inp + 1
for number in range(1,int_range) :
    print (number,end=' ')
    for item in range(2,int_range) :
        print(item * number,end=' ')
    print('\n')

# 2. Напишите программу, которая принимает два списка одинаковой длины и создает новый список,
# содержащий пары элементов из исходных списков. Используйте функцию zip()
# для создания пар элементов. Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите элементы первого списка, разделенные пробелом: 1 2 3 4 5
# Введите элементы второго списка, разделенные пробелом: A B C D E
# Список пар элементов: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
print ('ЗАДАНИЕ № 2')
print('''Пример ввода данных : 1 2 3 4 5
                      A B C
\033[91mПотерянные данные будут записаны в файл\033[0m ''')
file_log = 'log_file.txt'
log_text =''
file_encoding = 'utf-8'
while True :
    # Создадим log_file если его еще нет
    if not os.path.exists(file_log):
        with open(file_log,'w',encoding=file_encoding) as file:
            file.write('')
    while True :
        string_inp1 = input('Enter the items of the first list, separated by spaces : ').strip()
        if not string_inp1.replace(' ','').isnumeric() :
            print(' '.join('\033[31mThe first list must be integer only ! \033[0m'.split()))
            log_text += str(datetime.now())  + ' Ошибка ввода первых данных' + ' код 001' + '\n'
            continue
        break
    while True:
        string_inp2 = input('Enter the items of the second list, separated by spaces : ').upper().strip()
        if not string_inp2.replace(' ','').isalpha() :
            print('\033[31mThe second list should contain only letters ! \033[0m')
            log_text += str(datetime.now()) + ' Ошибка ввода вторых данных' + ' код 001' + '\n'
            continue
        break
    len_list1 = len(string_inp1.split())
    len_list2 = len(string_inp2.split())
    list1 = string_inp1.split()
    list2 = string_inp2.split()
    string_tmp =''
    count1 = 0
    count2 = 0
    count_tmp = 0
    if len_list1 != len_list2 :
        print('\033[93mAttention ! Some data will be lost !'.strip())
        if len_list2 > len_list1 :
            count1 = len_list2 - len_list1
            count_tmp = count1
            print(f'There are \033[1;31m{count1}\033[93m less elements in the first list. '
                  f'\033[0m')
            log_text += str(datetime.now()) + ' Потеря части вторых данных' + ' код 002' + '\n'
        else:
            count2 = len_list1 - len_list2
            count_tmp = count2
            print(f'\033[93mThere are \033[1;31m{count2}\033[93m fewer elements in the second'
                               f' list.\033[0m')
            log_text += str(datetime.now()) + ' Потеря части первых данных' + ' код 002' + '\n'
        while True :
            file_name = 'lost_data'
            file_format = '.txt'
            absolute_path = os.path.abspath(file_name + file_format)
            selection_inp = input('Write lost data to file? Y/N : ').lower().strip()
            if selection_inp == 'y' :
                if not os.path.exists(file_name + file_format) :
                    print(f'File with name \033[34m{file_name + file_format}\033[0m successfully created!')
                    print(f'File path : \033[34m{absolute_path}\033[0m')
                else :
                    print(f'\033[34mThe file : {file_name + file_format} will be overwritten !')
                    while True :
                        selection_inp1 = input('Overwrite \033[31m" Y - rewrite old file "\033[34m new file\033[31m '
                                               '" N - new name file "\033[0m : ').lower().strip()
                        if selection_inp1 == 'y' :
                            log_text += (str(datetime.now()) + f' Перезапись данных в файл : {file_name + file_format}'
                                        + ' код 003' + '\n')
                            break
                        elif selection_inp1 == 'n' :
                            file_name = file_name + '_' + str(int(datetime.now().strftime("%Y%m%d%H%M%S")))
                            log_text += (str(datetime.now()) + f' Запись данных в новый файл {file_name + file_format}'
                                        + ' код 005' + '\n')
                            break
                        else:
                            print('\033[31mYou must enter only Y or N \033[0m')
                            log_text += (str(datetime.now()) + ' Не верный ввод Y/N'+
                                         ' код 001' + '\n')
                    absolute_path = os.path.abspath(file_name + file_format)
                    print(f'File path: \033[34m{absolute_path}\033[0m')
                with open(file_name + file_format,'w') as file :
                    if count1 > 0:
                        for item in range(len_list2 - count_tmp,len_list2 ) :
                            string_tmp += list2[item] + ' '
                    else :
                        for item in range(len_list1 - count_tmp,len_list1 ) :
                            string_tmp += list1[item] + ' '
                    file.write(f'Lost data : {','.join(str(string_tmp).split())}')
                    if selection_inp == 'y' :
                        print(f'file : {file_name + file_format} successfully overwritten\n'
                              f'File path : {absolute_path}\033[0m')
                break
            elif selection_inp == 'n' :
                break
            else:
                print('\033[31mYou must enter only Y or N \033[0m')
    zipped = zip(list1,list2)
    print(f'Transformed data : {list(zipped)}')
    string_inp1 = input('Enter new data ? Y/N : ').lower().strip()
    if string_inp1 == 'y' :
        log_text += (str(datetime.now()) + ' Новый ввод данных' + ' код 005' + '\n')
        # Выгрузим данные в file_log чтоб не тягать с собой кучу данных
        if os.path.exists(file_log) :
            with open(file_log,'a',encoding=file_encoding) as file : # открою/закрою файл для добавления записей в файл
                file.write(log_text) # Добавляем строки
                file.flush()
        else:
            print(f'log file : {log_text} not found!')
        continue
    elif string_inp1 == 'n' :
        log_text += (str(datetime.now()) + ' Завершение работы программы' + ' код 006' + '\n')
        if os.path.exists(file_log) :
            with open(file_log,'a',encoding=file_encoding) as file : # открою/закрою файл для добавления записей в файл
                file.write(log_text) # Добавляем строки
            # Открою файл на чтение и посчитаю строки
            with open(file_log,'r',encoding=file_encoding) as f :
                count_tmp = len(f.readlines())
        else:
            print(f'log file : {file_log} not found!')
        break
    else:
        string_inp1 = input('\033[31mEnter only Y or N : \033[0m').lower().strip()
        log_text += (str(datetime.now()) + ' Не верный ввод Y/N' +' код 001' + '\n')
print(f'Number of lines in : {file_log} = {count_tmp}')

# list_start = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
# list_num , list_str = zip(*list_start)
# print (' '.join([str(num) for num in list_num]) + '\n' + ' '.join(list(list_str)))

