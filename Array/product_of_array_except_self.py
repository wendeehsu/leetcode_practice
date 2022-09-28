import math
nums = [-1,1,0,-3,3]

total = math.prod(nums)
def getOtherProduct(index,num):
    if num == 0:
        return math.prod(nums[:index] + nums[index+1:])
    else:
        return total//num

result = []
for i, num in enumerate(nums):
    result += [getOtherProduct(i,num)]

print(result)