nums = [5, 1, 6, 8, 2, 4, 9]

def bubbleSort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(0 , i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums
print(bubbleSort(nums))