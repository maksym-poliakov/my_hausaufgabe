# Напишите программу, которая запрашивает у пользователя строку и определяет,
# является ли она панграммой. Панграмма - это фраза, содержащая все буквы алфавита.
# Программа должна игнорировать регистр букв и пробелы при проверке панграммы.
# Выведите соответствующее сообщение на экран с помощью команды print. Решить задачу для латиницы.


string_inp = input('Enter string : ')
string_modify = string_inp.lower().replace(' ','')
start = 97
end = 122
while start <= end :
    is_found = chr(start)
    string_tmp = is_found in string_modify
    if not string_tmp :
        print('The string is not a pangram')
        break
    start += 1
if start > end :
    print(f'The string \"{string_inp}\" is  a pangram')


# Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество гласных
# и согласных букв в ней. Используйте функцию len() для подсчета количества букв.
# Выведите результат на экран с помощью команды print. Решить задачу для латиницы.

string_inp = input('Enter string : ').lower().replace(' ','')
vowels ='aeiou'
count_inp = 0
count_vowels = 0
while count_inp < len(string_inp) :
    count_tmp = 0
    while count_tmp < len(vowels) :
        if string_inp[count_inp] in vowels[count_tmp] :
            count_vowels += 1
        count_tmp += 1
    count_inp += 1
print(f'vowels = {count_vowels }  consonants = {len(string_inp) - count_vowels }')


