s = "{[}]"

def check(s):
    if len(s) < 2:
        return False

    if len(s) % 2 != 0:
        return False

    stack = []
    dic = {"(":0,"[":0,"{":0}
    for i in range(len(s)):
        if s[i] in ["(","[","{"]:
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if s[i] == ")" and last == "(":
                continue
            elif s[i] == "]" and last == "[":
                continue
            elif s[i] == "}" and last == "{":
                continue
            else:
                return False

    return len(stack) == 0
    
print(check(s))