# Code in Sätzen
- Mit For- Schleife nach einem der ersten Buchstaben suchen (s, t, k oder i)
- Wenn eines dieser Wörter gefunden ist, wird geprüft, ob der zweite Buchstabe des Wortes im Umfeld liegt
  (Im Fall von tat wäre das a)
- Falls das der Fall ist, mit den nächsten Buchstaben so fortfahren

# Pseudocode
    wordfield[5][5]
    
    words = ["sein", "tat", "kann", "ist"]
    wordcounter = 0
    
    for <zeile < 5> do
        for <spalte < 5> do
            for <k < 4> do
                if <wordfield[zeile][spalte] == words[k][wordcounter]> then
                    if <searchDiagonal(len(words[k], zeile, spalte)> then 
                        print("FOUND WORD")
                        exit
                    endif
                    if <searchHorizontal(len(words[k])> then 
                        print("FOUND WORD")
                        exit
                    endif
                    if <searchVertical(len(words[k])> then 
                        print("FOUND WORD")
                    endif
                endif
            endfor
        endfor
    endfor

    print("No Word found")
    exit
___
    searchDiagonal(len, zeile, spalte)

    // unten rechts oben links
    counter = 0
        for<i < len> do 
            counter++
            zeile--
            spalte--
            if <wordfield[zeile] [spalte] != words[counter]>
                break;
        endfor
        if <counter == len>
            return true
        endif

    // oben rechts unten links
    counter = 0
        for<i < len> do 
            counter++
            zeile++
            spalte--
            if <wordfield[zeile] [spalte] != words[counter]>
                break;
        endfor
        if <counter == len>
            return true
        endif

        // oben links unten rechts
            counter = 0
                for<i < len> do 
                    counter++
                    zeile++
                    spalte++
                    if <wordfield[zeile] [spalte] != words[counter]>
                        break;
                endfor
                if <counter == len>
                    return true
                endif

        // unten links oben rechts
            counter = 0
                for<i < len> do 
                    counter++
                    zeile--
                    spalte++
                    if <wordfield[zeile] [spalte] != words[counter]>
                        break;
                endfor
                if <counter == len>
                    return true
                else
                    return false
                endif

___
    searchHorizontal(len, zeile, spalte)
        // hoch
            counter = 0
                for<i < len> do 
                    counter++
                    zeile++
                    if <wordfield[zeile] [spalte] != words[counter]>
                        break;
                endfor
                if <counter == len>
                    return true
                endif
    
        // runter
            counter = 0
                for<i < len> do 
                    counter++
                    zeile--
                    if <wordfield[zeile] [spalte] != words[counter]>
                        break;
                endfor
                if <counter == len>
                    return true
                else
                    return false
                endif
___
    searchVertical(len, zeile, spalte)
        // rechts
            counter = 0
                for<i < len> do 
                    counter++
                    spalte++
                    if <wordfield[zeile] [spalte] != words[counter]>
                        break;
                endfor
                if <counter == len>
                    return true
                endif
    
        // links
            spalte = 0
                for<i < len> do 
                    counter++
                    zeile--
                    if <wordfield[zeile] [spalte] != words[counter]>
                        break;
                endfor
                if <counter == len>
                    return true
                else
                    return false
                endif
