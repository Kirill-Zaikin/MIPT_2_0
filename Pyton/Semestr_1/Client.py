from Data_output_interface import *

program_name = os.path.basename(__file__)

time_start = console_start(program_name)

'''Клиентский узел'''
import socket

# Создаём клиентское соединение с сервером, указав IP-адрес и порт сервера (127.0.0.1 и 5000)
with socket.create_connection(('127.0.0.1', 5000)) as s:  # Устанавливаем соединение с сервером

    # Отправляем строку "Привет, машина!" серверу.
    # Кодируем строку в байты с помощью UTF-8, так как `send` работает с байтовыми данными.
    s.send('Привет, машина!'.encode('utf-8'))

    # Получаем ответ от сервера. Мы ожидаем, что сервер отправит обратно те же данные, что мы отправили.
    answer = s.recv(4096).decode('utf-8')

    # Выводим полученный ответ на экран
    Console(f'\n{answer}')  # Сервер должен вернуть "Привет, машина!", если он работает как эхо-сервер

time_stop = console_stop(program_name, time_start)
summary(program_name, time_start, time_stop)