nums = [1,2,3,1]
# nums = [2,7,9,3,1]

def startRob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * (1+len(nums))
    dp[1] = nums[0]

    for i in range(2,len(dp)):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
    print(nums)
    print(dp)
    return dp[-1]

print("rob result ->",startRob(nums))