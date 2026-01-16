nums = [5 ,3 ,9 ,8 ,1 ,6 , 4, -10, -100]
target = int(input("Enter the target element:"))
n = len(nums)

def LS(nums, target, n):
    for i in range(0,n):
        if nums[i] == target:
             print(f"Index of {target}: {i}")
    
   
LS(nums, target, n)
