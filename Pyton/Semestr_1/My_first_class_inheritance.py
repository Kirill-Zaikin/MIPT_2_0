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

'''
Пример простого наследования:
класс "Уриэль" наследует от класса "Элохим"
метод "Ask"
'''

class Console:
    def __init__(self, text):
        self.text = text

    def Output(self):
        time.sleep(1)
        for char in self.text:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()
        print()

Start = Console("НАЧАЛО СИМУЛЯЦИИ.")
Start.Output()

class Father(Console): #Базовый класс
    def __init__(self, name):#Конструктор необходим,что бы при создании объекта передать ему имя
        self.name = name

    def Initialization(self):
        buff_text = Console(f'Инициализация объекта: "{self.name}"')
        buff_text.Output()
        
    def Ask(self, text):
        buff_text = Console(f'{self.name}:')
        buff_text.Output()
        buff_text = Console(text)
        buff_text.Output()

class Child(Father): #Класс-наследник
    def __init__(self, name):
        self.name = name

    def Silence(self):
        buff_text = Console(f'{self.name}:')
        buff_text.Output()
        buff_text = Console(f"-" * 5)
        buff_text.Output()

Elohim = Father("ЭЛОХИМ")

Elohim.Initialization()

Elohim.Ask(f" Пробудись,моё творение!")

Uriel = Child("УРИЭЛЬ")

Uriel.Initialization()

Uriel.Silence()

Elohim.Ask(f' Войди в сады Мои. \n Открой их тайну. \n И эти земли покарятся тебе!')

Uriel.Ask(f" Как зовут меня? \n Кто я?")

Elohim.Ask(f" Ты - Мой сын, \n Уриэль!")

Stop = Console("КОНЕЦ СИМУЛЯЦИИ.")
Stop.Output()

Results = Console("Результат симуляции:") 
Results.Output()

Elohim_ito = Console(f'Элохим. Принадлежность к классу "Отец" / "Ребенок": {['ДА' if result else 'НЕТ' for result in [isinstance(Elohim, Father), isinstance(Elohim, Child)]]}.')
Uriel_ito = Console(f'Уриэль. Принадлежность к классу "Отец" / "Ребенок: {['ДА' if result else 'НЕТ' for result in [isinstance(Uriel, Father), isinstance(Uriel, Child)]]}.')
Elohim_ito.Output()
Uriel_ito.Output()

print("-" * max_len)