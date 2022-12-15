from bit_list import *


################################################
# параметры
################################################
print()
print("Длина кода:", CODE_LEN := 31)
print("Длина последовательности:", SEQ_LEN := 16)
# print("Порождающий полином:", g := BitList(polynomial=[16, 12, 11, 10, 9, 4, 0]))
print("Порождающий полином:", g := BitList(polynomial=[15, 11, 10, 9, 8, 7, 5, 3, 2, 1, 0]))
# print("Порождающий полином:", g := BitList(polynomial=[0, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15]))
print()


def ones(x: BitList) -> int:
    return sum(map(int, str(x)))


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


################################################
if __name__ == '__main__':
    ############################################

    with open("bch_data.csv", 'r') as file:
        for line in file:
            i, _, code = line.strip().split(';')
            if code != str(encode(BitList(int(i), SEQ_LEN))):
                print(code)
                print(encode(BitList(int(i), SEQ_LEN)))
                print()

    # print(encode(BitList('0000111100110101')))
    # print(encode(BitList(3893, 16)))
