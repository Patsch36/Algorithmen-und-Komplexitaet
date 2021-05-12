
if __name__=="__main__":
    startnum = int(input("Geben Sie die Startzahl für den Collatz- Algorithmus ein: "))
    row = [startnum]

    while startnum is not 1:
        if startnum % 2 is 1:
            startnum = 3 * startnum + 1
        else:
            startnum = int(startnum / 2)
        row.append(startnum)

    print(row)
    print("Übrigens funktioniert der Collatzalgorithmus nur mit positiven Ganzzahlen größer 0 ;)")
