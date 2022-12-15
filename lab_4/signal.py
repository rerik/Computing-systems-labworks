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


# Функция для рассчёта массива значений ФМ сигнала
def FSK_signal(waveform_1: callable, waveform_2: callable, keying, tau: float, f: float):
    step = tau/len(keying)
    T = 1/f
    t = 0
    res = []
    while t < tau:
        i = int(t // step)
        res.append(waveform_1(t) if keying[i] else waveform_2(t))
        t += T
    return np.array(res)


# Функция демодуляции для восстановления информационной последовательности
def FSK_demodulator(sig, f1: float, f2: float):
    res = np.zeros(len(sig))
    interval = 100
    for i in range(1, len(sig)):
        if i < interval >> 1:
            beg = 0
            end = interval
        elif i + (interval >> 1) >= len(sig):
            beg = -1 - interval
            end = -1
        else:
            beg = i - (interval >> 1)
            end = beg + interval
        w1 = 2*pi/f1
        w2 = 2*pi/f2
        w = abs(np.mean(np.diff(np.diff(sig[beg:end])))/np.mean(sig[beg:end]))
        res[i] = 0 if abs(w - w1) <= abs(w - w2) else 1
    return res
