nums = [4,1,7,6,3,2,8]

def quickSort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quickSort(nums, low, pivot_index - 1)
        quickSort(nums, pivot_index + 1, high)
    
    return nums
        

def partition(nums, low, high):
    pivot = nums[low]
    i, j = low, high
    
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
            
        while nums[j] > pivot and j >= low + 1:
            j -= 1 
            
        if i < j:
            nums[i],nums[j] = nums[j],nums[i]
    
    nums[low],nums[j] = nums[j],nums[low]
    
    return j

print(quickSort(nums, 0, 6))