nums = [10,10,10]

num_lens = len(nums)
dp = [1] * num_lens

for i in range(num_lens-1,-1,-1):
    local_max = 1
    for j in range(i+1,num_lens,1):
        if nums[j] > nums[i]: # i can be added before j
            local_max = max(local_max, dp[j]+1)
    dp[i] = local_max
# print(nums)
print(max(dp))