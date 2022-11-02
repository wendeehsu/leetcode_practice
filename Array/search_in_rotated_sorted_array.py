nums = [4,5,6,7,0,1,2]
target = 0

def searchIndex(startIndex, endIndex, nums, target):
    # print(startIndex, endIndex, ":", nums[startIndex], nums[endIndex])
    if target == nums[startIndex]:
        return startIndex
    
    if target == nums[endIndex]:
        return endIndex
    
    if startIndex == endIndex and target != nums[startIndex]:
        return -1
    
    middleIndex = (endIndex+startIndex) // 2
    
    # no rotate
    if nums[startIndex] <= nums[middleIndex]:
        if target > nums[startIndex] and target <= nums[middleIndex]:
            return searchIndex(startIndex+1, middleIndex, nums, target)
        else:
            return searchIndex(middleIndex, endIndex-1, nums, target)
    else:
        if target >= nums[middleIndex] and target < nums[endIndex]:
            return searchIndex(middleIndex, endIndex-1, nums, target)
        else:
            return searchIndex(startIndex+1, middleIndex, nums, target)
    
def getIndex(nums, target):
    return searchIndex(0, len(nums)-1, nums, target)

print(getIndex(nums, 0))