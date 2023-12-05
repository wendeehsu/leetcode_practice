# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
counts = [1] * len(Lines)
for index, line in enumerate(Lines):
    print(line)
    line = line.split(":")[1]
    data = line.split()
    # print(data)
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
                num += 1
    for i in range(index+1, index+num+1):
        counts[i] += counts[index]
    print(index, "match ->", num)
    print("count ->", counts)
    # if index > 5:
    #     break

print("final ->", counts)
print("sum of final ->", sum(counts))
