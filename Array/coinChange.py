coins = [186,419,83,408]
amount = 6

coins.sort()
maxAmount = 99999

"""
idea:
- create a list dp:
  - number at index 0 = the min number of coins needed for amount 0
  - number at index n = the min number of coins needed for amount n
"""
minAmountList = [maxAmount] * (amount+1)
minAmountList[0] = 0

for i in range(amount+1):
    for coin in coins:
        # index is in list range(0, amount+1)
        if i - coin <= amount and i - coin >= 0:
            if minAmountList[i-coin] != maxAmount:
                minAmountList[i] = min(minAmountList[i], minAmountList[i-coin]+1)

if minAmountList[amount] == maxAmount:
    print(-1)
else:
    print(minAmountList[amount])
