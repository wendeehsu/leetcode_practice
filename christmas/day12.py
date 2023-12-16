file1 = open('input.txt', 'r')
Lines = file1.readlines()

def getAllPos(startIndex, data, ans):
    symbol = data[startIndex]
    if len(data) == startIndex+1:
        if symbol == "?":
            return [".", "#"]
        return [symbol]
    localtails = getAllPos(startIndex+1, data, ans)
    localResult = []
    for tail in localtails:
        if symbol != "?":
            localResult += [symbol+tail]
            continue
        tmpTail = tail.replace(".", " ").split()
        if tail[0] == "#": # determine should continue or end
            if len(tmpTail[0]) < ans[len(ans)-len(tmpTail)]:
                localResult += ["#"+tail]
            elif len(tmpTail[0]) == ans[len(ans)-len(tmpTail)]:
                localResult += ["."+tail]
        else:
            if len(tmpTail) == len(ans):
                localResult += ["."+tail]
            elif len(tmpTail) < len(ans):
                tofulfill = ans[:len(ans)-len(tmpTail)]
                neededSpace = sum(tofulfill) + len(ans)-len(tmpTail)-1
                if (1+startIndex) > neededSpace:
                    localResult += ["."+tail, "#"+tail]
                elif (1+startIndex) == neededSpace:
                    localResult += ["#"+tail]
    return localResult

def isValid(data,ans):
    data = data.replace("."," ").split()
    if len(ans) != len(data):
        return False
    for i in range(len(ans)):
        if len(data[i]) != ans[i]:
            return False
    return True

count = 0
for row in Lines:
    row = row.replace("\n","")
    data, ans = row.split()
    ans = list(map(lambda x: int(x), ans.split(",")))
    for possible in getAllPos(0,list(data), ans):
        if isValid(possible, ans):
            print(possible)
            count += 1
        # print(possible, "->", isValid(possible, ans))

print("ans ->", count)