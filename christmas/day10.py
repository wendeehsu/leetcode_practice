file1 = open('input.txt', 'r')
Lines = file1.readlines()

toExplore = []
for i,line in enumerate(Lines):
    Lines[i] = list(Lines[i].replace("\n",""))
    for j, symbol in enumerate(line):
        if symbol == "S":
            toExplore = [[i,j]]
            break

def bfs(x,y):
    if 0 > x or x >= len(Lines[0]) \
        or y < 0 or y >= len(Lines):
        return None
    if Lines[x][y] == "." or Lines[x][y] == "X":
        return None
    return [x,y]

def hasDuplicate(nums):
    strList = list(map(lambda x: str(x[0])+ "-" + str(x[1]), nums))
    if len(set(strList)) != len(strList):
        return True, list(map( \
            lambda x: [int(x.split("-")[0]), int(x.split("-")[1])] \
            , list(set(strList))))
    return False, nums

ans = 0
steps = 0
next_explore = []
while len(toExplore) > 0:
    x,y = toExplore.pop(0)
    symbol = Lines[x][y]
    if symbol == "S":
        for pos in [bfs(x,y-1), bfs(x,y+1), bfs(x-1,y), bfs(x+1,y)]:
            if pos != None:
                next_explore += [pos]
    elif symbol == "|":
        for pos in [bfs(x-1,y), bfs(x+1,y)]:
            if pos != None:
                next_explore += [pos]
    elif symbol == "-":
        for pos in [bfs(x,y-1), bfs(x,y+1)]:
            if pos != None:
                next_explore += [pos]
    elif symbol == "L":
        for pos in [bfs(x-1,y), bfs(x,y+1)]:
            if pos != None:
                next_explore += [pos]
    elif symbol == "J":
        for pos in [bfs(x-1,y), bfs(x,y-1)]:
            if pos != None:
                next_explore += [pos]
    elif symbol == "7":
        for pos in [bfs(x+1,y), bfs(x,y-1)]:
            if pos != None:
                next_explore += [pos]
    elif symbol == "F":
        for pos in [bfs(x+1,y), bfs(x,y+1)]:
            if pos != None:
                next_explore += [pos]
    
    if len(toExplore) == 0:
        # check is end
        steps += 1
        isDuplicate, next_explore = hasDuplicate(next_explore)
        if isDuplicate:
            ans = steps
        print("next ->", next_explore)
        toExplore = next_explore
        next_explore = []
    Lines[x][y] = "X" 

print(ans)

# print(hasDuplicate([[1,2], [2,2]]))
# print(hasDuplicate([[1,2], [1,2]]))