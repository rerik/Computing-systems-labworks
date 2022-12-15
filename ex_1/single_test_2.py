from bit_list import *


################################################
# параметры
################################################
print()
print("Длина кода:", CODE_LEN := 31)
print("Длина последовательности:", SEQ_LEN := 16)
# print("Порождающий полином:", g := BitList(polynomial=[16, 12, 11, 10, 9, 4, 0]))
print("Порождающий полином:", g := BitList(polynomial=[15, 11, 10, 9, 8, 7, 5, 3, 2, 1, 0]))
print()


# Кодирование БЧХ(31, 16, 7)
def encode(a):
    k = a << (CODE_LEN - len(a))
    s = g << (CODE_LEN - len(g))
    while k.len >= len(g):
        shift = s.len - k.len
        s = s >> shift
        k = k ^ s
    r = BitList(k.value, 15)
    return a + r


if __name__ == '__main__':

    # print("A:", a := BitList('0000111100110101'))
    print("A:", a := BitList(50, 16))
    aa = encode(a)
    print(aa)
    print(len(aa))
    print(sum(map(int, str(aa))))

