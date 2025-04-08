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

def last_discharge(a : str) -> str:
    a_list = a.split(".")
    if len(a_list) == 1:
        return str(int(a) - 1)

    div = int(a_list[0])
    mod = int(a_list[1])

    if mod != 0:
        mod -= 1
    else:
        div -= 1
        mod = "9" * len(a_list[1]) # такая форма записи необходима, чтобы корректно обработать форматы чисел типа 1.00 и более нулей
    return str(div) + '.' + str(mod)

print("Введенное число уменьшино на один бит: ",last_discharge(input("Введите любое число: ")))

print("-" * max_len_consol)