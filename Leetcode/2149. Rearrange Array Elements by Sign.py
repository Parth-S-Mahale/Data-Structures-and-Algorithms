nums=[5, 10, -3, -1, -10, 6]

def rearrangeArray(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
        
    pos_idx, neg_idx = 0, 1

    for i in range(0, n):
        if nums[i] > 0:
            result[pos_idx] = nums[i]
            pos_idx += 2
        else:
            result[neg_idx] = nums[i]
            neg_idx += 2
        
    return result

answer = rearrangeArray(nums)
print(answer)