# Напишите программу, которая запрашивает у пользователя натуральное десятичное число
# и выводит его двоичное представление. Реализуйте алгоритм перевода числа в двоичную систему счисления,
# используя основные концепции представления чисел (подсказка: через деление с остатком).
# Выведите полученное представление числа на экран.
# num_int = int(input('Enter natural decimal number : '))
# str_bin = ''
# while num_int > 0 :
#     rez = num_int % 2
#     str_bin = str(rez) + str_bin
#     num_int = num_int // 2
# print(str_bin)

# Напишите программу, принимающую число с плавающей точкой и округляющую его до целого числа
# в соответствии с правилами школьной математики. Использовать модуль math и методы из него нельзя.
# Учесть, что программа должна корректно работать с отрицательными числами.

# Первый вариант решения

# num_decimal = float(input('Enter decimal number : '))
# # int_num = 0
# if num_decimal < 0 :
#     num_decimal *= -1
#     num1  =  num_decimal - int(num_decimal)
#     if num1 >= 0.5 :
#         int_num = (int(num_decimal) +1) * (-1)
#     else:
#         int_num = int(num_decimal)  * (-1)
# else:
#     num1 = num_decimal - int(num_decimal)
#     if num1 >= 0.5:
#         int_num = int(num_decimal) + 1
#     else:
#         int_num = int(num_decimal)
# print(f'Circle numer : {int_num } ')
#
# # Второй вариант решения
num_decimal = float(input('Enter decimal number : '))
minus_flag = False
if num_decimal < 0 :
    minus_flag = True
num_decimal_abs = abs(num_decimal)
num1 = num_decimal_abs - int(num_decimal_abs)
if num1 >= 0.5 :
    num_circle = int(num_decimal_abs) + 1
else:
    num_circle = int(num_decimal_abs)
if minus_flag :
    num_circle *= -1
print(f'Circle numer : {num_circle } ')
