from typing import List

def maxFrequency(nums: List[int], k: int) -> int:
    if len(nums) == 1:
        return 1
    nums.sort(reverse=True)
    maxFreq = 1
    left = 0
    right = 1

    chanceUsed = 0
    pivot = nums[left]
    while right < len(nums):
        # print(left, right, chanceUsed)
        chanceUsed += pivot - nums[right]
        while chanceUsed > k:
            gap = pivot - nums[left+1]
            # print("gap:", gap, pivot)
            chanceUsed -= gap * (right-left)
            left += 1
            pivot = nums[left]
        else:
            maxFreq = max(maxFreq, right-left+1)
            right += 1

    return maxFreq

nums = [1,2,4]
k = 5
print(maxFrequency(nums, k))