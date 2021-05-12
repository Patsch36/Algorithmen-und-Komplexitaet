from time import time

class fibonacci:
    memory_rec = {0: 1, 1: 1}
    memory_it = {0: 1, 1: 1}

    def fibonacci_rec(n):
        # Use this if- statement for making recursion much faster
        # if n in recur_fibo.memory:
        #     return recur_fibo.memory[n]

        # Use this if statement for traditional recursion
        if n <= 1:
            return n
        else:
            fibonacci.memory_rec[n] = fibonacci.fibonacci_rec(n - 1) + fibonacci.fibonacci_rec(n - 2)
            return fibonacci.memory_rec[n]

    def fibonacci_it(n):
        for i in range(2, n + 1):
            fibonacci.memory_it[i] = fibonacci.memory_it[i - 1] + fibonacci.memory_it[i - 2]


if __name__ == "__main__":
    print("Aufgabe a: Es ist sehr ineffizient, da die Vorgängerzahlen bei jedem neuen Glied "
          "in jedem Zweig der Rekursion neu berechnet werden muss.")

    start = time()
    fibonacci.fibonacci_rec(25)
    end = time()
    print(fibonacci.memory_rec)
    print("Benoetigte Zeit: {:5.3f}s\n".format(end-start))

    start = time()
    fibonacci.fibonacci_it(25)
    end = time()
    print(fibonacci.memory_it)
    print("Benoetigte Zeit: {:5.3f}s".format(end-start))