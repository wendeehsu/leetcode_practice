root1 = [3,4,5,1,2]
subRoot1 = [3,1,2]

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

def traverseTree(root, subRoot):
    if root == None and subRoot == None:
        return True
    elif root != None and subRoot != None:
        if root.val == subRoot.val:
            if traverseTree(root.left, subRoot.left) and \
                traverseTree(root.right, subRoot.right):
                return True
            return False
    return False

def findStart(root, subRoot):
    if root != None:
        if root.val == subRoot.val:
            if traverseTree(root,subRoot):
                return True
        return findStart(root.left,subRoot) or findStart(root.right,subRoot)
    else:
        return False

def printTree(root):
    if root.left and root.right:
        print(root.val, "left:",root.left.val, "right:",root.right.val)
        printTree(root.left)
        printTree(root.right)
    elif root.left == None and root.right == None:
        print(root.val, "end")
    else:
        print(root.val, "left:",root.left.val)
        printTree(root.left)
        try:
            print(root.val, "left:",root.left.val, "right:",root.right.val)
            printTree(root.right)
        except Exception as e:
            print("eeeeeeee",e)

root = createTree(0,root1)
subRoot = createTree(0,subRoot1)
print(findStart(root,subRoot))