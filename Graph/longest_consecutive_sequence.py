nums = [100,4,200,1,3,2]

def getSequence(nums):
    nums = set(nums)
    globalBest = 0
    for num in nums:
        if num-1 not in nums:
            localBest = 1
            point = num
            while point+1 in nums:
                point += 1
                localBest += 1
            globalBest = max(globalBest, localBest)
    return globalBest

print(getSequence(nums))