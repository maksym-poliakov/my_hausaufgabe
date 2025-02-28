import sys
import os

# 1. Напишите программу, которая принимает в качестве аргумента командной
# строки путь к файлу .py и запускает его. При запуске файла программа должна
# выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен, программа должна вывести соответствующее
# сообщение об ошибке.
#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

# args = sys.argv
# if os.path.exists(args[1]):
#     if os.path.isfile(args[1]):
#         if args[1][-3:] == ".py":
#             os.system(f'python {args[1]}')
#             print(f'Файл {args[1]} успешно запущен')
#         else:
#             print('Файл не имеет расширения .py ')
#     else:
#             print('Это не файл ')
# else:
#     print(f'Файла {args[1]} не существует ')

print(print_task_number(1))
# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории
# и выводит список всех файлов и поддиректорий внутри этой директории.
# Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

args = sys.argv
os.chdir(args[1])
cur_dir = os.getcwd()

if os.path.exists(cur_dir ):
    if os.path.isdir(cur_dir ):
        for root, dirs, files in os.walk(cur_dir):
            for dir_ in dirs :
                print(os.path.join(root,dir_))
            for file in files :
                print(os.path.join(root, file))
    else :
        print('Это не каталог ')
else :
    print('Такого пути не существует ')

print(print_task_number(2))