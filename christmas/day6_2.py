# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()

time = int(''.join(Lines[0].split()[1:]))
distance = int(''.join(Lines[1].split()[1:]))
left = 1
right = time-1

while True:
    v = left
    if v*(time-v) < distance:
        left += 1
    else:
        break
while True:
    v = right
    if v*(time-v) < distance:
        right -= 1
    else:
        break
print(left, time-left,left*(time-left), distance)
print(right, time-right,right*(time-right), distance)

print(right-left+1)