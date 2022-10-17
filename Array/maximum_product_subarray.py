import math
nums = [-2,0,-1]

def getMax():
    global nums
    currentProduct = math.prod(nums)
    if currentProduct > 0:
        return currentProduct
    elif currentProduct == 0:
        # find zeros
        zeroIndexs = []
        for i,num in enumerate(nums):
            if num == 0:
                zeroIndexs.append(i)
        # print(zeroIndexs)
        sublists = []
        for i in range(len(zeroIndexs)):
            if i == 0:
                sublists += [nums[0:zeroIndexs[i]]]
            else:
                sublists += [nums[zeroIndexs[i-1]+1:zeroIndexs[i]]]
        sublists += [nums[zeroIndexs[-1]+1:]]
        
        maxProduct = max(nums)
        for sublist in sublists:
            # handle minus max
            if len(sublist) > 0:
                maxProduct = max(maxProduct,handleNegList(sublist))
        return maxProduct
    else:
        # handle minus max           
        return handleNegList(nums)

def handleNegList(sublist):
    currentProduct = math.prod(sublist)
    if currentProduct > 0:
        return currentProduct
    maxProduct = max(sublist)
    for i in range(len(sublist)):
        if sublist[i] < 0:
            left = sublist[0:i]
            right = sublist[i+1:]
            if len(left) > 0:
                maxProduct = max(maxProduct,math.prod(left))
            if len(right) > 0:
                maxProduct = max(maxProduct,math.prod(right))
    # print(sublist,maxProduct)
    return maxProduct


print(getMax())