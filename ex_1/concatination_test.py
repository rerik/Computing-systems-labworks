from bit_list import *


if __name__ == '__main__':

    for i in range(16):
        for j in range(16):
            a = BitList(i, 4)
            b = BitList(j, 4)
            # print(a, b, a+b)
            print((a+b).value)
