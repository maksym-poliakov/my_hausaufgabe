# 1. Напишите программу, которая запрашивает у пользователя его имя, возраст и место проживания,
# а затем выводит их в следующем формате:
# "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}."
# Вместо {0}, {1} и {2} подставьте соответствующие значения. Используйте метод format()
# для форматирования строки. Потом попробуйте использовать f-строку. Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите ваше имя: Alice
# Введите ваш возраст: 25
# Введите ваше место проживания: London
# Привет, меня зовут Alice. Мне 25 лет. Я живу в London.

string_name = input('Enter Name : ').strip().capitalize()
int_age = input('Enter Age : ').strip()
string_city = input('Enter City : ').strip().capitalize()
string_tmp = ' '.join('Hallo, my Name : {0}. My Age : {1}. I live in : {2} '
                      .format(string_name,str(int_age),string_city).split())
string_tmp1 = ' '.join(f'Hallo, my Name : {string_name}. My Age : {str(int_age)}. I live in : {string_city}'.split())
print(string_tmp)
print(string_tmp1)



# 2. Напишите программу, которая запрашивает у пользователя два числа и выводит
# их сумму и произведение в следующем формате:
# "Сумма: {sum:.2f}, Произведение: {product:.2f}"
# Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения, округленные до двух десятичных знаков.
# Используйте f-строки с использованием форматных спецификаторов для форматирования чисел. Выведите результат
# на экран с помощью команды print.
# Пример вывода:
# Введите первое число: 3.14159
# Введите второе число: 2.71828
# Сумма: 5.86, Произведение: 8.54

float_number_1 = float(input('Enter number one : '))
float_number_2 = float(input('Enter number two : '))
total_sum = float_number_1 + float_number_2
product = float_number_1 * float_number_2
print(f'summ = {total_sum :.2f}, product = {product :.2f}')
