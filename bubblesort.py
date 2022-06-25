def swap(i, j, list):
    c = list[i]
    list[i] = list[j]
    list[j] = c

def bubbleSort(list):
    n = len(list) - 1
    newlist = list.copy()
    for i in range(len(newlist)):
        for j in range(n):
            if newlist[j] > newlist[j + 1]:
                swap(j, j + 1, newlist)
    return newlist
