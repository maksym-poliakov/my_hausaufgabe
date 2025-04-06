import re
#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text
# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного
# текста и возвращает их в виде списка.
# Пример использования:
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']

def extract_emails(string) :
    pattern_email = r'[\w.]{1,64}@[\w.]{1,190}(?!\S)'
    return re.findall(pattern_email,string)

print(print_task_number(1))
text = "Contact us at info@example.com or support@example.com for assistance."
emails = extract_emails(text)
print(emails)

# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов
# в тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
# Пример использования:
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# highlighted_text = highlight_keywords(text, keywords)
# print(highlighted_text)
# # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."

def highlight_keywords(string: str, keyword: list[str]) -> str:
    new_text = string
    for word in keyword :
        new_text = re.sub(rf"({word})", r'*\1*', new_text, flags=re.IGNORECASE)
    return new_text

print(print_task_number(2))
text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
print(highlight_keywords(text,keywords))