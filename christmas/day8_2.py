file1 = open('input.txt', 'r')
Lines = file1.readlines()
direction = Lines[0].replace("\n", "")
maps = {}
startPos = set()
for i in range(2,len(Lines)):
    line = Lines[i]
    loc = line[:3]
    maps[loc] = {"L": line[7:10], "R": line[12:15]}
    if loc[2] == 'A':
        startPos.add(loc)
startPos = list(startPos)

print(startPos)
count = 1
step = 0
while True:
    canStop = False
    for i, loc in enumerate(startPos):
        nextPos = maps[loc][direction[step]]
        print(loc, "->", nextPos)
        if nextPos[2] == 'Z':
            print(nextPos)
            canStop = True
        startPos[i] = nextPos
    print(count, direction[step], startPos)
    if canStop:
        break
       
    step += 1
    count += 1
    if step == len(direction):
        step = 0

print("count -> ", count)
print(startPos)