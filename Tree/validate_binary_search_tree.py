class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def getMax(node):
            if node.left == None and node.right == None:
                return node.val
            elif node.left == None and node.right != None:
                return max(node.val, getMax(node.right))
            elif node.left != None and node.right == None:
                return max(node.val, getMax(node.left))
            else:
                return max(node.val, getMax(node.right), getMax(node.left))
            
        def getMin(node):
            if node.left == None and node.right == None:
                return node.val
            elif node.left == None and node.right != None:
                return min(node.val, getMin(node.right))
            elif node.left != None and node.right == None:
                return min(node.val, getMin(node.left))
            else:
                return min(node.val, getMin(node.right), getMin(node.left))
            
        def isTreeValid(node):
            if node == None:
                return True
            if node.right != None:
                if node.val >= getMin(node.right):
                    return False
            if node.left != None:
                if node.val <= getMax(node.left):
                    return False
            return  isTreeValid(node.left) and isTreeValid(node.right)
        return isTreeValid(root)