# Программа считывает натуральное число. 
# По данному натуральному числу найдите минимальное натуральное число, 
# состоящее из тех же цифр, что и данное, и выведите его на экран.
# Число не может начинаться с нуля


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

value = input("Введите число без пробелов:")

print("Тип переменной:",type(value))
print("Кол-во символов:",len(value))
print("Посимвольный вывод:", end = " ")

value_list = []

for i in range (0, len(value), 1):

    print(value[i], end = " ")
    value_list.append(value[i]) 

print()
print("Список символов:", value_list)
print("Тип списка символов:", type(value_list))

value_list.sort() # функция сортирует элементы списка в порядке возрастания, лучше использовать функцию sorted()

print("Отсортированный список:", value_list)
print("Тип отсортированного списка символов:", type(value_list))

if value_list[0] == '0':

    for i in range (0, len(value), 1):

        if value_list[i] != '0':

            value_list[0], value_list[i] = value_list[i], '0'
            break

print("Минимальный список:", value_list)
print("Тип минимального списка символов:", type(value_list))

minimal_number = int(''.join(value_list))

print("Минимальное число:", minimal_number)

print("-" * max_len)