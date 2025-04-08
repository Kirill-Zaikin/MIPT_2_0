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

def inifinite_numbers():
    num = 0 
    while True:
        yield num
        num += 1

iterator = iter(inifinite_numbers())

mapped = map(lambda x: x ** 2, iterator)

filtered = filter(lambda x: x % 2 == 0, mapped)

from itertools import islice

for value in islice(filtered, 5):
    print(value)

print("-" * max_len)
