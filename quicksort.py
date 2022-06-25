from bubblesort import swap

def partition(list, l, h):
    pivot = list[l]
    i = l
    j = h

    while i < j:
        while list[i] <= pivot:
            if i == h:
                break
            i += 1
        while list[j] > pivot:
            if j == l:
                break
            j -= 1
        if i < j:
            swap(i, j, list)
    swap(l, j, list)
    return j

def quickSort2(list, l, h):
    if l < h:
        j = partition(list, l, h)
        quickSort2(list, l, j)
        quickSort2(list, j + 1, h)

def quickSort(list):
    newlist = list.copy()
    quickSort2(newlist, 0, len(list) - 1)
    return newlist