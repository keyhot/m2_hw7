from bubblesort import bubbleSort
from selectionsort import selectionSort
from quicksort import quickSort
import random

def binary_search(toFind, list):
    n = len(list)
    resultOk = False
    first = 0
    last = n - 1
    pos = 0

    while first <= last:
        middle = (first + last) // 2
        if toFind == list[middle]:
            first = middle
            last = first
            resultOk = True
            pos = middle
            break
        else:
            if toFind > list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if resultOk == True:
        print("Элемент найден")
        print(pos)
    else:
        print("Элемент не найден")

list = random.sample(range(0, 100), 100)
print(list)
newlist = selectionSort(list)
print(newlist)
binary_search(0, newlist)

list = random.sample(range(0, 100), 100)
print(list)
newlist = bubbleSort(list)
print(newlist)
binary_search(99, newlist)

list = random.sample(range(0, 100), 100)
print(list)
newlist = quickSort(list)
print(newlist)
binary_search(99, newlist)