file1 = open('input.txt', 'r')
Lines = file1.readlines()

startPos = []
endPos = []
for i, line in enumerate(Lines):
    Lines[i] = line.replace("\n", "")
    if i == 0:
        startPos = [0, line.index(".")]
    elif i == len(Lines)-1:
        endPos = [len(Lines)-1, line.index(".")]

dMap = {"^":(-1,0), "v":(1,0), ">":(0,1), "<":(0,-1)}

def dfs(pos, direction, visited):
    x,y = pos
    newX = x + dMap[direction][0]
    newY = y + dMap[direction][1]
    if newX < 0 or newX >= len(Lines) or \
        newY < 0 or newY >= len(Lines[0]):
        return None
    if Lines[newX][newY] == "#":
        return None
    # if Lines[newX][newY] == ".":
    key = str(newX) + "_" + str(newY)
    if key in visited:
        return None
    return 1,[newX, newY], key
    # tmpStep = dfs([newX, newY], Lines[newX][newY], visited)
    # if tmpStep == None:
    #     return None
    # return tmpStep[0]+1, tmpStep[1], tmpStep[2]

ans = -1
loc = [[0,startPos,[str(startPos[0]) + "_" + str(startPos[1])]]]
while len(loc) > 0:
    pathLength, pos, visited = loc.pop(0)
    # print(pathLength, pos, visited)
    for direction in "^v><":
        tmpStep = dfs(pos, direction, visited)
        if tmpStep == None:
            continue
        steps, nextPos, key = tmpStep
        newPathLen = pathLength + steps
        print(newPathLen)
        if key == str(endPos[0]) + "_" + str(endPos[1]):
            if newPathLen > ans:
                ans = newPathLen
            continue

        if tmpStep != None:
            loc += [[newPathLen, nextPos, visited+[key]]]


print("ans ->", ans)