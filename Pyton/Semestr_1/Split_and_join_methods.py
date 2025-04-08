import os

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len_consol = 238
print("-" * max_len_consol)

t = "Шла Саша по шоссе"
s = ['Шла', 'Саша', 'по', 'шоссе']

print(t.split(' '))
print(type(t.split(' ')))
print("Класс элемента списка:", type(t.split(' ')[0]))

print()

print('||'.join(s))
print(type('||'.join(s)))
print("Класс элемента строки:",type('||'.join(s)[0]))

print("-" * max_len_consol)