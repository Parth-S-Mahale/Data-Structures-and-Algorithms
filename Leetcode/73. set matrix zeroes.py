matrix = [[1,1,1],[1,0,1],[1,1,1]]

# BruteForce Approach:
""" 
def markInfinity(matrix, r_idx, c_idx):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][c_idx] != 0:
            matrix[i][c_idx] = float("inf")

    for j in range(m):
        if matrix[r_idx][j] != 0:
            matrix[r_idx][j] = float("inf")
    

def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markInfinity(matrix, i, j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0
"""

# Optimal Approach:

def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rowtrack = [0 for _ in range(n)]
    coltrack = [0 for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rowtrack[i] = -1
                coltrack[j] = -1

    for i in range(n):
        for j in range(m):
            if rowtrack[i] == -1 or coltrack[j] == -1:
                matrix[i][j] = 0
    
    return matrix

setZeroes(matrix)    
print(matrix)