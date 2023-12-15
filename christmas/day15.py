file1 = open('input.txt', 'r')
Lines = file1.readlines()

lists = Lines[0].replace("\n","").split(",")
current_val = 0
ans = 0

def hash(char):
    val = current_val
    # print(char, "->", ord(char))
    val += ord(char)
    val *= 17
    val %= 256
    return val

for data in lists:
    current_val = 0
    for i in data:
        current_val = hash(i)
    ans += current_val

print("ans =", ans)