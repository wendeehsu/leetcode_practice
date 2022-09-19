s = "WENDEE"
k = 4

startIndex = 0
maxLetterCount = 0
letterCount = {}
result = 0

def updateLetterCount(letter, num):
    if letter in letterCount:
        letterCount[letter] += num
    else:
        letterCount[letter] = num
    
for index, letter in enumerate(s):
    updateLetterCount(letter,1)
    maxLetterCount = max(maxLetterCount, letterCount[letter])

    while (index - startIndex + 1 - maxLetterCount) > k:
        updateLetterCount(s[startIndex],-1)
        startIndex += 1
        maxLetterCount = 0
        for i in letterCount:
            maxLetterCount = max(maxLetterCount, letterCount[i])
    result = max(result, index-startIndex+1)

print(result)