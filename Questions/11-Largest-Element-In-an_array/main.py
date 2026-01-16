arr = [3,5,6,7,20,8,9,10]

def largest(arr):
    largest = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        
    return largest
    
print(largest(arr))
