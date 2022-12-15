from bit_list import *
from signal import *
from matplotlib import pyplot as plt

from numpy import linspace


print()  # Исходные данные
print("Входная последовательность:", a := BitList("0000111100110101"))
print(a.value)
print("Длина последовательности:", LENGTH := len(a))

VIEW_BORDERS = True


################################################
if __name__ == '__main__':
    ############################################

    print()

    # Параметры канала связи
    print("Амплитуда несущего сигнала:", A := 1)
    print("Несущие частоты: ", f1 := 1080, "Гц, ", f2 := 1750, "Гц", sep='')
    print("Время передачи: ", tau := .02, "с", sep='')
    print("Частота дискретизации сигнала: ", fd := max([f1, f2])*100, "Гц", sep='')
    # print("Уровень шума: ", round((lvl := 0)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .05)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .1)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .2)*100), "%", sep='')
    print("Уровень шума: ", round((lvl := .5)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .9)*100), "%", sep='')

    sinwave_1 = sinus(A, f1, 0)
    sinwave_2 = sinus(A, f2, 0)
    noisewave = noise(A * lvl)

    # Генерация несущего сигнала
    codesig = FSK_signal(sinwave_1, sinwave_2, a, tau, fd) + signal(noisewave, tau, fd)

    # Расшифровка сигнала в битовую последовательность
    ressig = FSK_demodulator(codesig, f1, f2)

    time_discretes = linspace(0, tau, len(codesig))
    fig = plt.figure()
    ax1 = fig.add_subplot(5, 1, (1, 4))
    plt.title("Несущий сигнал, двоичная частотная модуляция")
    plt.plot(time_discretes, codesig, marker='.', linestyle='')
    if VIEW_BORDERS:
        for border in linspace(0, tau, LENGTH+1):
            plt.plot([border, border], [-A*(1+lvl), A*(1+lvl)], color='grey', linestyle='dashed')
    ax2 = fig.add_subplot(5, 1, 5)
    plt.title("Демодуляция")
    plt.plot(time_discretes, ressig, marker='.', linestyle='')
    if VIEW_BORDERS:
        for border in linspace(0, tau, LENGTH+1):
            plt.plot([border, border], [0, 1], color='grey', linestyle='dashed')
    plt.subplots_adjust(hspace=.5)

    # sig1 = np.diff(np.unwrap(np.arctan(codesig)))
    # plt.figure()
    # plt.plot(sig1)

    plt.show()
