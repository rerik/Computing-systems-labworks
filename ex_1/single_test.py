import bchlib
from bit_list import *


CODE_LEN = 31


if __name__ == '__main__':

    print("A:", a := BitList('0000111100110101'))
    # print("g:", g := BitList(polynomial=[16, 12, 11, 10, 9, 4, 0]))
    print("g:", g := BitList(polynomial=[15, 11, 10, 9, 8, 7, 5, 3, 2, 1, 0]))
    # print("g:", g := BitList(polynomial=[0, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15]))
    print("k:", k := a << (CODE_LEN - len(a)))
    print("s:", s := g << (CODE_LEN - len(g)))

    print(g.value)
    print(a.value)
    bch = bchlib.BCH(16, 31)
    print(bch.encode(bytearray(a.value)))


    while k.len >= len(g):
        print("s >>", shift := s.len - k.len)
        print("k:", k)
        print("s:", s := s >> shift)
        print("k = k^s" + "-"*(CODE_LEN-4))
        print("k:", k := k ^ s)
