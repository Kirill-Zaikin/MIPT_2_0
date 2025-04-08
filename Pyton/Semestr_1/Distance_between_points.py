'''
Реализуйте класс Point3D, представляющий точку в трехмерном пространстве. Конструктор должен принимать три аргумента: x,y,z
 — координаты точки. Класс должен реализовывать метод distance_to, принимающий в качестве аргумента другую точку и возвращающий расстояние между ними.
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
    
point1 = Point3D(int(input('введите координату x первой точки: ')), 
                 int(input('введите координату y первой точки: ')), 
                 int(input('введите координату z первой точки: ')))

point2 = Point3D(int(input('введите координату x второй точки: ')), 
                 int(input('введите координату y второй точки: ')), 
                 int(input('введите координату z второй точки: ')))
print()

print("Расстоние между точками:", point1.distance_to(point2))

print("-" * max_len)