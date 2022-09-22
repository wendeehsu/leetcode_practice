numCourses = 3
prerequisites = [[1,0], [0,2]]

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
    # detect cycle
    print(index, "current visited ->", visited)
    if visited[index] == 1:
        return False
    
    visited[index] = 1 # in this cycle

    if index in classMap:
        currentNode = classMap[index]
        for preCourse in currentNode.pre:
            if traverse(preCourse.val) != True:
                return False

    # # finish detect, set to 1
    # for i in range(len(visited)):
    #     if visited[i] == 2:
    #         visited[i] = 1
    return True

while sum(visited) != numCourses:
    startIndex = -1
    for index, mark in enumerate(visited):
        if mark == 0:
            startIndex = index
            break
    if traverse(startIndex) == False:
        print(False)
        break

print(visited)
print(True)
# for i in classMap:
#     print(i)
#     for j in classMap[i].pre:
#         print("->",j.val)
