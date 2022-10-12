# s = "bb"
# wordDict = ["a","b","bbb","bbbb"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
s = "ccbb"
wordDict = ["bc","cb"]

def splitSubstring(s):
    global wordDict
    wordDict += ['']
    for i in range(len(s)):
        for word in wordDict:
            if i+1 >= len(word):
                if s[:len(word)] ==  word and s[len(word):i+1] in wordDict:
                    if s[:i+1] not in wordDict:
                        wordDict += [s[:i+1]]
    return s in wordDict

def getUnique(word):
    uniqueWords = list(set(''.join(word)))
    uniqueWords.sort()
    return uniqueWords

myWords = getUnique(list(set(s)))
dicWords = getUnique(wordDict)
contains = True
for i in myWords:
    if i not in dicWords:
        contains = False
        print(contains)
        break
if contains:
    print(splitSubstring(s))
    print(wordDict)