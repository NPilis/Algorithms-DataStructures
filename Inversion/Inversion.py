
def inversion(arr,inv):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        inversion(L,inv)
        inversion(R,inv)

        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                inv[0] += len(L[i:]) #amount of inversions
                # for elem in L[i:]:
                #     inv.append([elem,R[j]])
                arr[k] = R[j]
                j+=1
            else:
                arr[k] = L[i]
                i+=1
            k+=1

        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [5,4,3,2,1]
inv = [0]
inversion(arr,inv)
print(inv)
print(arr)
