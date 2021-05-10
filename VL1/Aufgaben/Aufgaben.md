# Aufgaben

## Aufgabe 1

Formulieren Sie einen Algorithmus (in einfachen Sätzen oder Pseudocode), der es ermöglicht, in dem unten gezeigten Buchstabenarray eines der Wörter: **sein**, **tat**, **kann** oder **ist** zu finden. Die Leserichtung für die Wörter kann dabei horizontal, vertikal oder diagonal und jeweils vorwärts und rückwärts sein. Sobald ein Wort gefunden wurde, terminiert der Algorithmus.

| n    | w    | b    | m    | t    |
| ---- | ---- | ---- | ---- | ---- |
| n    | i    | s    | t    | a    |
| a    | e    | e    | p    | t    |
| k    | f    | x    | s    | e    |



## Aufgabe 2- Collatz

Implementieren Sie den Algorithmus zum Collatz‐Problem und testen Sie ihn für verschiedene Eingaben. 

* Finden Sie eine Eingabe, für die der Algorithmus nicht terminiert.

## Aufgabe 3- GGT

Informieren Sie sich über die Möglichkeiten zur algorithmischen Berechnung des GGT. Formulieren Sie eine rekursive Vorschrift zur Berechnung Euklid und Stein ("steinscher Algorithmus"). Schreiben Sie je ein C‐ oder Java‐Programm, das diese beiden Algorithmen umsetzt und eine Trace‐Tabelle produziert. Durch eine solche Tabelle wird jeder Schritt des Ablaufs durch Ausgaben der Variablenwerte nachvollziehbar gemacht. Testen Sie Ihr Programm für verschiedene Eingaben.

## Aufgabe 4- Fibonacci

Die Folge der Fibonacci‐Zahlen ist folgendermaßen definiert: 
$$
F_0 = 0
$$

$$
F_1 = 1
$$

$$
F_n = F_{n - 1} + F_{n - 2}
$$



Somit ist der Wert der Fibonacci‐Zahlen mit den Indizes 0 und 1 genau ihr Index und jede weitere Fibonacci‐Zahl entspricht der Summe ihrer beiden Vorgänger. Die direkte Implementierung zur Berechnung der Fibonacci‐Zahlen mittels Rekursion ist leider sehr ineffizient – warum? 

Implementieren Sie die rekursive Variante und entwerfen Sie einen weiteren Algorithmus zur iterativen Berechnung der Folge bis zu einem (vom Benutzer einzugebenden) *݊n*.

