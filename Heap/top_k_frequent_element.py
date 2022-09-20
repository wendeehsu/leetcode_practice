nums = [1,1,1,2,2,3]
k = 2

sortedList = {}
def updateList(letter):
    if letter in sortedList:
        sortedList[letter] += 1
    else:
        sortedList[letter] = 1

for i in nums:
    updateList(i)

sortedList = sorted(sortedList.items(), key=lambda item: item[1], reverse=1)
finalList = []
for i in range(k):
    if i < len(sortedList):
        finalList += [sortedList[i][0]]

print(finalList)