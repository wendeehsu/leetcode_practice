class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isTreeValid(node, high=2**31+1, low=-2**31-1):
            if node == None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return isTreeValid(node.right, high, node.val) and isTreeValid(node.left, node.val, low)
        return isTreeValid(root)