file1 = open('input.txt', 'r')
Lines = file1.readlines()

import numpy as np

def getMirro(data):
    # init matrix
    matrix = np.zeros((len(data),len(data[0])))
    smugMatrix = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                matrix[i][j] = 1
                smugMatrix[i][j] = 1
    
    # get ori reflection line
    oriLine = ""
    for direction in ["row", "col"]:
        mirrowIndex = -1
        mirrowLines = 0
        middle = len(matrix) / 2
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
        if mirrowIndex != -1:
            oriLine = direction+str(mirrowIndex)
            break
        else:
            matrix = np.transpose(matrix)

    print("oriLine", oriLine)
    for direction in ["row", "col"]:
        # find same row
        mirrowIndex = -1
        mirrowLines = 0
        middle = len(smugMatrix) / 2
        for x in range(len(smugMatrix)):
            for y in range(len(smugMatrix[0])):
                if smugMatrix[x][y] == 0:
                    smugMatrix[x][y] = 1
                else:
                    smugMatrix[x][y] = 0

                for i in range(1,len(smugMatrix)):
                    if i <= middle:
                        if np.array_equal(smugMatrix[:i], np.flip(smugMatrix[i:2*i],0)):
                            # print("1 mirrowIndex", i, mirrowIndex, mirrowLines)
                            if i > mirrowLines and direction+str(i) != oriLine:
                                mirrowIndex = i
                                mirrowLines = i
                    else:
                        if np.array_equal(smugMatrix[i:], np.flip(smugMatrix[2*i-len(smugMatrix):i],0)):
                            # print("2 mirrowIndex", i, mirrowIndex, mirrowLines)
                            if i > mirrowLines and direction+str(i) != oriLine:
                                mirrowIndex = i
                                mirrowLines = i

                if smugMatrix[x][y] == 0:
                    smugMatrix[x][y] = 1
                else:
                    smugMatrix[x][y] = 0

        if mirrowIndex != -1:
            if direction == "row":
                return 100 * mirrowLines
            return mirrowLines
        else:
            smugMatrix = np.transpose(smugMatrix)



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