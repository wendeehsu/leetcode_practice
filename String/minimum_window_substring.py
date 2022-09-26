s = "ADOBECODEBANC"
t = "ABC"

minStr = ""
letterNeeded = {}
for letter in t:
    if letter not in letterNeeded:
        letterNeeded[letter] = 1
    else:
        letterNeeded[letter] += 1

def getMinStr():
    for windowSize in range(len(t),len(s)+1):
        # print("winSize", windowSize)
        for startIndex in range(len(s)-windowSize+1):
            # print("winSize", windowSize, "startIndex", startIndex)
            if startIndex + windowSize <= len(s):
                substr = s[startIndex:(startIndex+windowSize)]
                # print(substr)
                qualified = True
                for letter in letterNeeded:
                    if substr.count(letter) < letterNeeded[letter]:
                        qualified = False
                        break
                
                if qualified:
                    return substr
    return ""

print(getMinStr())
