class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

rootTree = [1,None,2]

# create tree
def createTree(index):
    if index >= len(rootTree):
        return None
    else:
        node = TreeNode(rootTree[index])
        node.left = createTree(2*index+1)
        node.right = createTree(2*index+2)
        return node

def getDepth(subTree):
    if subTree == None:
        return 0
    else:       
        return 1+ max(getDepth(subTree.left), getDepth(subTree.right))

root = createTree(0)
print(getDepth(root))