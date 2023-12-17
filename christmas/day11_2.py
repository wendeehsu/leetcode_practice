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

def getDis(startPos, endPos):
    global expandDic
    rowExpand = 0
    for index in expandDic["row"]:
        if index > min(startPos[0], endPos[0]) and \
            index < max(startPos[0], endPos[0]):
            rowExpand += (1000000-1) # <-----------update
    colExpand = 0
    for index in expandDic["col"]:
        if index > min(startPos[1], endPos[1]) and \
            index < max(startPos[1], endPos[1]):
            colExpand += (1000000-1) # <-----------update
    w = abs(endPos[1]-startPos[1])+colExpand+1
    h = abs(endPos[0]-startPos[0])+rowExpand+1
    if w == 1 or h == 1:
        return max(w,h)-1
    sl = min(w,h)
    # print(startPos, endPos, rowExpand, colExpand, 2* (sl-1) + max(w,h)- sl)

    return 2* (sl-1) + max(w,h)- sl

ans = 0
expandDic = expand(valueMap)
print("expandDic", expandDic)
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