file1 = open('input.txt', 'r')
Lines = file1.readlines()
maxCube = {"red": 12, "green": 13, "blue": 14}

count = 0
for line in Lines:
    line = line.replace("\n","")
    line = line.replace(",","")
    raw = line.split(":")
    gameId = int(raw[0].split()[1])
    sets = raw[1].split(";")
    possible = True
    for data in sets:
        data = data.split()
        for i in range(1,len(data),2):
            if int(data[i-1]) > maxCube[data[i]]:
                possible = False
                break
        if possible == False:
            break
    if possible:
        print("yes", gameId, sets)
        count += gameId

print("count ->", count)