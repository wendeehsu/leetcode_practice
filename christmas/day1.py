# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    num = 0
    left = 0

    while line[left].isnumeric() == False:
        left += 1
    num += int(line[left])*10
    right = len(line) - 1
    while line[right].isnumeric() == False:
        right -= 1
    num += int(line[right])
    count += num
    # print(num, line)
print(count)