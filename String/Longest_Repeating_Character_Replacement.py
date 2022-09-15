s = "WENDEE"
k = 0

startIndex = endIndex = 0
nextIndexList = []
maxLength = 1
while endIndex != len(s):
    """
    if s[endIndex] = s[startIndex]: increase window
    else:
        case 1. k > 0: k-= 1, record this place, increase window
        case 2. move start to nextIndex, reset nextIndex and k
    """
    if s[startIndex] == s[endIndex]:
        maxLength = max(maxLength, endIndex-startIndex+1)
        endIndex += 1
    else:
        if len(nextIndexList) < k:
            nextIndexList += [endIndex]
            maxLength = max(maxLength, endIndex-startIndex+1)
            endIndex += 1
        else:
            if k > 0:
                startIndex = endIndex = nextIndexList[0]
            else:
                startIndex = endIndex
            nextIndexList = []

maxLength = max(maxLength, min(len(s),endIndex-startIndex+k-len(nextIndexList)))
print(s,k,", len=", maxLength)
