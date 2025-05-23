from abc import ABC, abstractmethod
import math
# Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text
# 1. Реализуйте класс Employee, представляющий сотрудника компании.
# Класс должен иметь статическое поле company с названием компании, а также методы:
# set_company(cls, name): метод класса для изменения названия компании
# __init__(self, name, position): конструктор, принимающий имя и должность сотрудника
# get_info(self): метод, возвращающий информацию о сотруднике в виде строки (имя, должность, название компании)
# Пример использования:
# employee1 = Employee("John", "Manager")
# employee2 = Employee("Alice", "Developer")
# print(employee1.get_info())  # Вывод:
# """
# Name: John
# Position: Manager
# Company: ABC Company
# """
# Employee.set_company("XYZ Company")
# print(employee2.get_info())  # Вывод:
# """
# Name: Alice
# Position: Developer
# Company: XYZ Company
# """




class Employee :
    name_company = "ABC Company"
    def __init__(self, name, position) :
        self.name = name
        self.position = position


    @classmethod
    def set_company(cls,name):
        cls.name_company = name
        return name

    def get_info(self):
        return f""" 
Name: {self.name}
Position: {self.position}
Company: {Employee.set_company(self.name_company)}
"""
print(print_task_number(1))

employee1 = Employee("John", "Manager")
employee2 = Employee("Alice", "Developer")
print(employee1.get_info())
Employee.set_company("XYZ Company")
print(employee2.get_info())


# 2. Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте классы Rectangle (прямоугольник)
# и Circle (круг). Класс Shape должен иметь абстрактный метод area, который должен быть реализован
# в каждом дочернем классе. Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра.
# Выведите площадь и периметр прямоугольника и круга на экран.
# Пример использования:
# rectangle = Rectangle(5, 3)
# circle = Circle(2)
# print(f"Rectangle area: {rectangle.area()}")  # Вывод: Rectangle area: 15
# print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Вывод: Rectangle perimeter: 16
# print(f"Circle area: {circle.area()}")  # Вывод: Circle area: 12.566370614359172
# print(f"Circle perimeter: {circle.perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172

class Shape(ABC) :

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape) :
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self) :
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self) :
        return math.pi * math.sqrt(self.radius)

    def perimeter(self):
        return  2 * math.pi * self.radius

print(print_task_number(2))
rectangle = Rectangle(5, 3)
circle = Circle(2)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")



