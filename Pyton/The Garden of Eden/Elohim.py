import os
import time

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len = 200
print("-" * max_len)

class Console:
    print()
    def __init__(self, text):
        self.text = text
        time.sleep(2)
        for char in self.text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()
    print()

#НАЧАЛО ПОЛЬЗОВАТЕЛЬСКОГО КОДА
try:
    with open('D:\Desktop\MIPT\Pyton\The Garden of Eden\Gritting.txt', 'r', encoding='utf-8') as fd:
        text = fd.read()
except FileNotFoundError:
        print("КРИТИЧЕСКАЯ ОШИБКА: НЕ УДАЛОСЬ НАЙТИ ФАЙЛ ЗАПУСКА")

Start = Console(text)

Elohim = Console(f'ЭЛОХИМ: \n\n Здравствуй, дитя. \n Я - Элохим, хранитель этих садов. \n Как зовут тебя?')

print()
User_name = input('Введите своё имя: ')
print()
if User_name == 'Жанна':
    Elohim = Console(f'ЭЛОХИМ: \n\n {User_name}. \n Я знаю тебя. \n Мой отец говорил о тебе: \n "Чеснейший херувим и прекраснейший серафим" \n Я рад встретить тебя в моих садах. \n Для тебя любой путь открыт.')
    with open('D:\Desktop\MIPT\Pyton\The Garden of Eden\Soul.txt', 'w', encoding='utf-8') as f:
        f.write("Цветки взошли")

elif User_name == 'Кирилл':
    Elohim = Console(f'Здравствуй, Отец')
    person = 0
    try:

        with open('Soul.txt', 'r', encoding='utf-8') as fd:
            person = fd.read()

    except FileNotFoundError:
        None

    if person == 'Цветки взошли':
        Elohim = Console(f'Она заходила в твой сад.')

    else:
        Elohim = Console(f'Она не пришла.')

else:
    Elohim = Console(f'ЭЛОХИМ: \n\n Я рад видеть тебя в своих садах {User_name}. \n Я создал их, чтобы испытать тебя. \n Иди же, открой их секреты. ')

#КОНЕЦ ПОЛЬЗОВАТЕЛЬСКОГО КОДА

print("-" * max_len)