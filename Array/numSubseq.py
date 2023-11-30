from typing import List

def numSubseq(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)-1
    ans = 0
    nums.sort()
    while left <= right:
        if nums[left] + nums[right] <= target:
            ans += 2**(right-left)
            left += 1
        else:
            right -= 1
    return ans % (7+10**9)

nums = [2,3,3,4,6,7]
target = 12
print(numSubseq(nums, target))