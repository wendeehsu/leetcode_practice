from collections import OrderedDict

file1 = open('input.txt', 'r')
Lines = file1.readlines()

lists = Lines[0].replace("\n","").split(",")
boxs = {}

# init boxs
for i in range(256):
    boxs[i] = OrderedDict()

def hash(char,val):
    val += ord(char)
    val *= 17
    val %= 256
    print(char, " hash", val)
    return val

for data in lists:
    box_id = 0
    symbol_index = -1
    for index,i in enumerate(data):
        if i == "-" or i == "=":
            symbol_index = index
            break
        box_id = hash(i, box_id)
    
    label = data[:symbol_index]
    print(data, "label", label, box_id)
    if data[symbol_index] == "=":
        boxs[box_id][label] = int(data[symbol_index+1:])
    else:
        if label in boxs[box_id]:
            boxs[box_id].pop(label)

ans = 0
for i in range(256):
    index = 1
    for key, value in boxs[i].items():
        ans += (i+1)* index * value
        index += 1

print("ans =", ans)