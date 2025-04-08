import os
import sys
import re

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_path not in sys.path:
    sys.path.append(project_path)

from Semestr_1.Data_output_interface import *

program_name = os.path.basename(__file__)

time_start = console_start(program_name)

# Основной код программы
# ------------------------------------------------------------------------------------------------------------------

Console(f'Введите обрабатываемую строку:')
string = input()
print()
Console(f'Введите регулярное выражение:')
regex = input()
print()

re.compile(regex)
Console(f'Компиляция регульярного выражения успешна!')
print()
Console(f'Первое вхождение:{re.search(regex, string)}')
print()
Console(f'Все вхождения: {re.findall(regex, string)}')

# ------------------------------------------------------------------------------------------------------------------

time_stop = console_stop(program_name, time_start)
#summary(program_name, time_start, time_stop)