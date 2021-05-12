# ReadMe

## Informationen zu Aufgabe 4

Da in Kotlin die Option besteht, rekursive Funktionen als tailrec zu deklarieren, soll das auch angeführt werden.

Bei tailrec- Funktionen optimiert der Compiler die Funktionen in eine Funktionen mit iterativen Zügen und optimiert dabei leicht die Laufzeit.

Zur vereinfachten Ausführung ist das Kotlin- Skript (.kt) zu einer Jar Datei compiled, die bei installierter Java- Umgebung mit 

```shell
java -jar Aufgabe3_GGT.jar
```

ausgeführt werden kann.

## Kotlin- Datei compilen

Wer das Kotlin- Skript compilen möchte, muss sich den Kotlin Compiler unter https://github.com/JetBrains/kotlin/releases/tag/v1.5.0 downloaden. Entpackt man die .zip Datei, muss untern den Umgebungsvariablen -> Sstemvariablen -> Path das bin- Verzeichnis eingefügt werden.

Es empfiehlt sich, aus dem Windows Fileexplorer den Pfad zu kopieren. Über den Browse Dialog hat Windows manchmal Probleme, den fad korrekt zu erkennen.

Bei Erfolg kann die Datei mit 

````shell
kotlinc Aufgabe3_GGT.kt -include-runtime -d Aufgabe3_GGT.jar
````

compiled werden.