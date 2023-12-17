file1 = open('input.txt', 'r')
Lines = file1.readlines()

import numpy as np

# matrix to numpy
valueMap = np.zeros((len(Lines), len(Lines[0])-1))

for i in range(len(Lines)):
    for j in range(len(Lines[0])-1):
        if Lines[i][j] == '#':
            valueMap[i][j] = 1

def expand(vmap):
    # expand rows
    expandDic = {}
    for flip in ["row","col"]:
        expandDic[flip] = []
        index = 0
        while index < len(vmap):
            if vmap[index].sum() == 0:
                expandDic[flip] += [index]
            index += 1
        vmap = np.transpose(vmap)
    return expandDic

"""
def getClosest(x,y,vmap):
    dp = np.zeros(vmap.shape)
    dp.fill(vmap.shape[0]*vmap.shape[1])
    dp[x][y] = 0

    totalDis = 0
    hasMin = False
    border = 1
    startToGet = starNum -1
    while True:
        pos = [(x, y-border), (x, y+border), (x-border, y), (x+border,y)]
        for j in range(y-border, y+border+1):
            pos += [(x-border, j), (x+border,j)]
        for i in range(x-border+1, x+border):
            pos += [(i, y-border), (i, y+border)]
        
        for i, j in pos:
            if i < 0 or i >= len(dp) or \
                j < 0 or j >= len(dp[0]):
                continue
            
            if i == x or j == y:
                dp[i][j] = border

            if i < x:
                if j < y:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])
                elif j > y:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
            elif i > x:
                if j < y:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j+1])
                elif j > y:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
            
            if vmap[i][j] == 1:
                startToGet -= 1
                minDis = min(minDis, dp[i][j])
                # print("can be min:",i,j, dp[i][j])
        if hasMin:
            return minDis
        border += 1
"""

def getDis(startPos, endPos):
    w = abs(endPos[1]-startPos[1])+1
    h = abs(endPos[0]-startPos[0])+1
    if w == 1 or h == 1:
        return max(w,h)-1
    sl = min(w,h)
    return 2* (sl-1) + max(w,h)- sl



ans = 0
expandDic = expand(valueMap)
print(expandDic)
allPair = []
starPos = []
for i in range(len(valueMap)):
    for j in range(len(valueMap[0])):
        if valueMap[i][j] == 1:
            starPos.append((i,j))

for i in range(len(starPos)):
    for j in range(i+1, len(starPos)):
        allPair += [[starPos[i], starPos[j]]]
print("stars", len(starPos))
print("allPair nums:", len(allPair))

for startPos, endPos in allPair:
    d = getDis(startPos, endPos)
    ans += d
    # print(startPos, endPos, "-->", d)

print("ans ->", ans)