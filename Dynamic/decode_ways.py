s = "01"

def decode(s):    
    if s[0] == "0":
        return 0
    
    dp = [0] * (1+len(s))
    dp[0] = dp[1] = 1
    
    for i in range(2,len(s)+1):
        # current letter: s[i-1]
        if s[i-1] != "0":
            dp[i] = dp[i-1]
        
        if int(s[i-2:i]) <= 26 and s[i-2] != "0":
            dp[i] += dp[i-2]

    return dp[-1]

print(decode(s))