coins = [186,419,83,408]
amount = 6249

coins.sort()
print(coins)

"""
idea:
- create a list dp:
  - number at index 0 = the min number of coins needed for amount 0
  - number at index n = the min number of coins needed for amount n
"""