file1 = open('input.txt', 'r')
Lines = file1.readlines()
from collections import OrderedDict

initRule = True
rules = {}
ans = 0

for line in Lines:
    line = line.replace("\n", "")
    line = line.replace("}","")
    if line == "":
        initRule = False
        print(rules)
        continue
    
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
    else:
        # start map
        line = line.replace("{","").split(",")
        print("line", line)
        data = {}
        tmpSum = 0
        for section in line:
            data[section[0]] = int(section[2:])
            tmpSum += int(section[2:])
        
        keyPos = "in"
        while True:
            for keyValue in rules[keyPos]:
                key = keyValue[0]
                value = keyValue[1]
                if key == "-":
                    keyPos = value["next"]
                    break
                
                if key in data:
                    if value["sign"] == ">":
                        print(">", data[key],value, data[key] < value["num"])
                        if data[key] > value["num"]:
                            keyPos = value["next"]
                            break
                    else:
                        print("<", data[key],value, data[key] < value["num"])
                        if data[key] < value["num"]:
                            keyPos = value["next"]
                            break
            if keyPos == "R":
                print("Reject")
                break
            if keyPos == "A":
                ans += tmpSum
                print("Accepted! add", tmpSum)
                if (tmpSum == 3580): 
                    print("------------------------------")
                break

            print("->", keyPos)

        print("========")

print("ans ->", ans)