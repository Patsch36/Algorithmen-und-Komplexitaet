# Aufgaben

## Aufgabe 1 - Stack

### Aufgabenteil a

Geben Sie an, welche Ausgabe die println‐Zeile erzeugt, indem Sie zeigen, wie sich der Stack‐Inhalt entwickelt. Achten Sie bei den Operationen (insbesondere bei den Operatoren / und ‐ ) auf die Reihenfolge der Aufrufe von pop(). 

### Aufgabenteil b

Formulieren Sie den zur Berechnung passenden Postfix‐Ausdruck.

### Aufgabenteil c

Formulieren Sie den zur Berechnung passenden Infix‐Ausdruck. 

````java
push(2);
push(3);
push(pop() - pop());
push(4);
push(8);
push(pop() / pop());
push(6);
push(pop() / pop());
push(3);
push(pop() * pop());
push(pop() + pop());
push(5);
push(pop() – pop());
println(pop());
````

## Aufgabe 2 - LinkedQueue



Implementieren Sie den Abstrakten Datentyp Queue anhand des gegebenen Interfaces  Queue.java. Erstellen Sie eine auf Verweise basierende Datenstruktur in der Klasse LinkedQueue. Eine LinkedQueue hat dabei folgende Gestalt: 

![image-20210602113620148](C:\Users\Anwender\AppData\Roaming\Typora\typora-user-images\image-20210602113620148.png)

