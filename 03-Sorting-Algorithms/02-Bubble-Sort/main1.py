# nums = [1, 2, 3, 4, 5, 6, 7] # sorted Array/List

nums = [5, 1, 6, 8, 2, 4, 9] # unsorted Array/List

def bubbleSort(nums):
    n = len(nums)
    is_swapped = False
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swapped = True
        if is_swapped == False:
            return f"The Given Array/List is sorted!"
    return nums

print(bubbleSort(nums))