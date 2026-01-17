nums = [1,2,3,4,5,6,7]
k = 5

def rotate(nums: list[int], k: int) :

    n = len(nums)
    k = k % n
        
    def reverse(left, right):
        while left < right:
            nums[left] ,nums[right] = nums[right] ,nums[left]
            left += 1
            right -= 1

    reverse(n-k, n-1)
    reverse(0, n-k-1)
    reverse(0, n-1)

    return nums

print(rotate(nums, k))


""" def rotate(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate(nums, 3)) """

        