nums = [9,6,4,2,3,5,7,0,1]
n = len(nums); freq = {}

""" def missingNumber(nums ,n):
    for i in range(0,n+1):
        if i in nums:
            continue
        else:
            return i """

""" def missingNumber(nums, n):
    for i in range(0,n+1):
        freq[i] = 0
    
    for num in nums:
        freq[num] = 1
    
    for k,v in freq.items():
        if v == 0:
            return k """


def missingNumber(nums,n):
    sum = 0
    for i in range(0,n):
        sum = sum + nums[i]
    
    return int(n*((n+1)/2) - sum)
    

print(missingNumber(nums,n))