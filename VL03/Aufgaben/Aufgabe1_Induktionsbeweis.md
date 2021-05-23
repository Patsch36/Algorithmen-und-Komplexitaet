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
n \cdot log(n) \le n \cdot log(n) + 1
$$
**Induktionsschluss:**
$$
\frac{n \cdot log(n)}{n \cdot log(n)} = 1
$$

$$
1 = 1
$$

$$
q.e.d.
$$

