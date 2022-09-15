matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def traverse(direction):
    if matrix == None or len(matrix) == 0:
        return None
    if len(matrix[0]) == 0:
        return None

    sublist = []
    match direction % 4:
        case 0:
            # print("->")
            sublist = matrix.pop(0)
        case 1:
            # print("v")
            for row in matrix:
                sublist += [row.pop(-1)]
        case 2:
            # print("<-")
            sublist = matrix.pop(-1)
            sublist.reverse()
        case 3:
            # print("^")
            for index in range(len(matrix)-1, -1, -1):
                sublist += [matrix[index].pop(0)]
    
    direction += 1
    nextList = traverse(direction)
    if nextList != None:
        sublist += nextList
    # print(sublist)
    return sublist

direction = 0
traverseList = traverse(direction)
print("traverseList", traverseList)