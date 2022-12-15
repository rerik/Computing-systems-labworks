from random import random
from math import factorial


# замыкание, порождающее генераторы последовательностей ошибок
def error_stream(p: float) -> callable:
    def func(n: int):
        for _ in range(n):
            yield 1 if random() < p else 0
    return func


# рассчёт биномиального распределения
def C(t: int, n: int) -> float:
    return factorial(n)/(factorial(t)*(factorial(n-t)))
