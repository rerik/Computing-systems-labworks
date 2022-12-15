from random import randint, random
from typing import List
from functools import reduce

LENGTH = 16
SIZE = 5
ERR_PROB = .05


def martynov_filter(m: int) -> callable:

    def func(seq: List[int]) -> int:
        reg = [0]*m
        for a in seq:
            reg = [a] + reg[:-1]
            yield round(sum(reg)/m)

    return func


if __name__ == '__main__':

    f = martynov_filter(LENGTH)

    data = [randint(0, 1) for _ in range(SIZE)]
    seq = reduce(lambda x, y: x + y, [([bit]*LENGTH) for bit in data])
    print(''.join(map(str, seq)))

    err = [0 if random() > ERR_PROB else 1 for _ in range(LENGTH*SIZE)]
    for i in range(LENGTH*SIZE):
        seq[i] ^= err[i]
    print(''.join(map(str, seq)))

    # print(''.join(map(str, seq := [randint(0, 1) for _ in range(LENGTH*SIZE)])))

    print(''.join(map(str, res := [bit for bit in f(seq+[0]*(LENGTH >> 1))][LENGTH >> 1:])))
