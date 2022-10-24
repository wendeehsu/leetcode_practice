nums = [1,2,3,1]
# nums = [2,7,9,3,1]
# nums = [1,1]

def startRob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    currentMax = lastMax = 0
    for i in range(len(nums)):
        tmp = currentMax
        currentMax = max(lastMax + nums[i], currentMax)
        lastMax = tmp

    # print(nums)
    return currentMax

print("rob result ->",startRob(nums))