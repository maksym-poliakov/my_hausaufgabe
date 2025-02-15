import  json
import  random
# 1. Напишите программу, которая открывает файл, считывает из него
# два числа и выполняет операцию их деления. Если число отрицательное,
# выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

# Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text


file_name = 'two_number.json'

# Обработчик ошибки num_task вызывает ошибку ValueError
def task_error(num_task) :
    if num_task != 2 and num_task != 1:
       raise ValueError
# Создам файл json
# файл пересоздается каждый раз при запуске
# параметр num_task принимает значение 1 или 2
# эти значения означают для какого задания создать файл
def create_data_file(f_name,num_task):

    start_num1 = 0
    start_num2 = 0
    end_num= 10
    try:
        task_error(num_task)
    except ValueError :
        print(f'Не верное значение параметра num_task = {num_task} func : create_data_file')
    else:
        if num_task == 1:
            start_num1 = -1
            start_num2 = 1
        elif num_task == 2:
            start_num1 = -1
            start_num2 = 0
            end_num = 1
        data_number = {'num1' : random.randint(start_num1 ,end_num ),'num2' : random.randint(start_num2 ,end_num)}
        with open(f_name,'w') as file :
            json.dump(data_number,file,ensure_ascii=False,indent=4)

# Функция принимает json файл
# в котором лежат 2 числа, проверки
# число это или нет не делаются
def get_deviation_num(json_file):
    try:
        with open(json_file,encoding='utf-8') as file :
            data_number = json.load(file)
    except FileNotFoundError :
        print(f'Файла: {json_file} не существует func ')
    else :
        num1 = data_number.get('num1')
        num2 = data_number.get('num2')
        try:
            if num1 < 0 or num2 < 0 :
                raise ValueError
            result = num1 / num2
            return num1, num2, result
        except ValueError :
            print("Число должно быть положительным")

# функция возвращает результат вычисления
def print_result(tuple_result,task_num):
    if tuple_result:
        try:
            task_error(task_num)
            if task_num == 1:
                num1,num2,result = tuple_result
                return f'{num1} / {num2} = {round(result,2)}'
            if task_num == 2:
                num1 ,num2,deviation,summ,subtraction = tuple_result
                result_deviation = f'{num1} / {num2} = {round(deviation,2)}\n'
                result_summ = f'{num1} + {num2} = {summ}\n'
                result_subtraction  = f'{num1} - {num2} = {summ}\n'
                return result_deviation + result_summ + result_subtraction
        except ValueError :
            print(f'Не верное значение параметра num_task = {task_num} func : print_result')

    return ''

print(print_task_number(1))
create_data_file(file_name,1)
print(print_result(get_deviation_num(file_name),1))

# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет
# операции над числами в файле. Обработайте возможные исключения
# при открытии файла (FileNotFoundError) и при выполнении операций
# над числами (ValueError, ZeroDivisionError).
# Используйте конструкцию try-except-finally для обработки исключений и
# закрытия файла в блоке finally.

def mathematical_operations(json_file):
    file = None
    try:
        file = open(json_file,encoding='utf-8')
        data = json.load(file)
        num1 = data.get('num1')
        num2 = data.get('num2')

        if isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
            summ = num1 + num2
            subtraction = num1 - num2
            deviation = round(num1 / num2, 2)
            return num1,num2,deviation ,summ ,subtraction
        else :
            raise ValueError
    except FileNotFoundError :
        print('Файл не существует !')
    except ValueError :
        print('Не верные данные !')
    except ZeroDivisionError :
        print('Ошибка деления на ноль !!')
    finally:
        file.close()

print(print_task_number(2))
create_data_file(file_name,2)
print(print_result(mathematical_operations(file_name),2))