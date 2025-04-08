import os

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len_consol = 220
print("-" * max_len_consol)

def fibonacci (index : int) -> int :
    if index == 1:
        return 0
    if index == 2:
        return 1
    
    return fibonacci(index - 1) + fibonacci(index - 2)

print("Нужное вам число Фибоначчи: ", fibonacci(int(input('Введите номер желаемого числа Фибоначчи: '))))

print("-" * max_len_consol)