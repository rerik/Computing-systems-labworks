from math import sin, cos, pi, atan
from random import random

p = float(input('Задайте среднюю частоту дроблений '))
n = int(input('Задайте количество моделируемых посылок <1024 '))

# Генерация потока входных посылок
a1 = [0, 0, 0xffff, 0xffff]
a = [0]*(n+1)
for i in range(n+1):
    d = 0x8000
    a[i] = a1[i%4]
    for _ in range(16):
        if random() < p:
            a[i] ^= d
        d >>= 1

# Вычисление результирующего вектора фаз посылок
c = s = 0
for i in range(n):
    d1 = (a[i] ^ a[i] << 1) & 0xfffe
    for j in range(1, 15):
        if d1 & 0x8000:
            s += sin(j*pi/8)
            c += cos(j*pi/8)
    d1 >>= 1
    b = ((a[i + 1] >> 15) ^ a[i]) & 1
    if b:
        c += 1

r = atan(s/c) if c else pi
if r < 0:
    r += 2*pi
f = round(8*r/pi)
print(f"Фаза неискаженных посылок={f}")
