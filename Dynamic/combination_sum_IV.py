nums = [1,2]
target = 10
minValue = 0
dp = [minValue]*(target+1)
dp[0] = 1

for i in range(len(dp)):
    methods = dp[i]       
    for num in nums:
        if num <= i:
            if dp[i-num] > 0:
                methods += dp[i-num]
    
    dp[i] = methods

print(nums)
print(dp)
print(dp[-1])