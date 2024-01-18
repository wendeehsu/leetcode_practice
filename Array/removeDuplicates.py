from typing import List

def removeDuplicates(nums: List[int]):
    if len(nums) < 3:
        return len(nums)
    
    left = 0
    right = 0

    def update(left, right):
        nonlocal nums
        diff = right - left
        while diff > 2:
            nums.pop(left)
            diff -= 1
        left += 2
        right = left
        return left, right

    while right < len(nums):
        if nums[left] == nums[right]:
            if right == len(nums) - 1:
                left, right = update(left, right+1)
            else:
                right += 1
        else:
            if right - left > 2:
                left, right = update(left, right)
            else:
                left = right
    
    return len(nums)

nums = [1,1,1,1,2,3]
print(nums)
print(removeDuplicates(nums), nums)

