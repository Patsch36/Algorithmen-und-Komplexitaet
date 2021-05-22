/************************  Laufzeiten.java  *************************/
import java.util.Scanner;

/**
 * Bestimmung der Komplexitaet in O-Notation
 */
public class laufzeiten {

    public static int a(int n) {
        int z = 0;

        while (n > 1) {
            n = n / 2;
            z++;
        }
        return z;
    }

    public static int b(int n) {
        int i = 0;
        int b = 1;

        while (++i < n) {
            b = b + 2 * i + 1;
        }
        return b;
    }

    public static int c(int n) {
        int t = 1, z = 0;

        while (n > 0) {
            n = n - t;
            t = t + 2;
            z++;
        }
        return z;
    }

    public static int d(int n) {
        return c(a(n));
    }

    public static int e(int n) {
        return b(c(n));
    }

    public static int f(int n) {
        return c(b(n));
    }

    public static int g(int n) {
        int z = 0;

        for (int i = 1; i <= c(n); i++)
            z = z + c(n);

        return z;
    }

    public static int h(int n) {
        int z = 0;
        int y = c(n);

        for (int i = 1; i <= y; i++)
            z = z + c(n);

        return z;
    }

    public static int i(int n) {
        return c(n) + a(n);
    }

    public static int j(int n) {
        return b(b(n));
    }

    /** Hauptprogramm */
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);

        /* do {
            System.out.printf("Eingabe von n: ");
            n = sc.nextInt();
        } while (n < 1); */


        n = Integer.parseInt(args[0]);

        System.out.printf("a(" + n + ") =");
        System.out.printf("%8d\n", a(n));

        System.out.printf("b(" + n + ") =");
        System.out.printf("%8d\n", b(n));

        System.out.printf("c(" + n + ") =");
        System.out.printf("%8d\n", c(n));

        System.out.printf("d(" + n + ") =");
        System.out.printf("%8d\n", d(n));

        System.out.printf("e(" + n + ") =");
        System.out.printf("%8d\n", e(n));

        System.out.printf("f(" + n + ") =");
        System.out.printf("%8d\n", f(n));

        System.out.printf("g(" + n + ") =");
        System.out.printf("%8d\n", g(n));

        System.out.printf("h(" + n + ") =");
        System.out.printf("%8d\n", h(n));

        System.out.printf("i(" + n + ") =");
        System.out.printf("%8d\n", i(n));

        System.out.printf("j(" + n + ") =");
        System.out.printf("%8d\n", j(n));
    }
}