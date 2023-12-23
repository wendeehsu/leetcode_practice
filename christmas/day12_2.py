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
                if isValid(tail, ans):
                    localResult += ["."+tail]
            elif len(tmpTail) < len(ans):
                tofulfill = ans[:len(ans)-len(tmpTail)]
                neededSpace = sum(tofulfill) + len(ans)-len(tmpTail)-1
                if (1+startIndex) > neededSpace:
                    tofulfillString = data[:startIndex+1]
                    if tofulfillString.count("#") + tofulfillString.count("?") > sum(tofulfill):
                        localResult += ["."+tail, "#"+tail]
                        # remain_blocks = ''.join(tofulfillString).replace(".", " ").split()
                    #     if len(remain_blocks) > len(tofulfill):
                    #         localResult += ["."+tail, "#"+tail]
                    #     else:
                    #         if len(remain_blocks[-1]) > tofulfill[-1]:
                    #             localResult += ["."+tail, "#"+tail]
                    #         else:
                    #             localResult += ["#"+tail]
                    elif tofulfillString.count("#") + tofulfillString.count("?") == sum(tofulfill):
                        localResult += ["#"+tail]
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

def updateRow(row):
    row = row.replace("\n","")
    data, ans = row.split()
    ans = list(map(lambda x: int(x), ans.split(",")))
    ori_data = data
    ori_ans = ans.copy()
    # for i in range(4):
    #     data += "?" + ori_data
    #     ans += ori_ans
    return data, ans

count = 0
for i,row in enumerate(Lines):
    data, ans = updateRow(row)
    # print(data, ans)
    for possible in getAllPos(0,list(data), ans):
        if isValid(possible, ans):
            # print(possible)
            count += 1
        else:
            print(possible, "->", isValid(possible, ans))
    print(i, count)

print("ans ->", count)