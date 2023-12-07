file1 = open('input.txt', 'r')
Lines = file1.readlines()
points = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
toNum = {}
for i, d in enumerate(points):
    toNum[d] = len(points)-i
toNum['J'] = 0

def toNumList(raw):
    nums = []
    for i in raw:
        nums += [toNum[i]]
    print(raw, "->", nums)
    return nums

def getType(nums):
    nums = nums.copy()
    jNum = nums.count(0)
    if jNum > 0 and jNum < 5:
        maxChar = -1
        maxCount = -1
        for i in nums:
            if i != 0:
                localCount = nums.count(i)
                if localCount > maxCount:
                    maxCount = localCount
                    maxChar = i

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = maxChar

    char = list(set(nums))
    
    if len(char) == 1:
        return 7
    elif len(char) == 2:
        if nums.count(char[0]) == 1 or nums.count(char[0]) == 4:
            return 6
        return 5
    elif len(char) == 3:
        if nums.count(char[0]) == 3 or \
            nums.count(char[1]) == 3 or \
            nums.count(char[2]) == 3:
            return 4
        return 3
    elif len(char) == 4:
        return 2
    return 1        

finalData = []
for line in Lines:
    raw, bid = line.split()
    nums = toNumList(raw)
    finalData += [[getType(nums), nums, int(bid), raw]]
finalData.sort(key=lambda x: (x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4]))
# print(finalData)

count = 0
for i, data in enumerate(finalData):
    count += (i+1) * data[2]
    print(i+1, data, count)
print("count->", count)