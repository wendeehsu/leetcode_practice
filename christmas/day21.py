file1 = open('input.txt', 'r')
Lines = file1.readlines()

# init map
garden = []
locations = []
for i, line in enumerate(Lines):
    line = line.replace("\n", "")
    if "S" in line:
        locations += [str(i) + " " + str(line.index("S"))]
        line = line.replace("S",".")
    garden += [line]

def bfs(pos):
    x = int(pos[0])
    y = int(pos[1])
    nextPos = []
    for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
        newX = x + direction[0]
        newY = y + direction[1]
        
        if newX < 0 or newX >= len(garden) or \
            newY < 0 or newY >= len(garden[0]):
            continue
        if garden[newX][newY] == ".":
            nextPos += [str(newX) +" "+ str(newY)]
    return nextPos

for step in range(64):
    nextPos = []
    while len(locations) > 0:
        pos = locations.pop(0).split()
        nextPos += bfs(pos)
    locations = list(set(nextPos))
    # print(locations)    
    print(step+1, "->", len(locations))
    
print("ans ->", len(locations), locations)