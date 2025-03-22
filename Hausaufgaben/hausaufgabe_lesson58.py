#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади прямоугольника и calculate_perimeter()
# для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем,
# его площадь и периметр.

class Rectangle:

    def __init__(self,width = 5 ,height = 8):
        self.width = width
        self.height = height

    def calculate_area(self) :
        return self.width * self.height

    def calculate_perimeter(self) :
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Area = {self.calculate_area()} \nPerimeter = {self.calculate_perimeter()}'

    def __repr__(self):
        return f'Area : {self.calculate_area()} \nPerimeter : {self.calculate_perimeter()}'


print_task_number(1)
rectangle = Rectangle()
print(rectangle.__repr__())
print(rectangle.__str__())

# 2. Создайте класс BankAccount для представления банковского счета.
# Класс должен иметь атрибуты account_number (номер счета) и balance (баланс),
# а также методы deposit() для внесения денег на счет и withdraw() для снятия денег со счета.
# Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег.
# Выведите оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс
# может стать меньше нуля. В этом случае уходить в минус не будем,
# вместо чего будем возвращать сообщение "Недостаточно средств на счете".

class BankAccount :

    def __init__(self, account_number,balance):
        self.__account_number = account_number
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.__balance = balance

    def __str__(self):
        return f"Счет №{self.__account_number}, Баланс: {self.__balance:.2f}"

    def deposit(self, new_balance) :
        if new_balance > 0 :
            self.__balance += new_balance
            return f'Депозит успешно пополнен. {self}'
        return f'Сумма внесения на депозит должна быть больше нуля'

    def withdraw(self, new_balance) :
        if new_balance <= 0 :
            return f'Сумма снятия должна быть больше нуля'
        if self.__balance < new_balance:
            return f"Недостаточно средств. {self}"
        self.__balance -=new_balance
        return self.__str__()


print_task_number(2)
ba = BankAccount(123456,1)
print(ba.deposit(20))
print(ba.withdraw(120))
print(ba.withdraw(120))
print(ba.deposit(20))
print(ba.withdraw(12))