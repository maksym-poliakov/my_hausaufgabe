# 1. Напишите программу, которая принимает два числа и возвращает их сумму и
# произведение в виде кортежа (sum, product).
# Используйте функцию для вычисления суммы и произведения.
# Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите первое число: 3
# Введите второе число: 4
# Сумма и произведение чисел: (7, 12)

def matematik(number) :
    number_1,number_2 = number
    result = []
    result_sum = number_1 + number_2
    result.append(result_sum)
    result_product = number_1 * number_2
    result.append(result_product)
    return f'Сумма и произведение чисел : {tuple(result)}'

print(matematik(map(int,input('Enter 2 number : ').split()) ))

# 2. Напишите программу, которая принимает список чисел и возвращает сумму, минимальное
# и максимальное значение из списка. Используйте функцию для обработки списка чисел
# и возврата трех значений. Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите числа:  3, 7, 2, 9, 1, 5
# Сумма чисел: 27
# Минимальное значение: 1
# Максимальное значение: 9


def matematik_2(list_param) :
    tmp =[]
    for item in list_param :
        tmp.append(int(item))
    sum_item = sum(tmp)
    min_item = min(tmp)
    max_tmp = max(tmp)
    return f'''Сумма чисел : {sum_item}
Минимальное значение : {min_item}
Максимальное значение : {max_tmp}'''
print(matematik_2(input('введите список чисел через запятую : ').split(',')))






