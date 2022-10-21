nums = [1]

def findMin(nums):
    if nums[0] <= nums[-1]:
        return nums[0]

    midIndex = (len(nums)-1) // 2
    if nums[midIndex] > nums[midIndex+1]:
        return nums[midIndex+1]
    if nums[midIndex] < nums[midIndex-1]:
        return nums[midIndex]

    if nums[0] <= nums[midIndex]:
        return findMin(nums[midIndex:])
    else:
        return findMin(nums[0:midIndex+1])

print(findMin(nums))