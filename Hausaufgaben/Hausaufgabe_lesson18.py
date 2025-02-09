# Напишите программу, которая запрашивает у пользователя строку и преобразует ее,
# удаляя все гласные буквы из строки. Используйте метод replace() для замены гласных букв на пустую строку.
# Выведите преобразованную строку на экран с помощью команды print.


string_inp = input('Enter string : ')
vowels ='aeiou'
string_tmp = string_inp
count = 0
while count < len(vowels) :
    string_tmp = string_tmp.replace(vowels[count],'')
    count += 1
print(string_tmp)


# Напишите программу, которая запрашивает у пользователя строку и определяет, содержит ли она только
# уникальные символы. Если все символы в строке уникальны, выведите соответствующее сообщение на экран.
# В противном случае выведите сообщение о том, какие символы повторяются. Не используйте множества и
# подобные структуры данных, которые мы пока не изучали, для проверки уникальности символов.

string_inp = input('Enter string : ')
string_tmp = ''
count = 0
lange_string = len(string_inp)
while count < lange_string :
    # В условии за одно проверю чтоб повторяющиеся символы в строке где складываю повторяющиеся символы
    # тоже были уникальными и не повторялись
    if string_inp.count(string_inp[count]) > 1 and string_tmp.count(string_inp[count]) == 0 :
        string_tmp += string_inp[count] + " "
    count += 1
if string_tmp == '' :
    print('Your string contains only unique characters.')
else:
    # rstrip - уберу пробел с права чтоб replace не ставил последнюю ","
    print(f'Your string has duplicate characters : {string_tmp.rstrip().replace(" ", ",")}')


# Напишите программу, которая запрашивает у пользователя строку и выравнивает ее по центру
# с заданной шириной. Если строка не может быть выровнена по центру из-за нечетной ширины,
# она должна быть выровнена смещением вправо. Используйте методы center() и rjust()
# для выравнивания строки.

string_inp = input('Enter string : ').strip()
width = int(input('Enter width : '))
sum_len = len(string_inp) + width
string_len = len(string_inp)
while True :
    if width < 0 :
        print('width must be >= 0')
        width = int(input('Enter width : '))
        continue
    elif   width <= string_len    :
        print(f'can\'t center because width should be more than : {string_len } characters')
        width = int(input('Enter width : '))
        continue
    else :
        if sum_len  % 2 == 0 :
            print(string_inp.center(width))
            break
        else :
            print(string_inp.rjust(width))
            break
