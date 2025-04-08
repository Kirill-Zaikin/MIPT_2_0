import sys
import os

# Определяем путь к корневой директории проекта
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Добавляем путь к проекту в sys.path, если он там отсутствует
if project_path not in sys.path:
    sys.path.append(project_path)

# Импортируем необходимые функции из модуля Data_output_interface
from Semestr_1.Data_output_interface import *

# Получаем имя текущего файла (программы)
program_name = os.path.basename(__file__)

# Фиксируем время начала выполнения программы
time_start = console_start(program_name)

# Основной код программы
# ------------------------------------------------------------------------------------------------------------------

# Выводим сообщение "Привет, Мир!" с минимальной задержкой
Console(f'Привет, Мир!', 0.000001)

# ------------------------------------------------------------------------------------------------------------------

# Фиксируем время завершения выполнения программы
time_stop = console_stop(program_name, time_start)

# Выводим сводку по времени выполнения программы
summary(program_name, time_start, time_stop)
