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

'''
создание класса
'''
class My_first_class: #описание имени класса
    #ниже следует описание класса
    pass #пустой объект

'''
создание экземпляра (объекта) класса
'''
object = My_first_class() #выглядит как вызов функции

print(object.__class__) #вывод класса объекта х
print(type(object)) 
print()
'''
добавление атрибута к объекту
'''
object.name = "Жанна Демидова"
object.species = "моё Солнце"

print(object.name, 'это', object.species)
print()

print("-" * max_len)