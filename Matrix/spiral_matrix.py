matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def spiral(matrix):
    if matrix == None or len(matrix) == 0:
        return None
    subList = matrix.pop(0)
    matrix = list(zip(*matrix))[::-1]
    nextMatrix = spiral(matrix)
    if nextMatrix != None:
        subList += nextMatrix
    return subList

print(spiral(matrix))