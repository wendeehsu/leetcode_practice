coins = [186,419,83,408]
amount = 6249

coins.sort()
print(coins)

maxAmount = [0] * len(coins)
for index, coin in enumerate(coins):
    maxAmount[index] = amount // coin

print(maxAmount)

def amountLeft(coinIndex, currentAmount):
    tmpAmount = currentAmount // coins[coinIndex]
    tmpAmount = min(tmpAmount, maxAmount[coinIndex])
    return tmpAmount, currentAmount - tmpAmount * coins[coinIndex]

while True:
    left = amount
    ttlNumCoins = 0
    paneltyIndex = len(coins) - 1
    for i in range(len(coins)-1,-1,-1):
        numCoins, left = amountLeft(i, left)
        ttlNumCoins += numCoins
        if left == 0:
            break
    
    if left == 0:
        print("ttlNumCoins ->",ttlNumCoins)
        break 
    else:
        if paneltyIndex == 0:
            # no answer
            print(-1)
            break
        elif maxAmount[paneltyIndex] == 0:
            paneltyIndex -= 1
        else:
            maxAmount[paneltyIndex] -= 1
# print(maxAmount)
