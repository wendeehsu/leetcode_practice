# https://adventofcode.com/2023/day/3/input
# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0

def getNumber(index, line):
    # print("start index = ", index)
    while index > 0 and line[index-1].isnumeric():
        index -= 1
    # print("num start index = ", index)
    num = 0
    while line[index].isnumeric():
        num *= 10
        num += int(line[index])
        index += 1
        if index == len(line):
            break
    # print(index, "get", num, "fron", line)
    return num

def updateNumber(num1, newNum):
    if num1 == None:
        return newNum, None
    if num1 == newNum:
        return num1, None
    return num1, newNum

for i, line in enumerate(Lines):
    line = line.replace("\n","")
    for j in range(len(line)):
        if line[j] == "*":
            num1 = None
            num2 = None
            print(i, "j =", j)
            if i - 1 >= 0: # up
                if j < len(line)-1 and Lines[i-1][j+1].isnumeric(): # up right
                    tmp = getNumber(j+1, Lines[i-1])
                    num1, num2 = updateNumber(num1, tmp)
                elif Lines[i-1][j].isnumeric():
                    tmp = getNumber(j, Lines[i-1])
                    num1, num2 = updateNumber(num1, tmp)
                    
                elif j > 0 and Lines[i-1][j-1].isnumeric():
                    tmp = getNumber(j-1, Lines[i-1])
                    num1, num2 = updateNumber(num1, tmp)
                    
            if i + 1 < len(Lines): # down
                if j < len(line)-1 and Lines[i+1][j+1].isnumeric(): # up right
                    tmp = getNumber(j+1, Lines[i+1])
                    num1, num2 = updateNumber(num1, tmp)
                    
                elif Lines[i+1][j].isnumeric():
                    tmp = getNumber(j,Lines[i+1])
                    num1, num2 = updateNumber(num1, tmp)
                    
                elif j > 0 and Lines[i+1][j-1].isnumeric():
                    tmp = getNumber(j-1, Lines[i+1])
                    num1, num2 = updateNumber(num1, tmp)
                    
            if j > 0 and line[j-1].isnumeric():
                tmp = getNumber(j-1,line)
                num1, num2 = updateNumber(num1, tmp)
            if j < len(line)-1 and line[j+1].isnumeric():
                tmp = getNumber(j+1,line)
                num1, num2 = updateNumber(num1, tmp)
            if num1 != None and num2 != None:
                print(count, "->", num1, num2)
                count += num1* num2
                # print(count)
            if num1 == None or num2 == None:
                print("empty------",i,j)
            # print(count)
            # if i > 5:
            #     break
        

print("count ->", count)