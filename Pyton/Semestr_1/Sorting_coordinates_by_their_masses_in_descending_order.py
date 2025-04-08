#Даны N точек на прямой. У каждой известны координата X и масса M. 
#Задача: вывести координаты точек в порядке убывания массы.Программа считывает натуральное число N — количество точек.
# Далее программа построчно считывает параметры для каждой n-ой точки: координату xi и массу mi. 
# Оба параметра являются целыми числами, масса является положительным числом. 
# Гарантируется, что строгого совпадения масс двух точек в считываемых данных не встречается.
# Программа должна вывести координаты xi точек, отсортированных по убыванию массы, каждая в новой строке.

import os

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len = 220
print("-" * max_len)

N = int(input("Введите кол-во точек:"))

point = {

}

buff_list = []
coordinate_list = []
mass_list = []

for i in range (0, N, 1):
    input_str = (input(f"Введите координату и массу {i + 1} точки:"))
    buff_list = input_str.split(' ')
    coordinate_list.append(int(buff_list[0]))
    mass_list.append(int(buff_list[1]))
    buff_list.clear()
    point[mass_list[i]] = coordinate_list[i]

print()

print("Список координат точек:", coordinate_list)
print("Тип списка координат точек:", type(coordinate_list))

print()

print("Список масс точек:", mass_list)
print("Тип списка масс точек:", type(mass_list))

print()

print("Словарь масса - координата:", point)

#mass_list.sort()
mass_list = sorted(mass_list, reverse = True)

print()

print("Отсортированный список масс точек:", mass_list)
print("Тип отсортированного списка масс точек:", type(mass_list))

print()

print("Координаты точек,отсортированных по массе:")

for i in range(0, N, 1):
    print(point[mass_list[i]])

print("-" * max_len)