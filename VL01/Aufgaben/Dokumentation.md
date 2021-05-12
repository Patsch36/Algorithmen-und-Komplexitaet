# Dokumentation

## Dekoratoren

### Was sind Dekoratoren?

````python
def decorator(function):
    def with_decorator(*args, **kwargs):
        print(function.__name__ + " was called")
        return function(*args, **kwargs)
    return with_decorator

@decorator
def fun(x):
    print("Now the fun- function ist executed")
	return x**2
````

Dekoratoren ersetzen in Python eine Funktion mit einer anderen. So wird bei einem Aufruf von *fun(4)* Beispielsweise erst die decorator- Funktion aufgerufen und dadurch der Name der Funktion ausgegeben und danach erst die eigentlich aufgerufene Funktion durchgeführt.

Im Hintergrund wird die Funktion *fun* mit der Funktion *with_decorator* ersetzt. Der Effekt, dass erst die *decorator*- Funktion aufgerufen wird und danach erst die *func*- Funktion entsteht dadurch, dass erst das print- Statement durchgeführt wird und danach, im return- Statement, die Funktion *func* aufgerufen wird.

Alternativ kann auch geschrieben werden:

````Python
def fun(x):
    print("Now the fun- function ist executed")
    return x**2
fun = decorator(fun)
````

### functool.wraps

In Älteren Python- Versionen wurden Daten von Funktionen, wie zum Beispiel der Name, Parameter, etc. nicht übernommen. Dafür wurde der Dekorator wraps verwendet, um dieses Problem zu lösen.

In neueren Python- Versionen (Getestet in Python 3.9) existiert dieses Problem nicht mehr. Der Dekorator wraps wurde dennoch im Zuge der Abwärtskompatibilität eingefügt.