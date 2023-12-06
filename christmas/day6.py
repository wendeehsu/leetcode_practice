# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()

time = list(map(lambda x: int(x),Lines[0].split()[1:]))
distance = list(map(lambda x: int(x),Lines[1].split()[1:]))
ans = None

for i in range(len(time)):
    count = 0
    for v in range(1,time[i]):
        if v * (time[i]-v) >= distance[i]:
            count += 1
            print(v, time[i]-v, v * (time[i]-v), distance[i])
    if ans == None:
        ans = count
    else:
        ans *= count
    print(count, ans)


print(ans)