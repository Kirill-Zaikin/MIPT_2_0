from Data_output_interface import *

program_name = os.path.basename(__file__)

time_start = console_start(program_name)

'''Сетевой узел'''
import socket

# Создаём серверный сокет
server = socket.socket()

# Настройка сокета для повторного использования адреса порта
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Привязываем сервер к адресу '127.0.0.1' и порту 5000
server.bind(('127.0.0.1', 5000))  # Привязка к IP и порту
server.listen()  # Начинаем прослушивание порта, ожидаем входящие соединения

Console("Сервер запущен и ожидает подключений...")

try:
    while True:
        # Принимаем входящее соединение (блокирующий вызов)
        client, addr = server.accept()  # Получаем клиентский сокет и адрес клиента

        # Выводим информацию о подключившемся клиенте
        Console(f"Клиент подключен: {addr}") 
        
        # Получаем данные от клиента (до 4096 байт), декодируем в строку с использованием UTF-8
        request = client.recv(4096).decode('utf-8')
        
        # Выводим полученные данные (запрос от клиента)
        Console(f"Ответ от клиента: {request}")
        
        # Отправляем клиенту ответ (тот же запрос обратно, как эхо-сервер)
        client.send('Привет, человече!'.encode('utf-8'))  # Отправляем обратно тот же запрос, кодируем в UTF-8
         
        # Закрываем соединение с клиентом
        client.close()  # Закрываем соединение с клиентом

finally:
    # Закрываем серверный сокет после завершения работы
    time_stop = console_stop(program_name, time_start)
    summary(program_name, time_start, time_stop)
    server.close()  # Закрываем сервер