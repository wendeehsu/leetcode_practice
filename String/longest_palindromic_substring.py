s = "aacabdkacaa"

def getPalin(s):
    def isPalin(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    startIndex = 0
    longestStr = ""
    while startIndex < len(s) and len(s)-startIndex > len(longestStr):
        for i in range(len(s)-1, startIndex, -1):
            if s[startIndex] == s[i]:
                # print(startIndex, i, s[startIndex: i+1])
                # check is palin
                if isPalin(s, startIndex, i) and (i-startIndex+1 > len(longestStr)):
                    longestStr = s[startIndex: i+1]
                    break

        startIndex += 1
    
    if longestStr == "":
        return s[0]
    return longestStr

print("s ->", s)
print(getPalin(s))