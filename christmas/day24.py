file1 = open('input.txt', 'r')
Lines = file1.readlines()
ps = {}
bs = {}
vs = {}

for index, line in enumerate(Lines):
    line = line.replace("\n","").replace("@",",").replace(" ", "")
    data = list(map(lambda x: int(x), line.split(",")))
    ps[index] = {"x": data[0], "y": data[1], "z": data[2]}
    vs[index] = {"x": data[3], "y": data[4], "z": data[5]}
    bs[index] = vs[index]["x"] * ps[index]["y"] - vs[index]["y"] * ps[index]["x"]

import numpy as np
testBound = [200000000000000,400000000000000]
count = 0

def isPast(ansY, index):
    if ansY > ps[index]["y"] and vs[index]["y"] < 0:
        return True
    if ansY < ps[index]["y"] and vs[index]["y"] > 0:
        return True
    return False

for i in range(len(Lines)):
    for j in range(i+1, len(Lines)):
        if vs[i]["x"] * vs[j]["y"] == vs[j]["x"] * vs[i]["y"]:
            print(i,j,"--> paralal")
            continue

        a = np.array([[vs[i]["x"], -1 * vs[i]["y"]], [vs[j]["x"], -1 * vs[j]["y"]]])
        b = np.array([bs[i], bs[j]])
        ansY, ansX = np.linalg.solve(a,b)
        print(i,j,"->",ansX, ansY)
        if ansX < testBound[0] or ansY < testBound[0] or \
            ansX > testBound[1] or ansY > testBound[1]:
            print("out of range")
            continue
        
        if isPast(ansY, i) or isPast(ansY, j):
            print("past")
            continue
        
        count += 1
        print("success")
        
        # print("p", ps[i], "-- v", vs[i], "-- b", bs[i])
print("count ->", count)