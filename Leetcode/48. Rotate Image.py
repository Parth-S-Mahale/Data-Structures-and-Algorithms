matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Bruteforce Approach:

""" def rotate(matrix: List[List[int]]) -> None:
        n = len(matrix)
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(0,n):
            for j in range(0,n):
                result[j][(n-1)-i] = matrix[i][j]
    
        return list(result)

print(rotate(matrix)) """

# --------------------------------------------------------------

# Optimal Approach:

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
        
    # Transpose of a matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    # Reverse the Transposed matrix
    for i in range(n):
        matrix[i].reverse()
        
    return matrix 

print(rotate(matrix))