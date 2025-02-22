#  Напишите генератор, который будет принимать на вход числа и
#  возвращать их сумму. Генератор должен использовать инструкцию yield
#  для возврата текущей суммы и должен продолжать принимать новые числа для
#  добавления к сумме. Если генератор получает на вход число 0,
#  он должен прекращать работу и вернуть окончательную сумму. Напишите программу,
#  которая будет использовать этот генератор для пошагового расчета суммы чисел,
#  вводимых пользователем.
# Пример вывода:
# Введите числа для суммирования (0 для окончания):
# Введите число: 3
# Текущая сумма: 3
# Введите число: 5
# Текущая сумма: 8
# Введите число: 2
# Текущая сумма: 10
# Введите число: 0
# Текущая сумма: 10

# Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

# Вечный генератор
def get_int_input() :
    value = yield
    while True :
        summ = yield value
        value += summ

def get_total_sum():
    int_input = None
    summ = 0
    while int_input != 0 :
        int_input = int(input('Введите число:'))
        if int_input != 0 :
            print(f'Текущая сумма: {gen.send(int_input) }')
        else:
            summ = gen.send(int_input)
            gen.close()
    return f'Текущая сумма: {summ}'

print(print_task_number(1))
print('Введите числа для суммирования (0 для окончания) :')
gen = get_int_input().__iter__()
gen.__next__()
print(get_total_sum())

# 2. Напишите генератор, который будет генерировать
# бесконечную арифметическую прогрессию.
# Он должен принимать начало прогрессии (необязательно,
# если не передано, то старт с 1) и шаг прогрессии



def get_generator_regression(start,step):
    while True :
        yield start
        start += step


def print_generator(start_regression = 1 ,*,step_regression,count) :
    gen1 = get_generator_regression(start_regression, step_regression).__iter__()
    for _ in range(count):
        print(gen1.__next__())

print(print_task_number(2))
print_generator(step_regression=4,count=10)

