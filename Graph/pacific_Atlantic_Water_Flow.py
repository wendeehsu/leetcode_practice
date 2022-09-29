from collections import deque
heights = [[1,2,3],[8,9,4],[7,6,5]]

directions = [(0,1),(1,0),(-1,0),(0,-1)]
pacific = set()
atlantic = set()

# init reachable
# row
for i in range(len(heights)):
    pacific.add((i,0))
    atlantic.add((i,len(heights[0])-1))

# column
for j in range(len(heights[0])):
    pacific.add((0,j))
    atlantic.add((len(heights)-1,j))

def bfs(ocean):
    ocean = deque(ocean)
    reachable = set()

    while len(ocean) > 0:
        node = ocean.popleft()
        reachable.add(node)
        for direction in directions:
            x = node[0] + direction[0]
            y = node[1] + direction[1]
            
            if x < 0 or x >= len(heights) \
                or y < 0 or y >= len(heights[0]):
                continue # this node is not valid
            
            if (x,y) in reachable:
                continue # prevent TLE on re-computing
            
            if heights[node[0]][node[1]] <= heights[x][y]:
                ocean.append((x,y))
                reachable.add((x,y))

    return reachable

print(list(bfs(atlantic).intersection(bfs(pacific))))