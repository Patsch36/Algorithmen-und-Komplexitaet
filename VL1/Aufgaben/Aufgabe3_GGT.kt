import java.math.BigInteger

/*
*   Tailrec Function : Recursive Functions
*       -> Prevents Stackoverflow Exception
*
*   Fibonacci Series
*       0  1  1  2  3  5  8  13  21 ......
* */
fun main(args: Array<String>) {

    System.out.println("Zwei mal der selbte Algorithmus: Der erste als traditionelle Rekursion, der zweite als Kotlin's Tailrec (Errechnen der 40. Fibonacci Zahl)")

    var time: Double = -System.currentTimeMillis().toDouble()
    println(getFibonacciNumber(40))
    System.out.println(((time + System.currentTimeMillis().toDouble())/1000).toString() + "s")

    time = -System.currentTimeMillis().toDouble()
    println(getFibonacciNumberTailrec(40))
    System.out.println(((time + System.currentTimeMillis().toDouble() )/1000).toString() + "s")
}

fun getFibonacciNumber(n: Int): BigInteger {

    if (n <= 1)
        return BigInteger.ONE
    else
        return getFibonacciNumber(n - 1) + getFibonacciNumber(n - 2)
}

tailrec fun getFibonacciNumberTailrec(n: Int): BigInteger {

    if (n <= 1)
        return BigInteger.ONE
    else
        return getFibonacciNumber(n - 1) + getFibonacciNumber(n - 2)
}