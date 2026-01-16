arr = [5,7,3,2,6,1,5,9]

def reverseArray(arr, left, right):
    if left >= right:
        return
    
    arr[left], arr[right] = arr[right], arr[left]
    reverseArray(arr, left+1, right-1)
    
reverseArray(arr, 2, 5)    

print(arr)