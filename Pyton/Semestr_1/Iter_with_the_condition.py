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

def get_input():
    Input = input("Введите любой символ. Введите 'stop' для завершения: ")
    if Input == 'stop':
        print("Вы остановили программу")
    return Input
 
iterator = iter(get_input, 'stop')

for user in iterator:
    print(f"Вы ввели: {user}")

print("-" * max_len)
