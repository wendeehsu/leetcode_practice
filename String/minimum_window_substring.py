s = "ADOBECODEBANC"
t = "ABCBECODEBANC"

letterNeeded = {}
for letter in t:
    if letter not in letterNeeded:
        letterNeeded[letter] = 1
    else:
        letterNeeded[letter] += 1

indexList = []
for index, letter in enumerate(s):
    if letter in letterNeeded:
        indexList += [(index,letter)]

def check(startIndex,endIndex,indexList):
    tmpDict = {}
    for i in range(startIndex, endIndex+1):
        if indexList[i][1] not in tmpDict:
            tmpDict[indexList[i][1]] = 1
        else:
            tmpDict[indexList[i][1]] += 1

    for letter in letterNeeded:
        if letter not in tmpDict:
            return False
        elif tmpDict[letter] < letterNeeded[letter]:
            return False
    return True

startIndex = 0
finalStr = ""
for index, i in enumerate(indexList):
    while check(startIndex,index,indexList):
        substr = s[indexList[startIndex][0]:i[0]+1]
        # print(startIndex,endIndex,substr)
        if finalStr == "":
            finalStr = substr
        elif finalStr != "" and len(substr) < len(finalStr):
            finalStr = substr
        startIndex += 1

print("finalStr",finalStr)
