import math
nums = [1,2,3,4]
left = [1] * len(nums)
result = [1] * len(nums)

for i in range(1,len(nums)):
    left[i] = left[i-1]*nums[i-1]

acc = 1
for i in range(len(nums)-1,-1,-1):
    if i != len(nums)-1:
        acc *= nums[i+1]
    result[i] = left[i]*acc

print(result)