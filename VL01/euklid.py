# eucid algorithm

def euclid():
    num1 = 1632
    num2 = 112
    counter = 0
    while num1 % num2 is not 0:
        num1, num2 = num2, num1 % num2
        counter += 1
    print(f"Der größte gemeinsame Teiler ist {num2}, dazu wurden {counter} Rechenschritte gebraucht")


if __name__ == "__main__":
    euclid()