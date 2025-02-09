import random

# 1. Напишите программу, которая принимает матрицу (вложенный список) от пользователя и
# находит сумму всех элементов в матрице. Используйте вложенные списки и
# циклы для обхода элементов матрицы.
# Пример матрицы: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Пример вывода:
# Сумма элементов в матрице: 45

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Шапка для отделения заданий
def print_task_number(task_numb) :
    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text
# Функция возвращает True если 'Y' иначе False
def get_yes_no(string) :
    string = str(string).lower().strip()
    while True :
        if string == 'y' :
            return True
        elif string == 'n' :
            return False
        else :
            string = get_data_input(get_clear_text("Вы должны ввести только 'Y' или 'N' : "),
                                    'str','str')


# Функция чистит текст от лишних пробелов
# Текст для сообщений можно вводить не обращая внимания на лишние пробелы
# они очистятся, но недостающие не добавятся !!!
def get_clear_text(text) :
    text = ' '.join(str(text).split())
    return text

# Ввод данных принимает
# type_data = float , int ,str
# type_str = str,list
def get_data_input(text,type_data,type_str) :
    if type_data.lower() == 'float'  and type_str.lower() == 'list':
        return list(map(float,input(get_clear_text(text)).strip().split()))
    elif type_data.lower() == 'int'  and type_str.lower() == 'list':
        return list(map(int, input(get_clear_text(text)).strip().split()))
    elif type_data.lower() == 'str'  and type_str.lower() == 'list':
        return list(input(get_clear_text(text)).strip().split())
    elif type_data.lower() == 'str' and type_str.lower() == 'str':
        return input(get_clear_text(text)).strip()
    elif type_data.lower() == 'int' and type_str.lower() == 'int':
        return int(input(get_clear_text(text)))
    else :
        print(f'Комбинация {type_data.lower()} / {type_str.lower()} не предусмотрена !!!!')



# Функция создает матрицу из введенных данных
def get_date_matrix() :
    return_matrix =[]
    while True :
        matrix_inp = get_data_input('Введите   числа  через    пробел (Enter выход) : ',
                                    'float','list')
        if not matrix_inp   :
            break
        while True :
            if not get_correct_matrix(matrix_inp, return_matrix):
                print(get_clear_text(f'\033[31mОшибка ввода !!! Размер введенных данных не совпадает !!! \033[0m '))
                matrix_inp = get_data_input(f'\033[31mВведите данные из {get_correct_ending(len(return_matrix[0]
                                                                        ))}\033[0m','float','list')
                continue
            break
        if get_correct_matrix(matrix_inp, return_matrix) :
            return_matrix.append(matrix_inp)
    return return_matrix


# Функция возвращает True если длина матрицы одинаковая и False если разная.
# Принимает вводимые пользователем данные и возвращаемые данные
# из функции get_input_matrix()
def get_correct_matrix(matrix_i,matrix_ind) :
    if len(matrix_ind) == 0 :
        return True
    else:
        len_matrix_ind = len(matrix_ind[0])
        len_matrix = len(matrix_i) # получим длину первого элемента матрицы
        if len_matrix_ind == len_matrix :
            return True
    return False


# Функция возвращает результат сложения
def get_summ_matrix(matrix_inp) :
    sum_matrix = sum([element for num_element in matrix_inp for element in num_element ])
    return get_result_correct(sum_matrix)


def get_correct_ending_numbers(str_number) :
    list_endings = [' - го числа : ', ' - х чисел : ', ' - ти чисел : ', ' - ми чисел : ', ' - ка чисел : ',
                    ' - та  чисел : ', ' - от  чисел : ',' - чи чисел : ', ' - ч чисел : ']
    if len(str_number) == 1 :
        if  int(str_number[0]) == 1:
            return f' {list_endings[0]} '
        elif 1 <  int(str_number[0]) < 5:
            return f' {list_endings[1]} '
        elif 4 < int(str_number[0]) < 7 or 8 <  int(str_number[0]) < 20:
            return f' {list_endings[2]} '
        elif 6 < int(str_number[0]) < 9:
            return f' {list_endings[3]} '
    if len(str_number) == 2:
        if int(str_number[0]) == 4 and int(str_number[-1]) == 0:
            return f' {list_endings[4]} '
        elif not int(str_number[0]) and int(str_number[-1]) == 0 :
            return f' {list_endings[2]} '
    if len(str_number) == 3:
        if int(str_number[0]) == 1 and int(str_number[-1]) == 0:
            return f' {list_endings[5]} '
    elif 1 < int(str_number[0]) < 10 and int(str_number[-1]) == 0:
        return f' {list_endings[6]} '
    if len(str_number) == 4:
        if int(str_number[0]) == 1 and int(str_number[-1]) == 0:
            return f' {list_endings[7]} '
        elif 1 < int(str_number[0]) < 10 and int(str_number[-1]) == 0:
            return f' {list_endings[8]} '
    return ''


# Функция выводит корректное окончание для верного числа данных.
# Возвращает корректный текст с числом
def get_correct_ending(len_dat) :
    len_dat = int(len_dat)
    str_number = str(len_dat)
    len_str_number = len(str_number)
    # Добавим нули к числу str number
    if len_str_number > 1 :
        str_tmp = '1'.ljust( len_str_number,'0')
    else:
        str_tmp = '10'
    int_str_tmp = int(str_tmp)
    return_text =''
    while return_text == '' :
        result_divisions = len_dat % int_str_tmp
        return_text = get_correct_ending_numbers(str(result_divisions))
        int_str_tmp %= 10
    return  f' {len_dat} {return_text} '


# Функция возвращает результат в виде целого числа если нет дробной части больше нуля
def get_result_correct(sum_m) :
    if type(sum_m) is float or type(sum_m) is int:
        result_summ = sum_m - int(sum_m)
        if result_summ == 0 :
            return get_clear_text(f'\033[32mСумма элементов в матрице : {int(sum_m)}\033[0m')
        return get_clear_text(f'\033[32mСумма элементов в матрице : {sum_m}\033[0m')
    elif type(sum_m) is list :
        number_correct = []
        [number_correct.append(int(numb)) if numb - int(numb) == 0 else number_correct.append(numb) for numb in sum_m ]
        return number_correct


# Функция создает список элементов матрицы с рандомными значениями
# Если plus_element = 0 то идет одинаковое заполнение матрицы
# Если нужно допустить ошибку в заполнении данных plus_element должен быть > 0
def get_random_element(count_element,plus_element) :
    auto_element = []
    [auto_element.append(random.choice(range(1, 10000))) for item in range(count_element + plus_element)]
    return auto_element

# Результирующая функция.
# Возвращает результат выполнения программы
def main() :
    if get_yes_no(get_data_input('Заполнить матрицу автоматически ? Y/N : ','str','str')) :
        count_element_matrix = get_data_input('Количество элементов в матрице : ','int','int')
        count_matrix = get_data_input('Сколько матриц создать ? : ','int','int')
        matrix_data = []
        # Исключим возможность установить ноль так как базовая матрица будет в любом случае
        if count_matrix == 0 :
            count_matrix = 1
        # создаем первые данные матрицы
        matrix_data.append(get_random_element(count_element_matrix,0))
        print(f'Матрица {len(matrix_data)} успешно заполнена')
        while len(matrix_data) < count_matrix:
            if get_yes_no(get_data_input('Допустить ошибку в заполнении матрицы ? Y/N : ',
                                         'str', 'str')) :
                matrix_data.append(get_random_element(count_element_matrix, 1))
                while not get_correct_matrix(matrix_data, matrix_data) :
                        print(get_clear_text(f'\033[31mОшибка ввода !!! Размер введенных данных не '
                                             f'совпадает !!! \033[0m '))
                        print(get_clear_text(f'\033[31mДанные должны состоять из {get_correct_ending(len(matrix_data[0]
                                                                                                         ))} \033[0m'))
                        if get_yes_no(get_data_input(f'\033[31mЗаполнить верными данными Y/N ? : '
                                                     f'\033[0m' ,'str', 'str')) :
                            matrix_data.pop(-1)
                            matrix_data.append(get_random_element(count_element_matrix, 0))
                            print(f'Матрица {len(matrix_data)} успешно заполнена')
                            break
            else:
                matrix_data.append(get_random_element(count_element_matrix, 0))
                print(f'Матрица {len(matrix_data)} успешно заполнена')
        return get_summ_matrix(matrix_data)
    else :
        return get_summ_matrix(get_date_matrix())

# Выводит в консоль № Задания
print(print_task_number(1))
# Вывод в консоль результата выполнения программы
print(main())




# 2. Напишите программу, которая принимает список чисел от пользователя и сортирует его в
# порядке убывания, используя метод sort() и параметр reverse=True.
# Выведите отсортированный список на экран.
# Пример вывода:
# Введите список чисел, разделенных пробелами: 5 2 8 1 3
# Отсортированный список чисел: [8, 5, 3, 2, 1]

# Примеры ввода: 1 1.1 2.8 2
#                10 3 5 18

# Функция сортирует введенные числа как float, так и int.
# Принимает False или True. По умолчанию False
def get_sort_number(revers = False) :
    list_number = get_data_input('Введите список чисел, разделенных пробелами : ','float','list')
    sort_number = sorted(get_result_correct(list_number),reverse=revers)
    return sort_number

# Выводит в консоль № Задания
print(print_task_number(2))
# Вывод в консоль результата выполнения программы
print(get_sort_number(True))
