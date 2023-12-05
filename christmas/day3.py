# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
def isSymbol(symbol):
    return symbol.isnumeric() == False and symbol != "."

for i, line in enumerate(Lines):
    line = line.replace("\n","")
    num = 0
    canCount = False
    for j in range(len(line)):
        if line[j].isnumeric():
            num *= 10
            num += int(line[j])
            if i - 1 > 0: # up
                if isSymbol(Lines[i-1][j]):
                    canCount = True
                if j > 0 and isSymbol(Lines[i-1][j-1]): # up left
                    canCount = True
                if j < len(line)-1 and isSymbol(Lines[i-1][j+1]): # up right
                    canCount = True
            if i + 1 < len(Lines): # down
                if isSymbol(Lines[i+1][j]):
                    canCount = True
                if j > 0 and isSymbol(Lines[i+1][j-1]): # down left
                    canCount = True
                if j < len(line)-1 and isSymbol(Lines[i+1][j+1]): # down right
                    canCount = True
            if j > 0 and isSymbol(line[j-1]):
                canCount = True
            if j < len(line)-1 and isSymbol(line[j+1]):
                canCount = True
        else:
            if canCount:
                count += num
                print("add", num)
            num = 0
            canCount = False
        
        if j == len(line) -1 :
            if canCount:
                count += num
                print("add edd", num)
            num = 0
            canCount = False

print("count ->", count)