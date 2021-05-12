from functools import wraps

# euclid algorithm without trace data structure
def euclid(num1, num2):
    counter = 0
    while num1 % num2 is not 0:
        num1, num2 = num2, int(num1 % num2)
        counter += 1
    return num2


# euclid algorithm with trace data structure
def euclid_trace(num1, num2, data):
    data.append((num1, num2))
    counter = 0
    while num1 % num2 is not 0:
        num1, num2 = num2, int(num1 % num2)
        data.append((num1, num2))
        counter += 1
    return num2


# Stein algorithm without trace data structure
def stein_rec(a, b):
    if b == 0:
        return a
    if a < b:
        return stein_rec(b, a)
    if a % 2 == 0 and b % 2 == 0:
        return 2 * stein_rec(a // 2, b // 2)
    if a % 2 == 0:
        return stein_rec(a // 2, b)
    if b % 2 == 0:
        return stein_rec(a, b // 2)
    else:
        return stein_rec(a - b, b)


# Stein algorithm with trace data structure
def stein_rec_trace(a, b, data):
    data.append((a, b))
    if b == 0:
        return a
    if a < b:
        return stein_rec_trace(b, a, data)
    if a % 2 == 0 and b % 2 == 0:
        return 2 * stein_rec_trace(a // 2, b // 2, data)
    if a % 2 == 0:
        return stein_rec_trace(a // 2, b, data)
    if b % 2 == 0:
        return stein_rec_trace(a, b // 2, data)
    else:
        return stein_rec_trace(a - b, b, data)


def produce_trace_table(fun, num1, num2, tablename):
    data = []
    a = fun(num1, num2, data)
    with open(tablename, 'w') as table:
        table.write("STEP\t\tVALUE 1\t\tVALUE 2\n")

        for i in range(len(data)):
            table.write("%d\t\t\t%5d\t\t%5d\n" % (i, data[i][0], data[i][1]))

        table.write("\nDer groesste, gemeinsame Teiler ist %d\n\n" % (a))


# decorator to trace execution of recursive function
def trace(func, filename):

    # cache func name, which will be used for trace print
    func_name = func.__name__
    # define the separator, which will indicate current recursion level (repeated N times)
    separator = '|  '

    # printing filename
    _filename = filename

    # current recursion depth
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        # repeat separator N times (where N is recursion depth)
        # `map(str, args)` prepares the iterable with str representation of positional arguments
        # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
        # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
        with open(_filename, 'a+') as f:
            f.write(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})\n')
        # we're diving in
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # going out of that level of recursion
        trace.recursion_depth -= 1
        # result is printed on the next level
        with open(_filename, 'a+') as f:
            f.write(f'{separator * (trace.recursion_depth + 1)}|-- return {result}\n')
        return result

    return traced_func


if __name__ == "__main__":
    produce_trace_table(euclid_trace, 1632, 112, "euclid_trace.txt")
    produce_trace_table(stein_rec_trace, 1632, 112, "stein_trace.txt")

    stein_rec = trace(stein_rec, "stein_trace.txt")
    with open("stein_trace.txt", 'a+') as f:
        f.write(str(stein_rec(1632, 112)))
