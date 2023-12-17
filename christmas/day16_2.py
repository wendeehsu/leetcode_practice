file1 = open('input.txt', 'r')
Lines = file1.readlines()

dMap = {">": [0,1], "<": [0,-1], "v": [1,0], "^": [-1, 0]}
# symbol: {currentDir: [next]}
getNextDir = { \
    "." : {">": [">"], "<": ["<"], "v": ["v"], "^": ["^"]}, \
    "-" : {">": [">"], "<": ["<"], "v": ["<", ">"], "^": ["<", ">"]}, \
    "|" : {">": ["^", "v"], "<": ["^", "v"], "v": ["v"], "^": ["^"]}, \
    "\\" : {">": ["v"], "<": ["^"], "v": [">"], "^": ["<"]}, \
    "/" : {">": ["^"], "<": ["v"], "v": ["<"], "^": [">"]}}

def dfs(x,y,direction, travelMap):
    # out of range
    if x < 0 or x >= len(Lines) or \
        y < 0 or y >= len(Lines[0]):
        return None
    
    # has visited
    if direction in travelMap[x][y]:
        return None

    # not visited: mark and visit next
    symbol = Lines[x][y]
    nextPos = []
    for d in getNextDir[symbol][direction]:
        nextPos += [[x+dMap[d][0], y+dMap[d][1], d]]
    return nextPos

initPos = []
for i, line in enumerate(Lines):
    Lines[i] = line.replace("\n", "")
for i in range(len(Lines[0])):
    initPos += [[0,i,"v"]]
for i in range(len(Lines)):
    initPos += [[i, 0,">"]]
for i in range(len(Lines[0])):
    initPos += [[len(Lines)-1,i,"^"]]
for i in range(len(Lines)):
    initPos += [[i, len(Lines[0])-1,"<"]]
print(initPos)

# # init travelMap
maxCount = 0
for index,pos in enumerate(initPos):
    travelMap = []
    for i, line in enumerate(Lines):
        tmp = [""] * len(Lines[i])
        travelMap += [tmp]
    # print(travelMap)
    count = 0
    to_explore = [pos]
    while len(to_explore) > 0:
        x,y,direction = to_explore.pop(0)
        nextPos = dfs(x,y,direction, travelMap)
        if nextPos != None:
            if travelMap[x][y] == '':
                count += 1
            travelMap[x][y] += direction
            to_explore += nextPos
    print(index, "->", count, maxCount)
    maxCount = max(maxCount, count)

print("maxCount -->", maxCount)