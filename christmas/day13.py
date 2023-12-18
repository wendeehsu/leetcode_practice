file1 = open('input.txt', 'r')
Lines = file1.readlines()

import numpy as np

def getMirro(data):
    # init matrix
    matrix = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                matrix[i][j] = 1
    
    for direction in ["row", "col"]:
        # find same row
        mirrowIndex = -1
        mirrowLines = 0
        middle = len(matrix) /2
        for i in range(1,len(matrix)):
            if i <= middle:
                if np.array_equal(matrix[:i], np.flip(matrix[i:2*i],0)):
                    if i > mirrowLines:
                        mirrowIndex = i
                        mirrowLines = i
            else:
                if np.array_equal(matrix[i:], np.flip(matrix[2*i-len(matrix):i],0)):
                    if i > mirrowLines:
                        mirrowIndex = i
                        mirrowLines = i
        print(direction, "mirrow", mirrowIndex, mirrowLines)
        if mirrowIndex != -1:
            if direction == "row":
                return 100 * mirrowLines
            return mirrowLines
        else:
            matrix = np.transpose(matrix)



data = []
ans = 0
for line in Lines:
    line = line.replace("\n","")
    if line == "":
        print("=== start count")
        result = getMirro(data)
        print("result", result)
        ans += result
        data = []
    else:
        # add to list
        data += [line]

print("ans -->", ans)