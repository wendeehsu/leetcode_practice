# s = "bb"
# wordDict = ["a","b","bbb","bbbb"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
# s = "ccbb"
# wordDict = ["bc","cb"]

def splitSubstring(s):
    global wordDict
    dp = [False] * (1+len(s))
    dp[0] = True
    for i in range(1,1+len(s)):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[len(s)]

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