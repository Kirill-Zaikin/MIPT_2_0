import os
import time

program_name = os.path.basename(__file__)

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len = 200

text_start = f'ЗАПУСК ПРОГРАММЫ: {program_name}'
len_start = len(text_start)
len_start_output = '-' * (max_len - len_start)
text_start_output =  f'{text_start} {len_start_output}'

text_stop = f'ЗАВЕРШЕНИЕ ПРОГРАММЫ: {program_name}'
len_stop = len(text_stop)
len_stop_output = '-' * (max_len - len_stop)
text_stop_output =  f'{text_stop} {len_stop_output}'

class Console:
    def __init__(self, text, time_stop = 0.1) -> str:
        self.text = str(text)
        self.time_stop = time_stop
        time.sleep(1)
        for char in self.text:
            print(char, end='', flush=True)
            time.sleep(time_stop)
        print()
        print()


Console(text_start_output , 0.02)

#НАЧАЛО ПОЛЬЗОВАТЕЛЬСКОГО КОДА

class Creature:
 health_points: int

class EarthCreature(Creature):
 pass

class Troll(EarthCreature):
 health_points = 100

class Elf(EarthCreature):
 health_points = 80

class SeaCreature(Creature):
 pass

class Mermaid(SeaCreature):
 health_points = 60

class Siren(SeaCreature):
 health_points = 75

class AirCreature(Creature):
 pass

class Dragon(AirCreature):
 health_points = 120

class Pegasus(AirCreature):
 health_points = 85


class_dictionary = {
  'Эльф' : Elf(),
  'Троль' : Troll(),
  'Русалка' : Mermaid(),
  'Сирена' : Siren(),
  'Дракон' : Dragon(),
  'Пегас' : Pegasus()
  }

for key,x in class_dictionary.items():

    Console(f'Существо: {key}')
    Console(f'-Принидлежность к классу "Земные твари": {isinstance(class_dictionary[key], EarthCreature)}', 0.05)
    Console(f'-Принидлежность к классу "Твари": {isinstance(class_dictionary[key], Creature)}', 0.05)
    Console(f'-Здоровье существа: {class_dictionary[key].health_points}', 0.05)

#КОНЕЦ ПОЛЬЗОВАТЕЛЬСКОГО КОДА

Console(text_stop_output, 0.02)