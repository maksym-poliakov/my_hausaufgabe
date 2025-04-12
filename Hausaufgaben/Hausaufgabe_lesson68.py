import requests
import re
from collections import Counter
#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text
# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и
# возвращает объект ответа. Затем выведите следующую информацию об ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)
# Пример использования:
# url = "https://api.example.com"
# response = get_response(url)
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# print("Response Headers:", response.headers)

def get_response(url) :
    try:
        status = requests.get(url)
    except  requests.exceptions.ConnectionError as e:
        return f'{e}'
    return status


print(print_task_number(1))
url = "https://example.com"
response = get_response(url)
print(f"Status Code: {response.status_code} \n ")
print(f"Response Text: {response.text} \n ")
print(f"Response Headers:{response.headers} \n ")
# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее
# часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое
# страницы с помощью запроса GET и использовать регулярные выражения для извлечения слов.
# Затем функция должна подсчитать количество вхождений каждого слова и вернуть наиболее часто встречающиеся
# слова в порядке убывания частоты.


def find_common_words(url_list):
    word_count = Counter()  # счётчик для слов

    for url in url_list:
        response = requests.get(url)
        text = response.text

        words = re.findall(r'\b\w+\b', text, flags=re.I)
        word_count.update(words)
    return word_count.most_common()

list_url = ["https://example.com","https://ru.wikipedia.org/wiki"]

print(print_task_number(2))
common_words = find_common_words(list_url )
for word, count in common_words[:10]:
    print(f"{word}: {count}")


