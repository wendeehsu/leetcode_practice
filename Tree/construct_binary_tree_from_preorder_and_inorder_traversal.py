preorder = [3,9,20,15]
inorder = [9,3,15,20]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None
        
    rootValue = preorder[0]
    rootNode = TreeNode(rootValue)
    if len(preorder) == 1:
        return rootNode
    
    rootIndex = inorder.index(rootValue)
    left_inorder = inorder[:rootIndex]
    right_inorder = inorder[(rootIndex+1):]
    
    left_preorder = preorder[1:len(left_inorder)+1]
    right_preorder = preorder[(1+len(left_inorder)):]

    rootNode.left = buildTree(left_preorder, left_inorder)
    rootNode.right = buildTree(right_preorder, right_inorder)
    
    return rootNode
    # print(left_inorder)
    # print(left_preorder)
    # print(right_inorder)
    # print(right_preorder)

printTree(buildTree(preorder, inorder))
