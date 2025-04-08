'''
Добавьте к реализованному в задании № 1 классу Point3D класс Segment3D, представляющий отрезок. Конструктор должен принимать пару точек — концы отрезка. 
Класс должен реализовывать два метода:

●     length — не принимает аргументов, возвращает длину отрезка;
●     middle — не принимает аргументов, возвращает точку (экземпляр класса Point3D), находящуюся в середине отрезка.
'''

import os
from math import sqrt

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

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, point):
        result = sqrt(sum(list(map(lambda p: (p[0] - p[1]) ** 2, [[f(point) , f(self)] for f in [lambda a: a.x, lambda a: a.y, lambda a: a.z]])))) #внутри map идет перебор орт точек и обработка согласно функции lambda p: (p[0] - p[1]) ** 2
        return result
    
class Segment3D:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def length(self):
        result = self.point1.distance_to(self.point2)
        return result
    
    def middle(self):
        result = Point3D(*map(lambda p: (p[0] + p[1]) / 2, [[f(self.point1) , f(self.point2)] for f in [lambda a: a.x, lambda a: a.y, lambda a: a.z]]))
        return result

coordinate = Point3D('x', 'y', 'z')
   
point1 = Point3D(int(input('введите координату x первой точки: ')), 
                 int(input('введите координату y первой точки: ')), 
                 int(input('введите координату z первой точки: ')))

point2 = Point3D(int(input('введите координату x второй точки: ')), 
                 int(input('введите координату y второй точки: ')), 
                 int(input('введите координату z второй точки: ')))
print()

segment = Segment3D(point1, point2)
middle_point = segment.middle()

print("Длина, соединяющего точки, отрезка:", segment.length())
print()

coordinates = [
    (lambda a: a.x, "x"),
    (lambda a: a.y, "y"),
    (lambda a: a.z, "z")
]

for middle_point, coordinate in coordinates:
    print(f'{coordinate} координата средней точки на отрезке: {middle_point}')

print("-" * max_len)