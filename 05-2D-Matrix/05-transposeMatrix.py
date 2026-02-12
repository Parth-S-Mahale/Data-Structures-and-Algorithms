nums = [[1,2,3], [4,5,6], [7,8,9]]
rows = len(nums)
cols = len(nums[0])
result = [[0]*rows for _ in range(cols)]

for i in range(0, rows):
    for j in range(0, cols):
        result[i][j] = nums[j][i]
        print(result[i][j], end=' ')
    print()