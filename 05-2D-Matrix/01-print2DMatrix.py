nums = [[1,2,3], [4,5,6], [7,8,9]]
rows = len(nums)
cols = len(nums[0])

for i in range(0, rows):
    for j in range(0, cols):
        print(nums[i][j], end=' ')
    print()