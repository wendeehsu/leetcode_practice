nums = [1,2,3,1]

hashTable = {}
for i in nums:
    if i in hashTable:
        print(True)
        break
    else:
        hashTable[i] = 1
