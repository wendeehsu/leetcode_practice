file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    line = line.replace("\n","")
    line = line.replace(",","")
    raw = line.split(":")
    gameId = int(raw[0].split()[1])
    sets = raw[1].split(";")
    maxCube = {"red": 0, "green": 0, "blue": 0}
    for data in sets:
        data = data.split()
        for i in range(1,len(data),2):
            maxCube[data[i]] = max(int(data[i-1]), maxCube[data[i]])
        
    num = 1
    for i in maxCube:
        num *= maxCube[i]
    count += num
    print(gameId, num, maxCube)

print("count ->", count)