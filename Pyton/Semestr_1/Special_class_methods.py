import os
import time
import psutil
from datetime import datetime

program_name = os.path.basename(__file__)

def clear_terminal():

    # Для Windows
    if os.name == 'nt':

        os.system('cls')
    # Для Unix/Linux/Mac
    else:

        os.system('clear')

clear_terminal()

max_len = 160

text_start = f'ЗАПУСК ПРОГРАММЫ: {program_name}'
len_start = len(text_start)
len_start_output = '-' * (max_len)
text_start_output =  f'{text_start}\n{len_start_output}\n'

text_stop = f'ЗАВЕРШЕНИЕ ПРОГРАММЫ: {program_name}'
len_stop = len(text_stop)
len_stop_output = '-' * (max_len)
text_stop_output =  f'\n{len_stop_output}\n{text_stop}\n'

class Console:

    def __init__(self, text, time_stop = 0.1) -> str:

        self.text = str(text)
        self.time_stop = time_stop
        time.sleep(1)

        for char in self.text:

            print(char, end='', flush=True)
            time.sleep(time_stop)
        print()

class Summary(Console):

    def __init__(self, time_start, time_stop, date):
        
        self.start = time_start
        self.stop = time_stop
        self.date = date

        self.time_work = self.stop - self.start

        Console('СВОДКА РАБОТЫ ПРОГРАММЫ:\n',0.015)
        Console(f' - Время работы программы: {self.time_work:.4f} сек.', 0.015)
        Console(f" - Объём памяти: {psutil.Process().memory_info().rss / 1024 ** 2:.4f} МБ (учитывая оболочку сводки работы программы)", 0.015)

        Console(f'\nДата формирования сводки для "{program_name}": {self.date}\n', 0.015)

Console(text_start_output , 0.015)

programm_time_start = time.time()

#НАЧАЛО ПОЛЬЗОВАТЕЛЬСКОГО КОДА

#Вывод информации на экран
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    '''Специальный метод представления информации в консоль'''
    def __repr__(self):
        '''Возвращает строковое представление объекта'''
        return f'Point({self.x}, {self.y})'

p = Point(34, -23)

Console(p)

#Сравнение на равенство пользовательских объектов

class Point_eq(Point):
    '''Описывает сравнение для пользовательских объектов'''
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
if (p == Point_eq(34, -23)) == True:
    Console('\N{SMILING FACE WITH SMILING EYES}')

#Хеширование

class Point_hash(Point_eq):
    '''Описание функции вычисления хеш-кода'''
    def __hash__(self):
        return hash((self.x, self.y))
    
points = {Point_hash(34, -23): 10}

Console(f'Ключ точки в словаре: {points[Point_hash(34, -23)]}')

#КОНЕЦ ПОЛЬЗОВАТЕЛЬСКОГО КОДА

programm_time_stop = time.time()

Console(text_stop_output, 0.015)

Summary(programm_time_start, programm_time_stop, datetime.now())