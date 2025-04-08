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

class Player(Console):

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
    
class Power(Player):
 
 def __init__(self, name: str, cost: int) -> None:
  
  self.name = name
  self.cost = cost
 
 def use(self, player: Player) -> None:
  pass

class PhysicalPower(Power):
 
    def __init__(self, name: str, cost: int, count: int) -> None:
  
        super().__init__(name, cost) # вызов конструктора Power
        self.count = count
        self.using = {} # создание пустого словаря очков силы

    def use(self, player: Player):
  
        if player.id not in self.using.keys(): # проверка на существование очков силы у игрока
            self.using[player.id] = 0 # есди их не существует - выдача максимального количесва 

        if self.using[player.id] < self.count: # проверка применяемости физической способности
            Console(f"{player.name} used {self.name}")
            self.using[player.id] = self.using[player.id] + 1

        else:
            Console(f"{player.name} cannot use {self.name}")

class MagicPower(Power):
 
    def __init__(self, name: str, cost: int) -> None:
  
        super().__init__(name, cost)

    def use(self, player: Player):
  
        Console(f"{player.name} used {self.name}")
        player.scores += 1

# Пример использования класса:
p = Player(1, 'Bilbo')                        
t = PhysicalPower('teleport', 10, count=1)    
t.use(p)                                      
t.use(p)                                      
Console(p.scores)                               
 
b = MagicPower('black magic', 200)            
b.use(p)                                      
Console(p.scores)                               
b.use(p)                                      
Console(p.scores)


#КОНЕЦ ПОЛЬЗОВАТЕЛЬСКОГО КОДА

Console(text_stop_output, 0.02)