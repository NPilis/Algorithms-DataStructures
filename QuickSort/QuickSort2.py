def partition(arr,start,end):
    pivot = arr[end]
    i = low - 1

    for j in range(start,end-1):

        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1


def quickSort(arr,start,end):

    if start < end:
        pidx = partition(arr,start,end)

        quickSort(arr,start,pidx-1)
        quickSort(arr,pidx+1,end)

