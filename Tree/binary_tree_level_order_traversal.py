root1 = []

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# create tree
def createTree(index, rootTree):
    if index >= len(rootTree):
        return None
    else:
        node = TreeNode(rootTree[index])
        node.left = createTree(2*index+1,rootTree)
        node.right = createTree(2*index+2,rootTree)
        return node

root = createTree(0,root1)

def traverseTree(root):
    global toVisit
    if root != None:
        if root.left != None:
            toVisit += [root.left]
        if root.right != None:
            toVisit += [root.right]

toVisit = [root]
resultList = []
index = -1
while len(toVisit) > 0:
    resultList += [[]]
    index += 1
    length = len(toVisit)
    # print(index,toVisit)
    for i in range(length):
        currentNode = toVisit.pop(0)
        if currentNode != None and currentNode.val != None:
            resultList[index] += [currentNode.val]
            traverseTree(currentNode)

print(resultList)