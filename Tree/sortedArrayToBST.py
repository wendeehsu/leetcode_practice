from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return TreeNode(val=nums[0])
    else:
        mid_index = len(nums)//2
        leftTree = None
        if mid_index - 1 >= 0:
            leftTree = sortedArrayToBST(nums[0:mid_index])
               
        rightTree = None
        if mid_index + 1 < len(nums):
            rightTree = sortedArrayToBST(nums[mid_index+1: len(nums)])
        return TreeNode(val=nums[mid_index], left=leftTree, right=rightTree)

nums = [-10,-3,0,5,9]
print(sortedArrayToBST(nums))