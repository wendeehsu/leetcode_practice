numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# prerequisites = [[1,0],[2,0],[3,1],[3,2],[1,3]]
# prerequisites = [[0,1],[1,2],[0,3],[3,0]]

class Node:
    def __init__(self, val = 0, pre = None):
        self.val = val
        self.pre = pre if pre is not None else []

classMap = {} # value: Node
for pair in prerequisites:
    if pair[0] not in classMap:
        classMap[pair[0]] = Node(pair[0])
    if pair[1] not in classMap:
        classMap[pair[1]] = Node(pair[1])
    classMap[pair[0]].pre += [classMap[pair[1]]]

visited = [0] * numCourses

def traverse(index):    
    print(index, "current visited ->", visited)

    visited[index] = 2 
    if index in classMap:
        currentNode = classMap[index]
        for preCourse in currentNode.pre:
            if visited[preCourse.val] == 2: # visiting
                return False
            elif visited[preCourse.val] == 1: # visited
                continue
            else:
                if traverse(preCourse.val) == False:
                    return False

    visited[index] = 1
    return True

final = True
while sum(visited) != numCourses:
    startIndex = -1
    for index, mark in enumerate(visited):
        if mark == 0:
            startIndex = index
            break
    if traverse(startIndex) == False:
        final = False
        break

print(final)
