# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [8,-19,5,-4,20]
# nums = [5,4,-1,7,8]
# nums = [1,-1,1]
nums = [3,-3,2,-3]

def maxSubArray(nums):
    maxSum = nums[0]
    currentArray = nums[0]
    for i in range(1,len(nums)):
        num = nums[i]
        currentArray = max(num, currentArray + num)
        maxSum = max(maxSum, currentArray)
    return maxSum

print("maxSubArray -> ", maxSubArray(nums))