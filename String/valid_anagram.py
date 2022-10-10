s = "anagram"
t = "nagaram"

def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    
    if len(set(s)) != len(set(t)):
        return False
    
    dicS = {}
    for i in list(set(s)):
        dicS[i] = s.count(i)

    for i in dicS:
        if dicS[i] != t.count(i):
            return False
        
    return True

print(isAnagram(s,t))