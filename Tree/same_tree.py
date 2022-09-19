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

def compareTree(tree1, tree2):
    if tree1 == None and tree2 != None:
        return False
    if tree1 != None and tree2 == None:
        return False
    if tree1 == None and tree2 == None:
        return True
    if tree1.val != tree2.val:
        return False
    
    return compareTree(tree1.right, tree2.right) and compareTree(tree1.left, tree2.left)

print(compareTree(createTree(0,[1,2,3]), createTree(0,[1,2,4])))