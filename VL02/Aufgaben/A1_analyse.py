n = int(input("Geben Sie eine Zahl groesser 0 ein"))

x = 2
y = n
z = 1

while y > 0:
	if y%2 == 1:
		z *= x
		y -= 1
	else:
		x = x**2
		y /= 2
print(z)