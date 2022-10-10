s = "anagram"
t = "nagaram"

def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    
    if len(set(s)) != len(set(t)):
        return False
    
    
    for i in list(set(s)):
        if s.count(i) != t.count(i):
            return False
    return True

print(isAnagram(s,t))