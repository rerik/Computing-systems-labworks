from __future__ import annotations
from math import log2


class BitList:

    """
    Класс, моделирующий информационную последовательность бит.
    Экземпляр задаётся либо целым числом и длиной последовательности,
    либо строкой, состоящей из нулей и единиц. Примеры:

        >>> a = BitList(35, 8)
        >>> print(a)
        00100011

        >>> b = BitList('11001011')
        >>> print(b)
        11001011

    Экземпляр класса хранит значение, которое представляет
    последовательность бит целым числом, и длину последовательности.

    Для экземпляров класса определены следующие операции:
    len(a)
    a+b -- конкатенация
    a^b -- исключающее ИЛИ
    a&b -- И
    a|b -- ИЛИ
    a[i] -- обращение по индексу
    Доступны также итеративный перебор и приведение к строке
    """

    value: int
    length: int

    def __init__(self, value: int | str = 0, length: int = 0) -> None:
        if type(value) is str:
            self.value = int(value, 2)
            self.length = len(value)
        else:
            self.value = value
            self.length = length if length else log2(value)
            if self.length < 1:
                self.length = 1

    def __len__(self) -> int:
        return self.length

    def __add__(self, other: BitList) -> BitList:
        return BitList((self.value << len(other)) + other.value, len(self) + len(other))

    def __xor__(self, other: BitList) -> BitList:
        return BitList(self.value ^ other.value, max([len(self), len(other)]))

    def __and__(self, other: BitList) -> BitList:
        return BitList(self.value & other.value, max([len(self), len(other)]))

    def __or__(self, other: BitList) -> BitList:
        return BitList(self.value | other.value, max([len(self), len(other)]))

    def __rshift__(self, n: int):
        return BitList(self.value >> n, len(self))

    def __lshift__(self, n: int):
        return BitList((self.value << n) & ((1 << self.length) - 1), len(self))

    def __getitem__(self, item):
        return 1 if self.value & (1 << self.length - item - 1) else 0

    def __setitem__(self, key, value):
        if value:
            self.value |= (1 << self.length - key - 1)
        else:
            self.value &= (1 << self.length) - 1 - (1 << self.length - key - 1)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.length:
            self.counter += 1
            return self[self.counter - 1]
        else:
            raise StopIteration

    def __str__(self) -> str:
        res = bin(self.value)[2:]
        if self.length > len(res):
            return '0' * (self.length - len(res)) + res
        else:
            return res
