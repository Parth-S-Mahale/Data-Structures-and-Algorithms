arr = [5,7,3,2,6,1,5,9]

def reverseWhileLoop(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr

reverseWhileLoop(arr, 2, 5)

print(arr)