'''
Добавьте к реализованному в прошлом задании № 2  классу Segment3D метод cos_to, принимающий в качестве аргумента еще один объект класса Segment3D и 
возвращающий косинус угла между отрезками.
При решении задачи воспользуйтесь определением скалярного произведения векторов. 
Поскольку отрезки в отличие от векторов не имеют направления, косинус угла должен быть всегда положительным.
'''

import os
from math import sqrt, fabs

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
    
    def cos_to(self, point):
        result = fabs(sum(list(map(lambda p: (p[1][0] - p[0][0]) * (p[1][1] - p[0][1]), [[[f(f_s(self)), f(f_s(point))] for f_s in [lambda a: a.point1, lambda a:a.point2]] for f in [lambda a: a.x, lambda a: a.y, lambda a: a.z]]))) / (self.length() * point.length()))
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

segment2 = Segment3D(Point3D(0, 2, 0), Point3D(3, 0, 0))

print("Косинус равен:", segment.cos_to(segment2))

print("-" * max_len)