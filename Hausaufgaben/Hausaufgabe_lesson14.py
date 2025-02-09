# Напишите программу, которая запрашивает у пользователя целое число и определяет,
# является ли оно палиндромом. Число является палиндромом, если оно читается одинаково
# слева направо и справа налево. Выведите соответствующее сообщение на экран с помощью команды print.
# Используйте математические операции. Работу со строками использовать нельзя.

number = int(input('Enter number : '))
count_number = 0 # счетчик для количества цифр
number_tmp, number_tmp1 = number,number
number_tmp2,number_tmp3 = -1,-1 # для временных расчетов
number_one = number # для первой цифры в числе
x = 1 #
while True :
    if 0 <= number < 10: # число от 0 до 9 по любому палиндром
        print(f'The number {number} is a palindrome')
        break
    elif number < 0: # отрицательное число не может быть палиндром
        print('Error! The number cannot be less than zero. Enter the correct number.')
        number = int(input('Enter number : '))
        continue
    else:
        if number >= 0 :
            while number_tmp > 0 : # посчитаем в цикле сколько цифр в числе
                count_number += 1
                number_tmp //= 10
            x *= 10 **  (count_number - 1) # возведем х в степень count_number - 1 для вычисления первого числа
            while x > 1 :
                number_tmp2 = number_tmp1 % 10  # вычислим последнее число
                number_tmp3 = number_one // x  # вычислим первое число
                if number_tmp2 != number_tmp3: # сравним первое с последним и если они не равны то не палиндром
                    print(f'The number {number} is not palindrome')
                    break
                number_one = number_one - number_tmp3 * x # откинем первую цифру
                x = x / 10 # так как число уменьшилось на одну цифру спереди уменьшим х на один разряд
                number_tmp1 //= 10 # откинем последнюю цифру
            else:
                print(f'The number {number} is a palindrome')
        break

# Напишите программу, которая запрашивает у пользователя целое число и проверяет,
# является ли оно числом Армстронга. Число Армстронга - это число, которое равно сумме своих цифр,
# возведенных в степень, равную количеству цифр в числе. Выведите соответствующее сообщение на экран
# с помощью команды print.

number = int(input('Enter int number : '))
count_number = 0
number_tmp, number_tmp2= number,number
sum_number = 0
number_power =0
while True  :
    if number < 0 :
        print('Error! The number cannot be less than zero. Enter the correct number.')
        number = int(input('Enter number : '))
        continue
    while number_tmp > 0:
        number_tmp //= 10
        number_power += 1
    number_tmp, number_tmp2 = number,number # переопределю переменные
    while count_number < number_power :
        number_tmp2 = number_tmp % 10
        sum_number += number_tmp2 ** number_power
        number_tmp //=10
        count_number += 1
    if number == sum_number :
        print(f'The number {number} is an Armstrong number. ')
        break
    else :
        print(f'The number {number} is not an Armstrong number. ')
        break



