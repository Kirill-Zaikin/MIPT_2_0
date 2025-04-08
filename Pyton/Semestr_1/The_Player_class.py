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


Console(text_start_output , 0.02)

#НАЧАЛО ПОЛЬЗОВАТЕЛЬСКОГО КОДА

class Player:

    id: int
    name: str
    scores: int
    games: list

    def __init__(self, id: int, name: str) -> None:
        # Инициализация атрибутов игрока
        self.id: int = id
        self.name: str = name
        self.scores: int  = 0  # Начальные очки игрока
        self.games: list = []  # Список игр 

    def add_result(self, game_id: int, score: int) -> None:
        self.games.append(game_id)  # Добавление id игры в список
        self.scores: int = self.scores + score  # Прибавление очков к общему количеству

    def get_mean(self) -> float:
        if len(self.games) == 0:
            return 0.0  # Защита от деления на ноль
        return ((self.scores) / (len(self.games)))  # Средний балл

# Пример использования класса:
p = Player(1, 'Bilbo')
Console(p.id)              # 1
Console(p.name)            # Bilbo
Console(p.scores)          # 0
Console(p.games)           # []

p.add_result(15, 10) 
p.add_result(21, 5)  
Console(p.scores)          # 15
Console(p.games)           # [15, 21]
Console(p.get_mean())      # 7.5


#КОНЕЦ ПОЛЬЗОВАТЕЛЬСКОГО КОДА

Console(text_stop_output, 0.02)