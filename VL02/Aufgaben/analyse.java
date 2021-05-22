do n = StdIn.readInt(); while (n < 0);

x = 2; y = n; z = 1;

while (y > 0) {

    if (y % 2 == 1) {
        z = z * x;
        y = y – 1;
        
    } else {
        x = x * x;
        y = y / 2;

    }
    
}
StdOut.println(z);