import os
import time
import psutil
from datetime import datetime
from tqdm import tqdm

def clear_terminal():
    """Очищает терминал в зависимости от операционной системы."""
    if os.name == 'nt':
        os.system('cls')  # Для Windows используем команду cls для очистки терминала
    else:
        os.system('clear')  # Для Unix/Linux/Mac используем команду clear для очистки терминала

class Console:
    """Класс для вывода текста с эффектом печати в терминал."""
    
    def __init__(self, text, time_stop=0.05) -> str:
        """
        Инициализирует объект консоли, который будет выводить текст с заданной задержкой.
        
        :param text: Текст для вывода в терминал
        :param time_stop: Время задержки между выводом символов, по умолчанию 0.05 секунд
        """
        self.text = str(text)  # Преобразуем текст в строку
        self.time_stop = time_stop  # Задаём задержку между символами
        time.sleep(1)  # Задержка перед началом вывода
        
        # Выводим каждый символ с задержкой
        for char in self.text:
            print(char, end='', flush=True)
            time.sleep(time_stop)
        print()  # Печатаем пустую строку в конце для завершения вывода

class Summary(Console):
    """Класс для отображения сводки работы программы."""
    
    def __init__(self, programm_name, time_start, time_stop, date):
        """
        Инициализирует объект сводки, который выводит время работы программы, использованную память и дату.
        
        :param time_start: Время старта программы
        :param time_stop: Время завершения программы
        :param date: Дата формирования сводки
        """
        self.programm_name = programm_name #Имя программы
        self.start = time_start  # Время старта
        self.stop = time_stop    # Время завершения
        self.date = date         # Дата формирования сводки
        self.time_work = self.stop - self.start  # Время работы программы

        # Выводим сводку
        Console('СВОДКА РАБОТЫ ПРОГРАММЫ:\n', 0.015)
        Console(f' - Время работы программы: {self.time_work:.4f} сек.', 0.015)
        
        # Получаем объем памяти, использованный программой, и выводим его
        memory = psutil.Process().memory_info().rss / 1024 ** 2  # в МБ
        Console(f' - Объём памяти: {memory:.4f} МБ (учитывая оболочку сводки работы программы)', 0.015)
        
        # Выводим дату формирования сводки
        Console(f'\nДата формирования сводки для программы "{programm_name}": {self.date}\n', 0.015)

def console_start(program_name):
    """Функция для запуска терминала и отображения информации о старте программы."""
    
    # Очищаем терминал
    clear_terminal()

    # Получаем размеры терминала для создания горизонтальной линии
    size = os.get_terminal_size()
    width = size.columns  # Получаем ширину терминала
    len_output = '-' * (width)  # Горизонтальная линия, равная ширине терминала
    
    # Формируем строку для начала работы программы
    text_start = f'ЗАПУСК ПРОГРАММЫ: {program_name}'
    text_start_output = f'{text_start}\n{len_output}\n'

    # Выводим текст "Загружаем терминал" с прогрессом
    Console('ЗАГРУЗКА ТЕРМИНАЛА')
    for i in tqdm(range(20)):  # 20 шагов загрузки
        time.sleep(0.1)  # Задержка между шагами
    Console('ТЕРМИНАЛ ЗАГРУЖЕН')

    # Выводим информацию о запуске программы
    Console(f'\n{text_start_output}\n', 0.015)

    # Возвращаем время старта для дальнейшего использования
    return time.time()  # Время старта программы

def console_stop(program_name, time_start):
    """Функция для завершения работы программы и отображения информации о её завершении."""
    
    time_stop = time.time()  # Получаем время завершения программы

    # Получаем размеры терминала для создания горизонтальной линии
    size = os.get_terminal_size()
    width = size.columns
    len_output = '-' * (width)  # Горизонтальная линия

    # Формируем строку для завершения работы программы
    text_stop = f'ЗАВЕРШЕНИЕ ПРОГРАММЫ: {program_name}'
    text_stop_output = f'\n{len_output}\n{text_stop}\n'
    
    # Выводим информацию о завершении программы
    Console(text_stop_output, 0.015)
    
    # Возвращаем время завершения для использования в функции summary
    return time_stop

def summary(programm_name, programm_time_start, programm_time_stop):
    """Функция для отображения сводки работы программы."""
    
    # Создаём объект Summary, который отобразит время работы программы и другие данные
    return Summary(programm_name, programm_time_start, programm_time_stop, datetime.now())



"""
ПРИМЕР ИМПОРТА И ИСПОЛЬЗОВАНИЯ МОДУЛЯ

import sys
import os

#мДобавление корневого пути проекта в sys.path
# 
# os.path.dirname(__file__) возвращает абсолютный путь к директории текущего скрипта (Test_programm.py).
# os.path.join(..., '..') поднимается на один уровень выше (к корню проекта).
# os.path.abspath() преобразует путь в абсолютный.
# 
# Например, если скрипт лежит в "D:/MIPT/Pyton/Semestr_2/", то project_path станет "D:/MIPT/Pyton".
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Проверка, чтобы избежать дублирования пути в sys.path.
# sys.path — это список директорий, в которых Python ищет модули при импорте.
# Если project_path ещё нет в sys.path, он добавляется в начало списка.
if project_path not in sys.path:
    sys.path.append(project_path)

# Импорт необходимых функций из модуля Data_output_interface
from Semestr_1.Data_output_interface import console_start, console_stop, summary, time

# Получение имени текущего скрипта (файла) для последующего логирования
program_name = os.path.basename(__file__)

# Фиксация времени начала выполнения программы
time_start = console_start(program_name)

# Основной код программы
# ------------------------------------------------------------------------------------------------------------------

time.sleep(5)  # Например, задержка для теста работы программы

# ------------------------------------------------------------------------------------------------------------------

# Фиксация времени завершения программы
time_stop = console_stop(program_name, time_start)

# Вывод итоговой информации о выполнении программы
summary(program_name, time_start, time_stop)
"""