import datetime
import random

def heapify(arr,hs,i):
    left = 2*i + 1
    right = 2*i + 2

    if left < hs and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right < hs and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,hs,largest)

def buildHeap(arr,hs):
    for i in range(hs//2 - 1,-1,-1):
        heapify(arr,hs,i)

def heapSort(arr):
    hs = len(arr)
    buildHeap(arr,hs)

    for i in range(hs-1,1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)

    if arr[0] > arr[1]:
        arr[0],arr[1] = arr[1],arr[0]

arr1 = [random.randint(0,100000) for i in range(100000)]

t1 = datetime.datetime.now()
heapSort(arr1)
t2 = datetime.datetime.now()
print(t2-t1)