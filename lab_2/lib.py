from random import random


# модель Гилберта-Эллиота
def hilbert_error_stream(p00: float = .5,  # вероятность сохранения состояния S0
                         p11: float = .5,  # вероятность сохранения состояния S1
                         p0: float = .1,   # вероятность ошибки в состоянии S0
                         p1: float = .1    # вероятность ошибки в состоянии S1
                         ):

    p_e = [p0, p1]  # вероятности ошибок
    p_t = [1-p00, 1-p11]  # вероятности переходов состояний

    def func(n: int):
        s = 0  # текущее состояние
        for _ in range(n):
            yield 1 if random() < p_e[s] else 0
            if random() < p_t[s]:
                s ^= 1

    return func


def pct(num: float) -> float:
    return round(num*100, 2)
