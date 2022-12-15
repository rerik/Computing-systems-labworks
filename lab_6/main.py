from random import randint, seed, random

seed(0)

G_LEN = 16
MSG_LEN = 16
DATA_LEN = 260

ERR_PROB = .02

if __name__ == '__main__':

    # исходные данные
    print("G:", ''.join(map(str, G := list(map(int, "1110001011000011")))))
    print("message:", ''.join(map(str, message := [randint(0, 1) for _ in range(MSG_LEN)])))
    data = [randint(0, 1) for _ in range(DATA_LEN)]
    print("position:", pos := randint(0, DATA_LEN-G_LEN-MSG_LEN))
    data[pos:pos+G_LEN+MSG_LEN] = G + message
    print("data: ", *data, sep='')
    print(" "*6, "."*pos, f"^{'G':_^{G_LEN-2}}^", f"^{'message':_^{MSG_LEN-2}}^", "."*(DATA_LEN-pos-G_LEN-MSG_LEN), sep='')

    # вносим ошибки
    err = [0 if random() > ERR_PROB else 1 for _ in range(DATA_LEN)]
    for i in range(DATA_LEN):
        data[i] ^= err[i]
    print("data: ", *data, sep='')

    # ищем лучшее совпадение
    best_pos = 0
    best_mark = sum([e1 ^ e2 for e1, e2 in zip(data[0:G_LEN], G)])
    for start in range(DATA_LEN-G_LEN-MSG_LEN):
        mark = sum([e1 ^ e2 for e1, e2 in zip(data[start:start+G_LEN], G)])
        if mark < best_mark:
            best_mark = mark
            best_pos = start
    print(f"Best start position is {best_pos} with {best_mark} errors")
    print(f"Sent message is {''.join(map(str, data[best_pos+G_LEN:best_pos+G_LEN+MSG_LEN]))}")
