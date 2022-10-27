import re
s = "A man, a plan, a canal: Panama"

def isValid(s):
    s = re.sub(r'[^a-z0-9]', '', s)
    startIndex = 0
    endIndex = len(s) - 1
    while startIndex < endIndex:
        if s[startIndex] != s[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
    return True


print(isValid(s))