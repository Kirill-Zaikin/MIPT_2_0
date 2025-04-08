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

def super_print(*args, **kwards):
    print(*args, **kwards)
    print('\\' * 40)

super_print('Теперь текст выводится с разделителем')
super_print('И', 'можно', 'использовать', 'различные', 'опции', end = ':\n') # Последний аргумент - именованный
super_print('end', 'sep', 'и другие', sep = ', ', end = '!\n') # Последние два аргумента - именованные

print("-" * max_len)
 