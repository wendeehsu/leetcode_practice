file1 = open('input.txt', 'r')
Lines = file1.readlines()
direction = Lines[0].replace("\n", "")
maps = {}

for i in range(2,len(Lines)):
    line = Lines[i]
    maps[line[:3]] = {"L": line[7:10], "R": line[12:15]}

count = 1
step = 0
pos = 'AAA'
while True:
    nextPos = maps[pos][direction[step]]
    if nextPos == 'ZZZ':
        break
    step += 1
    count += 1
    pos = nextPos
    if step == len(direction):
        step = 0

print("count -> ", count)