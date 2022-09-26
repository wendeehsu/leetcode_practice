matrix = [[1,2,3],[4,5,6],[7,8,9]]

"""
1. rotate by diagnosis
2. reverse each list
"""
matrix_len = len(matrix)
if matrix_len > 1:
    for i in range(matrix_len):
        for j in range(i+1, matrix_len):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(matrix_len):
        matrix[i].reverse()
    print(matrix)