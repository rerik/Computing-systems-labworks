from math import pi, sin
from random import gauss
import numpy as np


# Замыкание синусоидальной функции
def sinus(A: float, f: float, phi: float) -> callable:

    # Циклическая частота
    omega = 2 * pi * f

    def func(t: float):
        return A * sin(omega * t + phi)

    return func


# Замыкание гауссова шума
def noise(A) -> callable:

    """
    Заданый уровень шума соответствует 3-м сигма в гауссовой функции,
    т.е., подразумевает, что 97% ошибок лежат в пределах заданного уровня.
    """

    sigma = A/3

    # Время t задаётся для унификации функций, порождающих сигналы
    def func(t: float) -> float:
        return gauss(0, sigma)

    return func


# Функция для рассчёта массива значений сигнала на заданном промежутке времени
def signal(waveform: callable, tau: float, f: float):
    T = 1/f
    t = 0
    res = []
    while t < tau:
        res.append(waveform(t))
        t += T
    return np.array(res)


# Функция для рассчёта массива значений ФОМ сигнала
def PSK_signal(waveform: callable, keying, tau: float, f: float):
    step = tau/len(keying)
    T = 1/f
    t = 0
    res = []
    while t < tau:
        i = int(t // step)
        res.append(waveform(t) if keying[i] else -waveform(t))
        t += T
    return np.array(res)


# Функция автокорреляции для восстановления информационной последовательности
def autocorrelation(sig, length: int):
    res = np.zeros(len(sig))
    res[0] = 1 if sig[0] >= 0 else 0
    delay = round(len(sig)/length)
    for i in range(1, len(sig)):
        if i < delay:
            res[i] = res[i] if sig[0] * sig[i] >= 0 else -(res[i] - 1)
        else:
            res[i] = res[i] if sig[i - delay] * sig[i] >= 0 else -(res[i] - 1)
    return res
