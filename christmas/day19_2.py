file1 = open('input.txt', 'r')
Lines = file1.readlines()

initRule = True
rules = {}

for line in Lines:
    line = line.replace("\n", "")
    line = line.replace("}","")
    if line == "":
        initRule = False
        # print(rules)
        break
    
    if initRule:
        # set up rules
        line = line.split("{")
        key = line[0]
        tmpData = []
        for r in line[1].split(","):
            if ":" in r:
                r, nextKey = r.split(":")
                tmpData += [[r[0],{"sign": r[1], "num": int(r[2:]), "next": nextKey}]]
            else:
                tmpData += [["-", {"next": r}]]
        rules[key] = tmpData

possiblePaths = []
wipPaths = []
for r in rules["in"]:
    wipPaths += [[["in", r[0], r[1]]]]

while len(wipPaths) > 0:
    path = wipPaths.pop(0)
    lastStop = path[-1][2]["next"]
    for r in rules[lastStop]:
        if r[1]["next"] == "A":
            possiblePaths += [ path + [[lastStop, r[0], r[1]]] ]
        elif r[1]["next"] == "R":
            continue
        else:
            wipPaths += [ path + [[lastStop, r[0], r[1]]] ]

def updateRange(oriRange, sign, num, reverse = False):
    if reverse:
        if sign == ">":
            sign = "<"
            num += 1
        else:
            sign = ">"
            num -= 1

    if sign == "<":
        if oriRange["low"] > num:
            return None
        else:
            oriRange["up"] = min(oriRange["up"], num-1)
    else:
        if oriRange["up"] < num:
            return None
        else:
            oriRange["low"] = max(oriRange["low"], num+1)
    return oriRange

print("possiblePaths:", len(possiblePaths))

combinations = []
for path in possiblePaths:
    data = {}
    canCount = True
    for i in "xmas":
        data[i] = {"up": 4000, "low": 1}
    for step in path:
        pathId = step[0]
        symbol = step[1]
        rule = step[2]

        for subRule in rules[pathId][:len(rules[pathId])-1]:
            if symbol != "-" and \
             symbol+subRule[1]["sign"]+str(subRule[1]["num"]) == symbol+rule["sign"]+str(rule["num"]):
                # print("need to follow", symbol, rule)
                tmpRange = updateRange(data[symbol], rule["sign"], rule["num"])
                if tmpRange == None:
                    canCount = False
                else:
                    data[symbol] = tmpRange
                break
            else:
                # print("need NOTT to follow", symbol, subRule)
                tmpRange = updateRange(data[subRule[0]], subRule[1]["sign"], subRule[1]["num"], True)

                if tmpRange == None:
                    canCount = False
                    break
                else:
                    data[subRule[0]] = tmpRange
        
        if canCount == False:
            break

    if canCount == True:
        # print("successsssssss")
        # print(path)
        # print(data)
        combinations += [data]

ans = 0
for combi in combinations:
    tmp = 1
    for symbol in "xmas":
        tmp *= (combi[symbol]["up"] - combi[symbol]["low"] + 1)
    ans += tmp
    
print("ans", ans)