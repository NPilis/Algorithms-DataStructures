
def selectionSort(tab):
    for j in range(0,len(tab)):
        min = j
        for i in range(j+1,len(tab)):
            if tab[i] < tab[min]:
                min = i

        tab[min],tab[j] = tab[j],tab[min]

    return tab

t1 = [1,4,2,8,3,5]
print(selectionSort(t1))