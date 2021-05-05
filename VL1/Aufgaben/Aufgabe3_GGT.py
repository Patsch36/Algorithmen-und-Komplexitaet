def euclid(num1, num2, data):
    data.append((num1, num2))
    counter = 0
    while num1 % num2 is not 0:
        num1, num2 = num2, int(num1 % num2)
        data.append((num1, num2))
        counter += 1
    return num2


def stein_rec(a, b, data):
    data.append((a, b))
    if b == 0:
        return a
    if a < b:
        return stein_rec(b, a, data)
    if a % 2 == 0 and b % 2 == 0:
        return 2 * stein_rec(a // 2, b // 2, data)
    if a % 2 == 0:
        return stein_rec(a // 2, b, data)
    if b % 2 == 0:
        return stein_rec(a, b // 2, data)
    else:
        return stein_rec(a - b, b, data)


def produce_trace_table(fun, num1, num2, tablename):
    data = []
    a = fun(num1, num2, data)
    with open(tablename, 'w') as table:
        table.write("STEP\t\tVALUE 1\t\tVALUE 2\n")

        for i in range(len(data)):
            table.write("%d\t\t\t%5d\t\t%5d\n" % (i, data[i][0], data[i][1]))

        table.write("\nDer groesste, gemeinsame Teiler ist %d" % (a))


if __name__ == "__main__":
    produce_trace_table(euclid, 1632, 112, "euclid_trace.txt")
    produce_trace_table(stein_rec, 1632, 112, "stein_trace.txt")
