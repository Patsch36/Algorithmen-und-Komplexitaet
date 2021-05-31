# Aufgaben

## Aufgabe 1- Sortolympics

In dieser Aufgabe soll die Laufzeit verschiedener Sortierverfahren mittels Zeitmessung verglichen werden. Schreiben Sie dazu ein C‐ , Java‐, (o.a.) Programm, das folgendes leistet: 

- Das Programm liest eine Liste von bis zu 100.000 Ganzzahlen von einer Datei (alternativ von der Tastatur) in ein Array ein.

- Es sortiert diese Liste mittels Selection Sort und Bubble Sort (optional Insert Sort) und stoppt die Zeit, die der Sortiervorgang (ohne Ein‐ und Ausgabe‐Operationen!) benötigt.

- Die sortierte Liste wird wieder in eine Datei (alternativ auf den Bildschirm) ausgegeben. 

- Die für den Sortiervorgang benötigte Zeit wird ausgegeben (Messung siehe timer.c). 

- Per Kommandozeilenparameter sollen der Sortieralgorithmus und die Ein‐ bzw. Ausgabedateien gewählt werden können, z.B.: 

  ````powershell
  sortolympics –[selection │ bubble]
  ````

- Beispielaufruf (Windows) 

  ````powershell
  C:\> sortolympics –selection list_10.txt sorted_10.txt 
  Laufzeit: 0.012 Sekunden 
  ````

  

