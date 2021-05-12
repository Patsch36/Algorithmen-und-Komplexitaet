from math import sqrt
num = pow(10, 6)
print(f"your number is {num}")

factors = []

for i in range(int(sqrt(num)) + 1):
    if (i % 10 != 0) and ((num/i) % 10 != 0) and (i % 1 == 0) and ((num/i) % 1 == 0):
        factors.append((i, int(num/i) ))

print(f"Possible factors are %d {factors}")
