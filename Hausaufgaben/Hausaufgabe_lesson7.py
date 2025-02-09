# Напишите программу, которая запрашивает у пользователя три числа
# и выводит их в порядке возрастания, разделенные запятой.
# Используйте условные операторы и вложенные условия для решения задачи.
# Предполагается, что все три числа различны.

number1 = int(input('Enter one number  : '))
number2 = int(input('Enter two number  : '))
number3 = int(input('Enter three number  : '))

if number2 < number1 > number3 :
    if  number2 > number3 :
        print( number3,number2,number1,sep = ',')
    else : print(number2,number3,number1 ,sep = ',')
elif number1 < number2 > number3 :
    if number1 > number3 :
        print(number3 , number1 ,number2 ,sep = ',')
    else : print(number1,number3,number2 ,sep = ',')
elif number1 < number3 > number2  :
    if number1 > number2 :
        print(number2 ,number1 ,number3 ,sep = ',')
    else : print(number1 ,number2 ,number3 ,sep =',' )

# Напишите программу, которая запрашивает у пользователя год и проверяет, является ли он високосным.
# Год является високосным, если он делится на 4 без остатка, но не делится на 100 без остатка,
# за исключением годов, которые делятся на 400 без остатка. Выведите соответствующее сообщение
# на экран с помощью команды print.

year = int(input('Enter Year : '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print(f'{year} Год високосный')
else: print(f'{year} Год не високосный')




