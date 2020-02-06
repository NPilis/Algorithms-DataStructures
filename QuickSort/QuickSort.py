import random
import datetime

def quickSort(arr,start,stop):
    i = start
    j = stop
    pivot = arr[(start+stop)//2] #choosing middle element as pivot

    while i < j:
        while arr[i] < pivot:
            i+=1
        while arr[j] > pivot:
            j-=1

        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1

    if j > start:
        quickSort(arr,start,j)
    if i < stop:
        quickSort(arr,i,stop)

