import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# ignore numpy warnings by calculating logarithms from 0
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

if __name__ == "__main__":
    # x_values also corresponds to n- row
    x_values = np.arange(0, 101, 5)

    log = np.log(x_values)
    n_log = x_values * log
    n_quad = np.power(x_values, 2)
    n_tri = np.power(x_values, 3)
    _2_n = np.array(np.power(2, x_values), dtype=np.uint64)

    print("For looking at all calculated values, look at functions.txt\nn^2 may end up with zeros even "
          + "though datatype uint64 is used.")

    with open("functions.txt", 'w') as file:
        enumeration_buffer = 0
        file.write("N- row:\n")
        for number in x_values:
            file.write("%3d\t\t%3.3f\n" % (enumeration_buffer, number))
            enumeration_buffer += 5
        file.write("\n")
        enumeration_buffer = 0

        file.write("log(n):\n")
        for number in log:
            file.write("%3d\t\t%3.3f\n" % (enumeration_buffer, number))
            enumeration_buffer += 5
        file.write("\n")
        enumeration_buffer = 0

        file.write("N * log(n):\n")
        for number in n_log:
            file.write("%3d\t\t%3.3f\n" % (enumeration_buffer, number))
            enumeration_buffer += 5
        file.write("\n")
        enumeration_buffer = 0

        file.write("n^2:\n")
        for number in n_quad:
            file.write("%3d\t\t%3.3f\n" % (enumeration_buffer, number))
            enumeration_buffer += 5
        file.write("\n")
        enumeration_buffer = 0

        file.write("n^3:\n")
        for number in n_tri:
            file.write("%3d\t\t%3.3f\n" % (enumeration_buffer, number))
            enumeration_buffer += 5
        file.write("\n")
        enumeration_buffer = 0

        file.write("2^n:\n")
        for number in _2_n:
            file.write("%3d\t\t%3d\n" % (enumeration_buffer, number))
            enumeration_buffer += 5

    # plt.plot(x_values, x_values, log, n_log, n_quad, n_tri, _2_n)
    plt.plot(x_values)
    plt.title("f(x)=n")
    plt.show()
    plt.plot(log)
    plt.title("f(x)=log(n)")
    plt.show()
    plt.plot(n_log)
    plt.title("f(x)=n*log(n)")
    plt.show()
    plt.plot(n_quad)
    plt.title("f(x)=n^2")
    plt.show()
    plt.plot(n_tri)
    plt.title("f(x)=n^3")
    plt.show()
    plt.plot(_2_n)
    plt.title("f(x)=2^n")
    plt.show()

