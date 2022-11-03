nums = [1,2,3,4,5,1]

def robHouse(nums):
    if len(nums) <= 3:
        return max(nums)

    dp1 = [0]*(len(nums)) # 0 ~ n-2
    dp2 = [0]*(len(nums)) # 1 ~ n-1
    dp1[1] = nums[0]
    dp2[1] = nums[1]

    for i in range(2, len(nums)):
        dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i-1])
        dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

    # print(dp1)
    # print(dp2)
    return max(dp1[-1],dp2[-1])

print(nums)
print(robHouse(nums))