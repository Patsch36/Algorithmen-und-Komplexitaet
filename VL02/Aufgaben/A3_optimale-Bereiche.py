from scipy.optimize import fsolve
import pylab
import numpy
from numpy.linalg import solve
import math

import terminaltables


class functions:
    @staticmethod
    def f(x):
        return 2 ** x

    @staticmethod
    def g(x):
        return 50 * x ** 2

    @staticmethod
    def h(x):
        return 1000 * x


class operations(functions):
    def __init__(self):
        self.points = []

    def findIntersection(self, fun1, fun2, x0):
        _x = fsolve(lambda x: fun1(x) - fun2(x), x0)
        self.points.append((_x[0], fun1(_x)[0]))
        self.points = sorted(self.points)

    def show_plots(self, ):
        x = numpy.linspace(-1, 20, 10000)
        x_f = numpy.linspace(-1, 15, 10000)
        pylab.plot(x_f, self.f(x_f), x, self.g(x), x, self.h(x),
                   self.points[0][0], self.points[0][1], 'ro', self.points[1][0], self.points[1][1], 'ro',
                   self.points[2][0], self.points[2][1], 'ro', self.points[3][0], self.points[3][1], 'ro',
                   self.points[4][0], self.points[4][1], 'ro', self.points[5][0], self.points[5][1], 'ro')
        pylab.show()

        x = numpy.linspace(-0.5, 0.5, 250)
        pylab.plot(x, self.f(x), x, self.g(x), self.points[1][0], self.points[1][1], 'ro', 0, self.g(0), 'ro',
                   self.points[3][0],  self.points[3][1], 'ro')
        pylab.show()

    def show_functions(self, _min, _max, _amount_entry):
        x = numpy.linspace(_min, _max, _amount_entry)
        pylab.plot(x, self.f(x), x, self.g(x), x, self.h(x))
        pylab.show()

    def show_most_efficient_area(self):
        if self.points[0][0] != -math.inf:
            self.points.insert(0, (-math.inf, -math.inf))
            self.points.insert(len(self.points), (math.inf, math.inf))

        print('Lowest functions in certain areas: ')
        for entry in range(len(self.points) - 1):
                print('Von %f bis %f: ' % (self.points[entry][0], self.points[entry + 1][0]),
                      self.find_lesser_func((self.points[entry][0] + self.points[entry + 1][0])/2)[1])

        self.show_plots()

    def find_lesser_func(self, x):
        results = []
        results.append((self.f(x), 'f'))
        results.append((self.g(x), 'g'))
        results.append((self.h(x), 'h'))
        results = sorted(results)
        return results[0]

    def print_tablular(self, rows, alignments, heading=True):
        values = [[str(v) for v in row] for row in rows]
        widths = [max(len(row[i]) for row in values) for i in range(len(rows[0]))]

        def align(s, w, a):
            return {'l': s.ljust, 'r': s.rjust, 'c': s.center}[a](w)

        def print_line(c):
            print(c * (sum(widths) + 3 * len(widths) + 1))
            print_line("=")

        for row in values:
            if heading and len(values) > 1 and row == values[1]: print_line("-")
            print("| %s |" % " | ".join(align(s, w, a) for s, w, a in zip(row, widths, alignments)))
        print_line("=")


if __name__ == "__main__":
    op = operations()
    op.findIntersection(functions.f, functions.g, 1.0)
    op.findIntersection(functions.f, functions.g, -1.0)
    op.findIntersection(functions.f, functions.g, 13.0)
    op.findIntersection(functions.h, functions.g, 0.0)
    op.findIntersection(functions.h, functions.g, 20.0)

    print("Aufgabe a:\n")
    op.show_most_efficient_area()

    print("\n\nAufgabe b:\n")
    print("Annahme bei Aufgabe b und c ist, dass n die Anzahl der zu lösenden Probleme ist und das Ergebnis der " +
          "Funktion die dafür benötigten Arbeitsschritte. \nDeshalb wurde für gegebenen Wert (Mögliche Arbeitsschritte" +
          "in gegebener Zeit) eine Lösung für n gesucht.")
    timesR1 = [
        ['Time in secconds', 'Operations Algorithm 1000*n', 'Operations Algorithm 50*n**2', 'Operations Algorithm 2**n'],
            [1, solve([[1000]], [1000]), numpy.sqrt(solve([[50]], [1000])), solve([[1]], [numpy.log2(1000)])],
            [60, solve([[1000]], [60000]), numpy.sqrt(solve([[50]], [60000])), solve([[1]], [numpy.log2(60000)])],
            [3600, solve([[1000]], [3600000]), numpy.sqrt(solve([[50]], [3600000])), solve([[1]], [numpy.log2(3600000)])]
        ]
    tableR1 = terminaltables.SingleTable(timesR1, title="Rechner 1")
    print(tableR1.table)

    print("\n\nAufgabe b:\n")
    timesR2 = [
        ['Time in secconds', 'Operations Algorithm 1000*n', 'Operations Algorithm 50*n**2',
         'Operations Algorithm 2**n'],
        [1, solve([[1000]], [10000]), numpy.sqrt(solve([[50]], [10000])), solve([[1]], [numpy.log2(10000)])],
        [60, solve([[1000]], [600000]), numpy.sqrt(solve([[50]], [600000])), solve([[1]], [numpy.log2(600000)])],
        [3600, solve([[1000]], [36000000]), numpy.sqrt(solve([[50]], [36000000])), solve([[1]], [numpy.log2(36000000)])]
    ]
    tableR2 = terminaltables.SingleTable(timesR2, title="Rechner 2")
    print(tableR2.table)

    print("Beim Algorithmus 1000*n ist Rechner 1 immer 10 mal schneller, da der Algorithmus linear verläuft und " +
          "die Rechengeschwindigkeit verzehntfacht wurde.\n" +
          "Der Algorithmus 50*n**2 hat sich grob verdreifacht, der Algorithmus 2**n weißt bei zunehmender  Zeit " +
          "immer kleinere Verbesserungen bei Rechner 2 vor.")
