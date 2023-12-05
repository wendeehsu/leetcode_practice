# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
text2Num = {"one": 1, "two": 2, "three": 3, \
            "four": 4, "five": 5, "six": 6, \
            "seven": 7, "eight": 8, "nine": 9}
startMap = {"o": ['one'], \
            "t": ["two", "three"], \
            "f": ["four", 'five'], \
            "s": ["six", "seven"], \
            "e": ["eight"], \
            "n": ["nine"]}
endMap = {"e": ["one", "three", "five", "nine"], \
            "o": ['two'], \
            "r": ["four"], \
            "x": ["six"], \
            "t": ["eight"], \
            "n": ["seven"]}

count = 0
# Strips the newline character
for line in Lines:
    num = 0
    left = 0
    right = len(line) - 1

    while True:
        if line[left].isnumeric() == True:
            num += 10 * int(line[left])
            break
        
        added = False
        if line[left] in startMap:
            for number in startMap[line[left]]:
                if left + len(number) <= len(line) and \
                    number == line[left:left + len(number)]:
                    num += 10 * text2Num[number]
                    added = True
                    break
        if added:
            break
        left += 1
    
    while True:
        if line[right].isnumeric() == True:
            num += int(line[right])
            break
        
        added = False
        if line[right] in endMap:
            for number in endMap[line[right]]:
                if right + 1 - len(number) >= 0 and \
                    number == line[right + 1 - len(number): right+1]:
                    num += text2Num[number]
                    added = True
                    break
        if added:
            break
        right -= 1
    print(num, line)
    
    # right = len(line) - 1
    # while line[right].isnumeric() == False:
    #     right -= 1
    # num += int(line[right])
    count += num
    # print(num, line)
print("-->", count)