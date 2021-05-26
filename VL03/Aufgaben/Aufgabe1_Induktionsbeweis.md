# Aufgabe 1- Induktionsbeweis

## Aufgabenteil a- Laufzeitkomplexität

Komplexität des Algorithmus
$$
f(n)
\begin{cases}
    log_2(n)     		& n \le 2\\
    log_2(\frac{n}{3})	& n > 2
\end{cases}
$$

## Aufgabenteil b- Induktionsbeweis

**Induktionsanfang:** 
$$
f(1) = 1
$$
**Induktionsvoraussetzung:**
$$
f(n) \in n \cdot log(n)
$$
**Induktionsbehauptung:**
$$
f(n) \le n \cdot log(n) + 1
$$
**Induktionsschluss:**
$$
f(n  1) \le (n + 1) \cdot \log(n + 1) + 1
$$

$$
f ( n + 1 ) = 3 \cdot \biggl(\frac{n + 1}{3} \biggr)
$$

$$
= 3 \cdot \biggl(\frac{n + 1}{3} \cdot \log\biggl(\frac{n + 1}{3}\biggr) + 1\biggr)
$$

$$
(n + 1) \cdot \log(n + 1) - (n + 1) \cdot \log(3) + 3
\le (n + 1) \cdot \log( n + 1)
$$

