#  Напишите программу, которая генерирует и выводит квадраты чисел
#  от 1 до N с использованием генераторного выражения.
#  Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и использует
#  генераторное выражение для генерации квадратов чисел. Затем выведите квадраты чисел на экран.
#  Пример работы программы:
# 1
# 4
# 9
# 16
# 25

# Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

def get_num_input(num_task) :
    try:
        if num_task == 1 :
            int_input = int(input('Введите количество чисел : '))
            return int_input
        elif num_task == 2 :
            int_input = int(input('Введите количество чисел Фибоначчи: '))
            return int_input
    except (TypeError ,ValueError) :
        print('Вы должны ввести только целое число ')

def generate_squares(n) :
    try:
        if n > 0 :
            yield from (num ** 2 for num in range(1,n+1))
        else :
            raise ValueError ('Число должно быть больше нуля')
    except ValueError as e :
        print(e)

print_task_number(1)

for sqr_tmp in generate_squares(get_num_input(1)) :
    print(sqr_tmp)




# 2. Напишите генератор, который будет генерировать бесконечную
# последовательность Фибоначчи. Каждый раз, когда генератор вызывается,
# он должен возвращать следующее число последовательности. Напишите программу,
# которая будет использовать этот генератор для вывода первых N чисел Фибоначчи.
# Пример вывода:
# Введите количество чисел Фибоначчи: 10
# Первые 10 чисел Фибоначчи:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


def get_infinite_fibonacci_sequence() :
    fibo1, fibo2 = 0, 1
    while True :
        yield fibo1
        fibo1, fibo2 = fibo2, fibo1 + fibo2

def print_count_fibo(count_num) :
    try :
        if count_num > 0 :
            it = get_infinite_fibonacci_sequence().__iter__()
            for i in range(count_num) :
                print(next(it))
        else:
            raise ValueError ('Введенное число должно быть больше нуля ')
    except ValueError as e:
        print(e)
    except TypeError :
        print('Не верное значение count_num')




print_task_number(2)
print_count_fibo(get_num_input(2))

