class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

rootTree = [-10,-9,20,-16,-21,15,-7]

# create tree
def createTree(index):
    if index >= len(rootTree):
        return None
    else:
        node = TreeNode(rootTree[index])
        node.left = createTree(2*index+1)
        node.right = createTree(2*index+2)
        return node

root1 = createTree(0)

currentMax = -9999
def maxGain(root):
    global currentMax
    if root == None or root.val == None:
        return 0
    # print("ttl ->", root.val)
    leftGain = max(0,maxGain(root.left))
    rightGain = max(0,maxGain(root.right))

    newPath = root.val + leftGain + rightGain

    if currentMax < newPath:
        # print("start new root->", root.val)
        currentMax = newPath

    return root.val+max(leftGain,rightGain)

maxGain(root1)
print(currentMax)
