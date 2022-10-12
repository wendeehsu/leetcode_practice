# s = "applepenapple"
# wordDict = ["apple","pen"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

def splitSubstring(s):
    for i in range(len(s)):
        for word in wordDict:
            if word == s[:i+1]:
                # print(word, s[:i+1], s[i+1:])
                if s[i+1:] == '':
                    return True
                if splitSubstring(s[i+1:]):
                    return True
    return False

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