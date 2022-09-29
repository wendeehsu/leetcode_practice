text1 = "wendee"
text2 = "edw"

start2 = len(text2)
dp = [0] * (len(text1) + 1)

for i in range(len(text1)-1,-1,-1):
    # print(i,text1[i])
    hasFound = False
    for j in range(len(text2),-1,-1):
        if text1[i] == text2[j]:              
            start2 = j
            dp[i] = dp[i+1] + 1
            hasFound = True
            break
    if hasFound == False:
        dp[i] = dp[i+1]

print(dp)
print("result ->", dp[0])