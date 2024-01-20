from typing import List

def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    
    def hasPeak(startIndex, endIndex):
        print("===", startIndex, endIndex, "===")
        if startIndex == endIndex:
            return startIndex

        middleIndex = (startIndex + endIndex) // 2
        if nums[middleIndex] > nums[middleIndex+1]:
            return hasPeak(startIndex, middleIndex)
        return hasPeak(middleIndex+1, endIndex)
    return hasPeak(0, len(nums)-1)

nums = [1,2]
print(findPeakElement(nums))