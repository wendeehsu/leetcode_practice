nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-4,-1,0]

def maxSubArray(nums):
    def getPositive(nums):
        indexs = []
        for i, num in enumerate(nums):
            if num > 0:
                indexs += [i]
        return indexs

    positiveIndexs = getPositive(nums)
    if len(positiveIndexs) == 0:
        return max(nums)
    if len(positiveIndexs) == 1:
        return nums[positiveIndexs[0]]
    
    startIndex = endIndex = positiveIndexs[0]
    maxSum = 0
    for i in range(len(positiveIndexs)):
        for j in range(i,len(positiveIndexs)):
            localSum = sum(nums[positiveIndexs[i]:positiveIndexs[j]+1])
            maxSum = max(maxSum, localSum)
    return maxSum

print("maxSubArray -> ", maxSubArray(nums))