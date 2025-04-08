import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Задаём параметры: N - длина сигнала, M - размер ДВПФ
N = 16  # Длина сигнала
M = 20  # Размер ДВПФ
x = np.zeros(N)  # Инициализируем массив для сигнала нулями

# Создаём сигнал
for k in range(0, N - 1, 1):
    # Сигнал x[k] состоит из суммы косинусоидальных компонентов и модулируется дополнительным косинусом с частотой 5/16
    x[k] = (0.42 - 0.5 * np.cos(2 * np.pi * k / N) + 0.08 * np.cos(2 * np.pi * 2 * k / N)) * np.cos(2* np.pi * k * 5 / 16)

# k - это индексы отсчётов сигнала x, обновляем его для использования в графике
k = np.arange(len(x))  # Индексы для оси x на графике

print('x =\n', x)  # Выводим сигнал
print()
print('k =', k)  # Выводим индексы
print()

# График сигнала
plt.figure(figsize=[6, 2], dpi=120)  # Устанавливаем размер графика
ax = plt.axes()  # Создаём ось
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1))  # Устанавливаем шаг для оси X
plt.stem(k, x)  # Рисуем график стемом (столбики для отсчётов)
plt.xlabel("$k$")  # Подпись оси X
plt.ylabel("$x[k]$")  # Подпись оси Y
plt.title("Сигнал $x[k]$")  # Заголовок графика
plt.grid()  # Включаем сетку
plt.tight_layout()  # Подгонка графика
plt.show()  # Показываем график

# Функция для вычисления ДВПФ (дискретное преобразование Фурье)
def dtft(variable, M=1024):
    # Возвращаем нормированные частоты и ДВПФ сигнала
    return np.arange(M) / M, np.fft.fft(variable, M)

# Вычисление ДВПФ сигнала
nu, X_DTFT = dtft(x, M=1024)

print('X_ДВПФ =\n', X_DTFT)  # Выводим результат ДВПФ
print()

# Вычисление ДПФ (быстрое преобразование Фурье)
X_DFT = np.fft.fft(x)  # Стандартный ДПФ с помощью numpy
n = np.arange(X_DFT.size)  # Индексы для оси графика ДПФ

print('n  =', n)  # Выводим индексы
print()
print('X_ДПФ  =\n', X_DFT)  # Выводим результат ДПФ
print()

# График амплитуд ДВПФ и ДПФ
plt.figure(figsize=(6, 3), dpi=120)  # Устанавливаем размер графика
plt.plot(nu, (X_DTFT), label="ДВПФ", linestyle="--", color="blue")  # График ДВПФ
plt.stem(n / len(x), (X_DFT), markerfmt="ro", basefmt=" ", linefmt="r", label="ДПФ")  # График ДПФ

plt.xlabel("Нормированная частота")  # Подпись оси X
plt.ylabel("Амплитуда")  # Подпись оси Y
plt.title("Сравнение ДВПФ и ДПФ")  # Заголовок графика
plt.legend()  # Легенда
plt.grid()  # Включаем сетку
plt.show()  # Показываем график