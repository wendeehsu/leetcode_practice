file1 = open('input.txt', 'r')
Lines = file1.readlines()

directions = {"-1_0": ["7", "F", "|"], \
            "1_0": ["J", "L", "|"], \
            "0_1": ["-", "J", "7"], \
            "0_-1": ["-", "F", "L"]}
symbolToDirection = { \
    "|" : [(-1,0), (1,0)], \
    "-" : [(0,-1), (0,1)], \
    "L" : [(-1,0), (0,1)], \
    "J" : [(-1,0), (0,-1)], \
    "7" : [(1,0), (0,-1)], \
    "F" : [(1,0), (0,1)]}

toExplore = []
for i,line in enumerate(Lines):
    Lines[i] = list(Lines[i].replace("\n",""))
    for j, symbol in enumerate(line):
        if symbol == "S":
            for d in [(0,1), (0,-1), (1,0), (-1,0)]:
                toExplore += [[i,j,d[0], d[1]]]
            break

def bfs(fromX, fromY, deltaX, deltaY):
    nextX = fromX + deltaX
    nextY = fromY + deltaY
    if nextX < 0 or nextX >= len(Lines[0]) \
        or nextY < 0 or nextY >= len(Lines):
        return False
    nextSymbol = Lines[nextX][nextY]
    if nextSymbol in directions[str(deltaX) + "_" + str(deltaY)]:
        return True
    return False
    
def hasValidDuplicate(nums):
    numList = list(map(lambda x: [x[0] + x[2], x[1]+x[3]], nums))
    validList = []
    # print("nums ->", nums)
    for num in numList:
        crypt = str(num[0]) + "_" + str(num[1])
        if num[0] < 0 or num[0] >= len(Lines[0]) \
            or num[1] < 0 or num[1] >= len(Lines):
            continue
        if Lines[num[0]][num[1]] not in ["X", ".", "S"]:
            if crypt not in validList:
                validList += [crypt]
            else:
                return True
    return False

steps = 0
next_explore = []
while len(toExplore) > 0:
    x,y,deltaX,deltaY = toExplore.pop(0)
    symbol = Lines[x][y]
    if bfs(x,y,deltaX,deltaY):
        Lines[x][y] = "X"
        nextSymbol = Lines[x+deltaX][y+deltaY]
        for direction in symbolToDirection[nextSymbol]:
            next_explore += [[x+deltaX, y+deltaY, direction[0], direction[1]]]

    if len(toExplore) == 0:
        # check is end
        steps += 1
        if hasValidDuplicate(next_explore):
            steps += 1
            break
        toExplore = next_explore
        next_explore = []

print(steps)
