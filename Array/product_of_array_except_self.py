import math
nums = [-1,1,0,-3,3]
right = [1] * len(nums)
left = [1] * len(nums)

for i in range(1,len(nums)):
    left[i] = left[i-1]*nums[i-1]

for i in range(len(nums)-2,-1,-1):
    right[i] = right[i+1]*nums[i+1]

result = []
for i in range(len(nums)):
    result += [right[i]*left[i]]

print(result)