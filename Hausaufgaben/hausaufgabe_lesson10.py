import random
# Напишите программу, которая генерирует случайное число от 1 до 100,
# а затем предлагает пользователю угадать это число. Если пользователь угадывает число,
# программа выводит сообщение о победе. Если пользователь не угадывает число, программа сообщает,
# больше или меньше загаданное число и предлагает попробовать снова.
# Используйте цикл с инструкцией break, чтобы остановить выполнение цикла, когда число угадано.

# num = random.randint(1,100)
# res = int(input('Guess a number from 1 to 100 : '))
# while True :
#     if res != num and num > res and 1 <= res <= 100:
#         print('the number guessed is higher')
#         res = int(input('try again :'))
#         continue
#     elif res != num and num < res and 1 <= res <= 100 :
#         print('the number guessed is less')
#         res = int(input('try again :'))
#         continue
#     elif 1 < res > 100 :
#         print('the number must be between 1 and 100')
#         res = int(input('Guess a number from 1 to 100 : '))
#         continue
#     else :
#         print(f'Congratulations! You guessed the number {num}!')
#         break


# Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи.
# Числа Фибоначчи - это последовательность чисел, где каждое следующее число является суммой двух предыдущих
# чисел (начиная с 0 и 1). Используйте цикл while для решения задачи.
# Выведите числа через запятую с помощью команды print.

num1 = int(input('enter int number : '))
print(f'The first {num1} Fibonacci numbers:')
i = 0
fibo1 ,fibo2 = 0 , 1
while i < num1:
    if i > 0 :
        print(", ", end="")
    print(fibo1,end="")
    fibo1, fibo2 = fibo2 , fibo1 + fibo2
    i += 1

# решение на уроке чисел фибоначи
while True:
    n = int(input("Введите количество числе Фибоначчи: "))
    f1, f2 = 0, 1
    count = 0 # счетчик
    while count < n:
        if count == 0:
            print(f1, end='') # end по умолчанию переводит на новую строку.
        else:
            print(f', {f1}', end='')
        f1, f2 = f2, f1 + f2
        count += 1
    print()

# Решение неадекватки
while True: #
    num = int(input("Enter a number: ")) # Запрос ввода числа от пользователя
    a, b = 0, 1 #Инициализация первых двух чисел последовательности Фибоначчи
    count = 0 #Счётчик, который будет отслеживать количество уже сгенерированных чисел
    print("First", num, "numbers of Fibonacci series:", end="") #Выводит заголовок перед последовательностью end="" предотвращает автоматический перевод строки после заголовка
    while count < num: # Внутренний цикл для генерации чисел Фибоначчи. Будет работать, пока количество сгенерированных чисел меньше запрошенного
        print(a, end="" if count == num - 1 else ", ") # Выводит текущее число последовательности end="" для последнего числа (без запятой)", " между числами (с запятой)
        a, b = b, a + b #Ключевая строка для генерации чисел Фибоначчи
        count += 1
    ask = input("\nWould You like to enter another number (y/n)?:")
    if ask == "n":
        print("Goodbye")
        break
# Напишите программу, которая запрашивает у пользователя целое положительное число и проверяет,
# является ли оно простым. Простое число - это число, которое делится только на 1 и на само себя без остатка.
# Используйте цикл while и проверку деления числа на все числа от 2 до N-1 для решения задачи.
# Выведите соответствующее сообщение на экран с помощью команды print.

# num = int(input('enter int number : '))
# i = 1
# count = 0
# while i <= num :
#     if num == 1 :
#         print(f'number {num} is not prime ')
#         break
#     elif num % i == 0 :
#         count += 1
#         i += 1
#     elif  num % i != 0 :
#         i += 1
#         if  count > 2  :
#             print(f'number {num} is not prime ')
#             break
# else :
#     print(f'number {num} is prime ')


