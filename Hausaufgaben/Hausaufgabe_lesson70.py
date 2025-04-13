from bs4 import BeautifulSoup
import requests
#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице.
def get_list_links(url) :
    list_href = []
    html = requests.get(url).text
    sour = BeautifulSoup(html ,'html.parser')
    links = sour.find_all('a')
    for link in links :
        href = link.get('href')
        if href and href[:4] == "http":
            list_href.append(href )
    return  list_href

print(print_task_number(1))
print("пример для ввода : https://en.wikipedia.org/wiki/English_Wikipedia")
srt_inp = input("Введите url адрес в формате https://....... : ")
print(get_list_links(srt_inp))

# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков,
# а затем использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня
# (теги h1, h2, h3 и т.д.) с их текстом.

def check_titles(title,name_title):
    if title[0] == name_title :
        return True
    else :
        return False

def get_titles(url,name_tgs,list_titles) :
    html = requests.get(url).text
    sour = BeautifulSoup(html,"html.parser")
    dict_title = {}
    for key in list_titles :
        if check_titles(key,name_tgs) :
            title = sour.find_all(key)
            for t in title :
                if t :
                    if key in  dict_title :
                        dict_title[key].append(t.text)
                    else :
                        dict_title[key] =[t.text]
    return dict_title

def get_info(dict_data) :
    for key,value in dict_data.items() :
        print(f'{key} : ')
        for v in value :
            print(v)

print(print_task_number(2))
print("пример для ввода : https://en.wikipedia.org/wiki/English_Wikipedia")
print("пример для ввода : https://convertmonster.ru/blog/seo-blog/html-tegi-h1-h2-h3-h4-h5-h6-zagolovki/")
srt_inp = input("Введите url адрес в формате https://....... : ")
print('Пример ввода заголовков : h1,n2,h2,h3,h4,h5,h6 ')
title_inp =  list(map(str,input("Введите уровень заголовков от h1 до h6 : " ).split(',')))
get_info(get_titles(srt_inp,'h',title_inp ))
