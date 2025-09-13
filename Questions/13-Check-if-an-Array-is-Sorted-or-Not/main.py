arr = [3,5,6,7,8,9,10,20]

def isSorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
                
    return True

print(isSorted(arr))