
def merge(tab,l,m,r):

    L = []
    R = []

    n1 = m-l+1
    n2 = r-m

    for i in range(0,n1):
        L.append(tab[l+i])
    for j in range(0,n2):
        R.append(tab[m+j+1])

    i = 0
    j = 0
    k = l
    while(i < n1 and j < n2):
        if L[i] < R[j]:
            tab[k] = L[i]
            i+=1
        else:
            tab[k] = R[j]
            j+=1
        k+=1

    while i < n1:
        tab[k] = L[i]
        i+=1
        k+=1
    while j < n2:
        tab[k] = R[j]
        j+=1
        k+=1


def mergeSort(tab,l,r):
    if l < r:
        m = (l+r)//2
        mergeSort(tab,l,m)
        mergeSort(tab,m + 1, r)
        merge(tab,l,m,r)

s1 = [1,4,5,2,3,8,7]
mergeSort(s1,0,len(s1)-1)
print(s1)


def mergeSort2(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort2(L)
        mergeSort2(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



s2 = [1,4,5,2,3,8,7]
mergeSort2(s2)
print(s2)