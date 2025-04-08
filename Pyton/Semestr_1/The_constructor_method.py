import os

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len = 200
print("-" * max_len)

'''Конструктор с однним атрибутом для всех объектов'''
class Box:
    def __init__(self): #объявление метода __init__, self(с англ. соглашение) обязательный аргумент метода __init__
        self.content = [] # создан атрибут content - список данных
'''Создание объектов x и y'''
x = Box() #автоматически вызывается __init__ в качестве self передается объект x 
y = Box()
x.content.append([1, 5, 6, 8])
y.content.append("КОТ")

print(x.content)
print(y.content)
print()
'''Конструктор с разными атрибутоми для разных объектов'''
class Message:
    def __init__(self, first, second): 
        self.first =  'Жанна'
        self.second = str(second)

'''Создание объектов'''
letter = Message(None, 'я тебя люблю!')  

print(f'{letter.first}, {letter.second}') 
print()

'''Конструктор с разными атрибутоми для разных объектов и разными методами'''
class Point_2D:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

'''Создание объектов'''
point1 = Point_2D(3, 4)  

print(point1.distance_to_origin()) 
print()

print("-" * max_len) 