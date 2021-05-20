# Karten sortieren

|      | Kreuz | Pik  | Herz | Karo |
| ---- | ----- | ---- | ---- | ---- |
| A    | 1     | 21   | 41   | 61   |
| 2    | 2     | 22   | 42   | 62   |
| 3    | 3     | 23   | 43   | 63   |
| 4    | 4     | 24   | 44   | 64   |
| 5    | 5     | 25   | 45   | 65   |
| 6    | 6     | 26   | 46   | 66   |
| 7    | 7     | 27   | 47   | 67   |
| 8    | 8     | 28   | 48   | 68   |
| 9    | 9     | 29   | 49   | 69   |
| 10   | 10    | 30   | 50   | 70   |
| J    | 11    | 31   | 51   | 71   |
| Q    | 12    | 32   | 52   | 72   |
| K    | 13    | 33   | 53   | 73   |

````python
from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)
````



