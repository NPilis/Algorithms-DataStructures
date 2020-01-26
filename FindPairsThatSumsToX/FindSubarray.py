
def findSubarray(arr,x):

    complement = dict()
    pairs = set()

    for i in range(0,len(arr)):
        if x - arr[i] in complement.values():
            pairs.add((x-arr[i],arr[i]))
        else:
            complement[i] = arr[i]

    print(pairs)



arr1 = [1,2,4,5,2,7,8,9,9,9]
findSubarray(arr1,11)