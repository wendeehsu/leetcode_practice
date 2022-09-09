prices = [7,6,4, 100,1000]

largestPrice = prices[-1]
maxProfit = 0
for i in range(len(prices)-1,-1,-1):
    largestPrice = max(largestPrice,prices[i])
    maxProfit = max(maxProfit, largestPrice-prices[i])

print(maxProfit)
