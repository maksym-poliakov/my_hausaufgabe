from itertools import accumulate
from  functools import reduce
import operator
#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text
# Напишите программу, которая принимает список слов от пользователя и
# использует генераторное выражение (comprehension) для создания нового списка,
# содержащего только те слова, которые начинаются с гласной буквы.
# Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр.
# В результате программа должна вывести новый список,
# содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем регистре.
words = ['cat','apple','mountain','ice','dog', 'umbrella','pen','ocean','house','egg','fish','island','sun','elephant',
    'tree','unicorn','lamp','orange','book','ear']

def new_list_words(words_list: list[str]) -> list[str] :
    vowels = ['a', 'e', 'i', 'o', 'u']
    words_list_sorted = list(map(lambda w : w.capitalize(),[word for word in words_list if word[0] in vowels ]))
    return words_list_sorted
print(print_task_number(1))
print(f'Список слов : {words}')
print(f'Результат {new_list_words(words)}')


# Напишите программу, которая принимает список чисел от пользователя и использует
# функцию reduce из модуля functools, чтобы найти произведение всех чисел в списке.
# Затем программа должна использовать функцию itertools.accumulate для накопления произведений
# чисел в новом списке. В результате программа должна вывести список,
# содержащий накопленные произведения.


print(print_task_number(2))
numbers = [2,3,4,5,6,7]
def get_list_works(num)  :
    print(f'reduce : {reduce(operator.mul,num)}')
    return list(accumulate(num, operator.mul))

print(f'Список чисел : {numbers}')
print(get_list_works(numbers))