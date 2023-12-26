file1 = open('input.txt', 'r')
Lines = file1.readlines()

import numpy as np

pos = [0,0]
xs = [pos[0]]
ys = [pos[1]]
dMap = {"R": (0,1), "L": (0,-1), "U": (-1,0), "D":(1,0)}
c = 0
def updatePath(direction, step):
    global pos, xs, ys
    x,y = pos
    # print(direction, step)
    steps = step
    x += dMap[direction][0] * steps
    y += dMap[direction][1] * steps
    xs += [x]
    ys += [y]
    pos[0] = x
    pos[1] = y

for line in Lines:
    # print(line)
    direction, step, color = line.split()
    updatePath(direction, int(step))
    c += int(step)
    # print(xs)
    # print(ys)
    # print("----")

xs = np.array(xs)
ys = np.array(ys)
i=np.arange(len(xs))

print(xs)
print(ys)
print("area ->", np.abs(np.sum(xs[i-1]*ys[i]-xs[i]*ys[i-1])*0.5))
print(c)