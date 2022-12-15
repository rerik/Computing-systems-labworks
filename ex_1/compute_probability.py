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


def mac_williams(q: int, n: int, k: int, A: List[int]) -> callable:

    p = (q-1)/q
    return [int((q**(n-k))*((1/q + p*y)**n)*A[int((1-y)/(1+(q-1)*y))]) for y in range(len(A))]


################################################
if __name__ == '__main__':
    ############################################

    # статистика блочных ошибок
    Q: List[int] = [0]*(CODE_LEN+1)

    for i in range(2**SEQ_LEN):
        Q[ones(encode(BitList(i, SEQ_LEN)))] += 1

    for i in range(CODE_LEN+1):
        print(f"Q{i}: {Q[i]}")

    print(sum(Q))
    print()

    B = mac_williams(2, CODE_LEN, 15, Q)
    for i in range(16):
        print(f"B{i}: {B[i]}")

    print(sum(B))
    print()

    # Статистика по кодам из Matlab для сравнения
    # Q2: List[int] = [0]*(CODE_LEN+1)
    #
    # with open("bch_data.csv", 'r') as file:
    #     for line in file:
    #         code = line.split(';')[-1].strip()
    #         Q2[sum(map(int, code))] += 1
    #
    # for i in range(CODE_LEN+1):
    #     print(f"Q{i}: {Q2[i]}")
    #
    # print(sum(Q2))
    # print()

    # print(encode(BitList('0000111100110101')))
