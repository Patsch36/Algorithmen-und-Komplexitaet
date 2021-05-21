# Aufgaben 3

## Aufgabe 1- Induktionsbeweis

Ein bestimmter Algorithmus löse eine Problemstellung mit der Eingabegröße *n* , indem er es in drei (Teil‐)Probleme der Größe *n/3* aufteilt und rekursiv löst.  Ein Problem der Größe *n = 2* oder *n=1* kann der Algorithmus in einem Schritt lösen.

### Aufgabenteil a

Formulieren Sie eine rekursive Funktion ݂, welche die Laufzeit der Methode in Abhängigkeit von n ausdrückt.

### Aufgabenteil b

Beweisen Sie:
$$
f \in O(n \cdot \log(n))
$$
indem Sie durch Induktion zeigen: 
$$
f(n) \le n \cdot \log(n) + 1
$$


Hinweis:
$$
\log\biggl(\frac{a}{b}\biggr) = \log(a) - \log(b)
$$


## Aufgabe 2- Shaker Sort

Shaker Sort ist eine Abwandlung des in der Vorlesung behandelten Sortieralgorithmus Bubble Sort. Sie finden eine Implementierung in der Datei ShakerSort.java. 

- Beschreiben Sie die Vorgehensweise des Sortieralgorithmus und stellen Sie die Unterschiede zu Bubble Sort dar. 
- Schätzen Sie grob die worst‐case Laufzeit des Algorithmus ab (keine genaue Analyse). 
- Ist Shaker Sort stabil? 
- Ein (Sortier‐)Algorithmus arbeitet in‐place, wenn er zusätzlich zu dem Speicherplatz, den die zu bearbeitenden Daten einnehmen, nur eine konstante Menge an Speicher (unabhängig von der zu bearbeitenden Datenmenge) benötigt. Arbeitet Shaker Sort in‐ place?

## Aufgabe 3- Rekursion

In Aufgabe 1.4 haben Sie die Fibonacci‐Folge sowohl rekursiv als auch iterativ berechnet.  Bei der heute vorgestellten binären Suche sind ebenfalls beide Implementierungsvarianten möglich. Es stellt sich die Frage, welche Implementierungsvariante bevorzugt werden sollte.  

Implementieren Sie dazu beide Algorithmen in der Sprache Ihrer Wahl und vergleichen die Laufzeit der rekursiven und iterativen Varianten. Wählen Sie entsprechend große Eingaben, so dass die Laufzeit im Sekundenbereich liegt und damit einfach messbar ist. Wählen Sie ggf. mehrere Eingaben und geben daraufhin eine Abschätzung in O‐Notation für beide Algorithmen (in ihren jeweiligen Implementierungsvarianten) an.  

Was stellen Sie fest? Schildern Sie Ihre Beobachtungen