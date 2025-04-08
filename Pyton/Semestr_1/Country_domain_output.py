#Программа считывает URL-адрес сайта (например, https://vk.com). 
# Определите, находится ли сайт в международном домене, и если нет, к какой стране он относится.
# Если домен является международным, выведите на экран слово «Международный». 
# Если домен является национальным, выведите на экран название страны.
# Варианты доменов, которые могут быть на входе:
# ●             .uk Великобритания
# ●             .de Германия
# ●             .il Израиль
# ●             .in Индия
# ●             .kz Казахстан
# ●             .mm Мьянма
# ●             .om Оман
# ●             .ru Россия
# ●             .uz Узбекистан
# ●             .et Эфиопия
# ●             .com Международный
# ●             .org Международный
# ●             .net Международный

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

Domen = {
    'uk':'Великобритания',
    'de':'Германия',
    'il':'Израиль',
    'in':'Индия',
    'kz':'Казахстан',
    'mm':'Мьянма',
    'om':'Оман',
    'ru':'Россия',
    'uz':'Узбекистан',
    'et':'Эфиопия',
    'com':'Международный',
    'org':'Международный',
    'net':'Международный',
}

def str_revers(x):
  return x[::-1]

str_input = input("Введите адрес:")
str_input_revers = str_revers(str_input)

print("Перевернутый адрес:", str_input_revers)

input_list_revers = str_input_revers.split('.')

print("Список перевернутого адреса:", input_list_revers)

print("Домен:", str_revers(input_list_revers[0]))

print("Владелец домена:", Domen[str_revers(input_list_revers[0])])

print("-" * max_len)