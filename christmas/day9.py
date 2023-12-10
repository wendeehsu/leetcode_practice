file1 = open('input.txt', 'r')
Lines = file1.readlines()

def predict(nums):
    diff = list(map(lambda i: nums[i]-nums[i-1],list(range(1,len(nums)))))
    if len(set(diff)) == 1:
        return nums[-1] + diff[0]
    return nums[-1] + predict(diff)

ans = 0
for i, line in enumerate(Lines):
    nums = list(map(lambda x: int(x),line.replace("\n","").split()))
    nex = predict(nums)
    ans += nex
    print(i, "->", nex, ans)

print("ans ->", ans)