s = "WENDEE"
k = 2

startIndex = 0
maxLetterCount = 0
letterCount = {}
result = 0

def updateLetterCount(letter, num):
    if letter in letterCount:
        letterCount[letter] += num
    else:
        letterCount[letter] = num
    print(letter,num, letterCount[letter])
    
for index, letter in enumerate(s):
    updateLetterCount(letter,1)
    maxLetterCount = max(maxLetterCount, letterCount[letter])

    while (index - startIndex + 1 - maxLetterCount) > k:
        updateLetterCount(s[startIndex],-1)
        startIndex += 1
        maxLetterCount = max(letterCount.values())
    result = max(result, index-startIndex+1)

print(result)