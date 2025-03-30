#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text
# 1. Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)
# Пример использования:
# counter = Counter(5)
# counter += 3
# print(counter)  # Вывод: 8
# counter -= 2
# print(int(counter))  # Вывод: 6

class Counter :
    def __init__(self,number):
        self.number = number

    def __add__(self, other):
         self.number += other
         return self

    def __sub__(self, other):
         self.number -= other
         return self

    def __str__(self):
        return f'Вывод : {self.number} '

    def __int__(self):
        return self.number


print(print_task_number(1))
count = Counter(5)
count -= 2
print(int(count))
count += 5
print(count)

# 2. Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)
# Пример использования:
# email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
# email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
# email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
# print(email1)  # Вывод:
# """
# From: john@example.com
# To: jane@example.com
# Subject: Meeting
# Hi Jane, let's have a meeting tomorrow.
# """
# print(len(email2))  # Вывод: 24
# print(hash(email3))  # Вывод: -920444056
# print(bool(email1))  # Вывод: True
# print(email2 > email3)  # Вывод: True

class Email:

    def __init__(self,from_init,to,subject,text_email,data):
        self.from_init = from_init
        self.to = to
        self.subject =subject
        self.text_email = text_email
        self.data = data

    def __str__(self):
        return f'From: {self.from_init}\nTo: {self.to}\nSubject: {self.subject}\n{self.text_email}'

    def __lt__(self, other):
        return  self.data < other

    def __gt__(self, other):
        return self.data > other

    def __le__(self, other):
        return self.data <= other

    def __ge__(self, other):
        return self.data >= other

    def __eq__(self, other):
        return self.data == other

    def __ne__(self, other):
        return self.data != other

    def __len__(self):
        return len(self.text_email)

    def __hash__(self):
        return hash((self.from_init,self.to,self.subject,self.text_email,self.data))

    def __bool__(self):
        return  bool(self.text_email)



email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

print(print_task_number(2))

print(email2,'\n'*2)
print(len(email2))
print(hash(email3))
print(bool(email1))
print(email2 > email3)