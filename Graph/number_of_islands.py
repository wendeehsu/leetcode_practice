from collections import deque

grid = [\
  ["1","1","0","0","0"],\
  ["1","1","0","0","0"],\
  ["0","1","1","0","0"],\
  ["0","0","1","1","1"]\
]

def printGrid(g):
    for i in g:
        print(i)

def explore(x,y):
    island = deque([[x,y]])
    while len(island) > 0:
        start = island.popleft()
        grid[start[0]][start[1]] = '#'
        for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x = start[0] + direction[0]
            new_y = start[1] + direction[1]

            if new_x < 0 or new_x >= len(grid):
                continue

            if new_y < 0 or new_y >= len(grid[0]):
                continue
            
            if grid[new_x][new_y] == '1':
                grid[new_x][new_y] = '#'
                island.append([new_x,new_y])
        
numIsland = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1':
            numIsland += 1
            explore(i,j)
            # printGrid(grid)
            # print('-----------')
    

print("island ->", numIsland)