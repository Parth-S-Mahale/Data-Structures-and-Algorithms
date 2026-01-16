nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

""" def maxSubArray(nums) -> int:
    n = len(nums)
    max_sum = float("-inf")
    total = 0
    for i in range(0,n):
        total = 0
        for j in range(i ,n):
            total += nums[j]
            max_sum = max(max_sum, total)
    
    return int(max_sum) """

def maxSubArray(nums) -> int:
    n = len(nums)
    max_sum = float("-inf")
    total = 0
    for i in range(0,n):
        total += nums[i]
        max_sum = max(max_sum, total)
        if total < 0: 
            total = 0
    
    return int(max_sum)

print(maxSubArray(nums))
        