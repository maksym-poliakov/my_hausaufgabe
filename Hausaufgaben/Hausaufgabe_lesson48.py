
# 1. Напишите функцию find_longest_word, которая будет
# принимать список слов и возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.
# Пример вызова функции и ожидаемого вывода:
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)  # Ожидаемый вывод: "dragonfruit"

#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text



def find_longest_word(data: list[str]) -> str :
    sort_data = sorted(data)
    data_tmp = []
    for wort in sort_data :
        if not data_tmp :
            data_tmp.append(wort)
        elif len(wort) == len(data_tmp[0]) :
            data_tmp.append(wort)
    return ','.join(data_tmp)

print(print_task_number(1))
print("words= ['Hallo','World','Funktion','Windows','Elements']")
words= ['Hallo',"World","Funktion","Windows",'Elements']
result = find_longest_word(words)
print(f'Result : {result}')

# 2. Напишите программу, которая будет считывать данные о продуктах из файла и
# использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt", в котором каждая строка будет
# содержать информацию о продукте в формате "название, цена, количество". Например:
# Apple, 1.50, 10
# Banana, 0.75, 15
# В программе определите функцию calculate_total_price, которая будет принимать
# список продуктов и возвращать общую стоимость.
# Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла,
# разделите строки на составляющие и создайте список продуктов.
# Затем вызовите функцию calculate_total_price с этим списком и выведите результат.
# Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода.
# Потому что в реальных задачах обычно этого нет.
# Нужно самому придумывать даже самые простые тестовые данные,
# содержимое тестовых файлов и т.п. В случае с классами (будут чуть позже) особенно.

file_names  = 'product.txt'
def list_product(file_name) -> list[list[str]] :
    list_tmp = []
    with open(file_name,"r",encoding='utf-8') as file :
        for line in file.readlines() :
            list_tmp.extend([line.strip().split(',')])
    return list_tmp

def calculate_total_price(list_prod: list[list[str]]) -> float :
    summ = 0.0
    # name,price,count = list_product
    for item in list_prod :
        summ += float(item[1])
    return summ


print(print_task_number(2))
print(f'Total price : {calculate_total_price(list_product(file_names))}')