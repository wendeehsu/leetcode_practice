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
        node.left = createTree(2*index+1, rootTree)
        node.right = createTree(2*index+2, rootTree)
        return node

def invertTree(node):
    if node == None:
        return None
    else:
        tmpNode = invertTree(node.right)
        node.right = invertTree(node.left)
        node.left = tmpNode
        return node

root = createTree(0,[4,2,7,1,3,6,9])
newTree = invertTree(root)
# while newTree != None:
#     print(newTree.val)
#     newTree = newTree.left