from lib import *

print()
print("Длинна последовательностей:", n := 100)
print()

################################################
if __name__ == '__main__':
    ############################################

    E1 = hilbert_error_stream(.95, .90, .01, .90)
    E2 = hilbert_error_stream(.90, .85, .05, .95)

    print("E1: ", *list(E1(n)), sep='')
    print("E2: ", *list(E2(n)), sep='')
