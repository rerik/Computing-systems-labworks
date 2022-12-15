from lib import *
from random import random

print()
print("Длинна последовательностей:", n := 1000)
print("Количество испытаний:", m := 10)
print()

################################################
if __name__ == '__main__':
    ############################################

    for i in range(m):
        p00 = random()
        p01 = 1 - p00
        p11 = random()
        p10 = 1 - p11
        p0 = random()
        p1 = random()
        print(f"№{i+1}. p00: {pct(p00)}% p01: {pct(p01)}% p11: {pct(p11)}% p10: {pct(p10)}% p0: {pct(p0)}% p11: {pct(p1)}%")
        P0 = p10 / (p01 + p10)
        P1 = 1 - P0
        E = hilbert_error_stream(p00, p11, p0, p1)
        print(f"Теоретическая вероятность: {pct(P0*p0 + P1*p1)}%. Статистическая вероятность: {pct(sum(E(n))/n)}%")
