# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0

for line in Lines:
    print(line)
    line = line.split(":")[1]
    data = line.split()
    print(data)
    win = set()
    num = 0
    starCounting = False
    for i in data:
        if starCounting == False:
            if i == '|':
                starCounting = True
            else:
                win.add(i)
        else:
            if i in win:
                # print(i)
                num += 1
    print("match ->", num)
    if num > 0:
        count += 2**(num-1)
    print("count ->", count)

print("final ->", count)
