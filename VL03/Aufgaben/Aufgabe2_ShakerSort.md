# Aufgabe 2- ShakerSort

## Aufgabenteil a- Beschreibung

Der Algorithmus startet so lang einen neuen Sortierdurchlauf, wie wenn im vorherigen Durchlauf noch etwas sortiert wurde. Er terminiert, wenn in einem Durchlauf nichts mehr geändert wurde.

Der Algorithmus rotiert das größte Element der Liste bis zum Ende der Liste und verkürzt dann den Sortierradius um eins, da das Ende der Liste bereits sortiert ist.

Danach rotiert der Algorithmus von end-1 beginnend das kleinste Element an den Anfang der Liste und verkürzt dann den Sortierradius um start + 1, da der Anfang der Liste auch sortiert wurde.

Der Unterschied zu Bubble- Sort ist, dass Bubblesort immer das größere Element von zwei Paaren an die hintere Stelle von dem Paar rotiert und somit schrittweise die größeren Elemente nach hinten rotiert. Allerdings durchläuft Bubblesort bei jedem Durchlauf die ganze Liste, wohingegen bei ShakerSort der Sortierumfang ständig um die bereits sortierten Elemente verkürzt wird.

## Aufgabenteil b- Worst Case Situation

Worst Case ist eine Invers- Sortierte Liste. Dabei müssen n Elemente jeweils die Liste durchlaufen, wobei sich die Länge der Liste jeden Durchlauf um 1 verkürzt.

Die Laufzeit beträgt also n^2.

## Aufgabenteil c- Stabilität

Ja. Sollten zwei gleiche Zahlen aufeinander treffen, wird die hintere der beiden weiter rotiert. Dadurch wird trotzdem der jeweilige Zahlenwert einsortiert.

## Aufgabenteil d- inplace

Der Algorithmus arbeitet "insitu", da er auf den Daten selbst arbeitet. Demnach also nicht inplace.

