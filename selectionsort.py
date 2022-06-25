def selectionSort(list):
    list2 = list.copy()
    newlist = []
    for i in range(len(list)):
        min = list2[0]
        for j in range(1, len(list2)):
            if list2[j] < min:
                min = list2[j]
        newlist.append(min)
        list2.remove(min)
    return newlist