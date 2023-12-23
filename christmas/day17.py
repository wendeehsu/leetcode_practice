file1 = open('input.txt', 'r')
Lines = file1.readlines()

valueMap = []
minMap = []
for line in Lines:
    line = line.replace("\n","")
    valueMap += [list(map(lambda x: int(x), line))]
    minMap += [[-1]*len(line)]

dirMap = {">":(0,1),"<":(0,-1),"v":(1,0),"^":(-1,0)}
reverse = {">":"<","<":">","v":"^","^":"v"}

minMap[0][0] = 0
locations = [[0,(0,0),""]]
minLocation = None
while len(locations) > 0:
    heat, pos, path = locations.pop(0)
    for direction in "<>v^":
        if path == '>>v>>>^>>>vv>':
            print("==================", direction,"=====================")
        newX = pos[0] + dirMap[direction][0]
        newY = pos[1] + dirMap[direction][1]
        print("pos", newX, newY)
        if newX < 0 or newX >= len(valueMap) or \
            newY < 0 or newY >= len(valueMap[0]):
            print("value out")
            continue
        if path != "":
            lastDirection = path[-1]
            if direction == reverse[lastDirection]:
                print("wrong direction")
                continue
        if len(path) >= 3:
            lastThree = path[-3:]
            if len(set(lastThree)) == 1 and \
                direction == lastThree[0]:
                print("can't continue")
                continue
        tmp = [heat+valueMap[newX][newY], (newX, newY), path+direction]
        print("tmp:", tmp)
        if newX == len(valueMap)-1 and newY == len(valueMap[0])-1:
            print("minLocation", minLocation)
            if minLocation == None or tmp[0] < minLocation[0]:
                minLocation = tmp
                print("set ---->", minLocation)
            continue
        print("check minMap", minMap[newX][newY])
        if minMap[newX][newY] != -1 and minMap[newX][newY] < tmp[0]:
            print("minMap", minMap[newX][newY], tmp)
            continue

        if minLocation!= None and minLocation[0] < tmp[0]:
            continue

        # if len(path) < 3 or (len(tmp[2]) >= 3 and len(set(tmp[2][-3:])) > 1):
        minMap[newX][newY] = tmp[0]
        locations += [tmp]
        print(tmp)
        print("----")


print("min", minLocation)