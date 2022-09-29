
heights = [[1,2,3],[8,9,4],[7,6,5]]

def printMatrix(m):
    for i in m:
        print(i)

def initMatrix():
    m = len(heights[0])
    n = len(heights)
    pa_matrix = [[1]*m]
    for row in range(1,n):
        pa_matrix += [[1] + (m-1)*[0]]
    
    at_matrix = []
    for row in range(n-1):
        at_matrix += [(m-1)*[0]+[1]]
    at_matrix += [[1]*m]
    
    return pa_matrix, at_matrix

pa_matrix, at_matrix = initMatrix()

# pacific
for i in range(1,len(heights)):
    for j in range(1,len(heights[0])):
        if heights[i][j] >= heights[i-1][j]:
            pa_matrix[i][j] = max(pa_matrix[i][j],pa_matrix[i-1][j])
        if heights[i][j] >= heights[i][j-1]:
            pa_matrix[i][j] = max(pa_matrix[i][j],pa_matrix[i][j-1])


# atlantic
for i in range(len(heights)-2,-1,-1):
    for j in range(len(heights[0])-2,-1,-1):
        if heights[i][j] >= heights[i+1][j]:
            at_matrix[i][j] = max(at_matrix[i][j],at_matrix[i+1][j])
        if heights[i][j] >= heights[i][j+1]:
            at_matrix[i][j] = max(at_matrix[i][j],at_matrix[i][j+1])

result = []
for i in range(len(heights)):
    for j in range(len(heights[0])):
        if at_matrix[i][j] == 1 and pa_matrix[i][j] == 1:
            result += [[i,j]]
# printMatrix(pa_matrix)
# print("--")
# printMatrix(at_matrix)
print(result)