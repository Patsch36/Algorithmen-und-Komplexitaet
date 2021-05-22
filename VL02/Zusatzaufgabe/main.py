import math
from functools import reduce


def mogroh(zellen):
    for i in range(len(zellen)):
        for j in range(len(zellen)):
            if (j+1) % (i+1) == 0:
                zellen[j] = (zellen[j] + 1) % 2
    return zellen


def print_open(zellen):
    open = []
    for i in range(len(zellen)):
        if zellen[i] == 1:
            print("Zelle %d ist offen!" % (i+1))
            open.append(i)
    return open


if __name__ == "__main__":
    zellen = []
    for i in range(100):
        zellen.append(0)

    zellen_end = mogroh(zellen)
    open = print_open(zellen_end)

    print("Es sing genau %d Zellen offen" % (len(open)))
    print("Es sind nur Quadratzahlen offen, weil diese eine ungerade Anzahl an Primfaktoren haben")
    print("\n")
    print("Laufzeitkomplexität = n^2")

