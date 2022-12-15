from random import randint, random, seed
from functools import reduce
from math import pi, cos, sin, atan
from matplotlib import pyplot as plt

LENGTH = 16
SIZE = 16

HEAD_WIDTH = .1
HEAD_LENGTH = .2

seed(2)

if __name__ == '__main__':

    for err_prob in [0, .01, .02, .03, .04, .05]:

        # создаём последовательность данных
        data = [randint(0, 1) for _ in range(SIZE)]
        seq = sum([([bit]*LENGTH) for bit in data], [])
        print(''.join(map(str, seq)))

        x, y = [], []
        for i in range(LENGTH * SIZE - 1):
            if seq[i] != seq[i+1]:
                alpha = 2*pi/LENGTH*(i % LENGTH)
                x.append(cos(alpha))
                y.append(sin(alpha))

        plt.figure()
        plt.title(f"Error probability is {err_prob: .2f}")
        cx, cy = 0, 0
        for i in range(len(x)):
            plt.arrow(
                x=cx, y=cy, dx=x[i], dy=y[i],
                head_width=HEAD_WIDTH, head_length=HEAD_LENGTH,
                length_includes_head=True, color="green"
            )
            cx += x[i]
            cy += y[i]
            res = atan(cx/cy if cy else pi) % (2*pi)
            print(f"phi: {res/(2*pi)*16:.0f}")

        # вносим в данные ошибку
        err = [0 if random() > err_prob else 1 for _ in range(LENGTH*SIZE)]
        for i in range(LENGTH*SIZE):
            seq[i] ^= err[i]
        print(''.join(map(str, seq)))

        x, y = [], []
        for i in range(LENGTH * SIZE - 1):
            if seq[i] != seq[i+1]:
                alpha = 2*pi/LENGTH*(i % LENGTH)
                x.append(cos(alpha))
                y.append(sin(alpha))

        cx, cy = 0, 0
        for i in range(len(x)):
            plt.arrow(
                x=cx, y=cy, dx=x[i], dy=y[i],
                head_width=HEAD_WIDTH, head_length=HEAD_LENGTH,
                length_includes_head=True, color="blue"
            )
            cx += x[i]
            cy += y[i]
            res = atan(cx/cy if cy else pi) % (2*pi)
            print(f"phi: {res/(2*pi)*16:.0f}")
        plt.arrow(
            x=0, y=0, dx=sum(x), dy=sum(y),
            head_width=HEAD_WIDTH, head_length=HEAD_LENGTH,
            length_includes_head=True, color="red"
        )

    plt.show()
