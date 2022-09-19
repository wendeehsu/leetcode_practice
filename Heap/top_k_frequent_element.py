nums = [1]
k = 2

sortedList = []

def updateList(letter):
    target_index = -1
    for index, pair in enumerate(sortedList):
        if pair[0] == letter:
            pair[1] += 1
            target_index = index
            break
    """
    target_index:
    -1: create pair
    exist: pop
    -> insert pair
    """
    target_pair = [letter, 1]
    if target_index != -1:
        target_pair = sortedList.pop(target_index)
    
    insert_index = -1
    for index, pair in enumerate(sortedList):
        if pair[1] <= target_pair[1]:
            insert_index = index
            break
    if insert_index == -1:
        sortedList.append(target_pair)
    else:
        sortedList.insert(insert_index, target_pair)

for i in nums:
    updateList(i)

finalList = []
for i in range(k):
    if i < len(sortedList):
        finalList += [sortedList[i][0]]

print(finalList)