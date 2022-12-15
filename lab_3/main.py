from bit_list import *
from signal import *
from matplotlib import pyplot as plt

from numpy import linspace


print()  # Исходные данные
print("Входная последовательность:", a := BitList("0000111100110101"))
print("Длина последовательности:", LENGTH := len(a))

VIEW_BORDERS = True


################################################
if __name__ == '__main__':
    ############################################

    # Преобразование в последовательность относительной модуляции
    w = BitList(length=LENGTH)
    w[0] = a[0]
    for i in range(1, LENGTH):
        w[i] = a[i] ^ w[i-1]

    print("Закодированная последовательность:", w)
    print()

    # Параметры канала связи
    print("Амплитуда несущего сигнала:", A := 1)
    print("Частота несущего сигнала: ", f := 10, "Гц", sep='')
    print("Время передачи: ", tau := LENGTH/f, "с", sep='')
    print("Частота дискретизации сигнала: ", fd := f*100, "Гц", sep='')
    print("Уровень шума: ", round((lvl := 0)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .05)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .1)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .2)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .5)*100), "%", sep='')
    # print("Уровень шума: ", round((lvl := .9)*100), "%", sep='')
    print("Уровень шума: ", round((lvl := 1.5)*100), "%", sep='')

    sinwave = sinus(A, f, 0)
    noisewave = noise(A * lvl)

    # Генерация несущего сигнала
    codesig = PSK_signal(sinwave, w, tau, fd) + signal(noisewave, tau, fd)

    # Расшифровка сигнала в битовую последовательность
    ressig = autocorrelation(codesig, LENGTH)

    time_discretes = linspace(0, tau, len(codesig))
    fig = plt.figure()
    ax1 = fig.add_subplot(5, 1, (1, 4))
    plt.title("Несущий сигнал, относительная фазовая модуляция")
    plt.plot(time_discretes, codesig, marker='.', linestyle='')
    if VIEW_BORDERS:
        for border in linspace(0, tau, LENGTH+1):
            plt.plot([border, border], [-A*(1+lvl), A*(1+lvl)], color='grey', linestyle='dashed')
    ax2 = fig.add_subplot(5, 1, 5)
    plt.title("Автокорреляция")
    plt.plot(time_discretes, ressig, marker='.', linestyle='')
    if VIEW_BORDERS:
        for border in linspace(0, tau, LENGTH+1):
            plt.plot([border, border], [0, 1], color='grey', linestyle='dashed')
    plt.subplots_adjust(hspace=.5)
    plt.show()
