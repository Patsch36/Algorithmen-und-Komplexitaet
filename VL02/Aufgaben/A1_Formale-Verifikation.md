# Aufgabe 1- Formale Verifikation

````java
do n = StdIn.readInt(); while (n < 0);
// n >= 0
x = 2; y = n; z = 1;
// z*x^y = 2^n, y >= n
while (y > 0) {
    // z*x^y = 2^n, y >= n, y>0
    // z*x^y = 2^n, y >= 0
    if (y % 2 == 1) {
	// z*x^(y-1) = 2^n, y >= n
    z = z * x;
	// z*x^y = 2^n, y - 1 >= n
    y = y – 1;

    }
    
    else {
	// z*x^(y+1) = 2^n, y >= n
    x = x * x;
	// z*x^((y+1)*2) = 2^n, 2*y >= n
    y = y / 2;

    }
    
}
StdOut.println(z);
````

Der Algorithmus berechnet das Ergebnis von 2^n

