# Aufgabe 1- Stack

## Aufgabenteil a

````
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

|      |      |      |      |      |      |      |      |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |      |      |      |      |      |      |      |
|      |      |      |      | 8    |      | 6    |      | 3    |      |      |      |      |
|      | 3    |      | 4    | 4    | 2    | 2    | 3    | 3    | 9    |      | 5    |      |
| 2    | 2    | 1    | 1    | 1    | 1    | 1    | 1    | 1    | 1    | 10   | 10   | -5   |

Es wird -5 ausgegeben.

## Aufgabenteil b

Postfix: 5 6 8 4 / / 3 * 3 2 - + -

## Aufgabenteil c

Infix: 5 - ((6 / (8 / 4)) * 3 + (3 - 2))

