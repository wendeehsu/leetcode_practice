from typing import List

def printG(grid: List[List[int]]):
    for i in grid:
        print(i)

def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    row_num = len(grid1)
    col_num = len(grid1[0])

    # traverse all lands in grid1 and mark grid2 in the same time
    candidates = []
    
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j] == 1 and grid2[i][j] == 1:
                grid2[i][j] = 2
                candidates += [[i,j]]
    
    # traverse all lands in grid2, only take those that are all marked
    subCount = 0

    for pos in candidates:
        
        # is head?
        if grid2[pos[0]][pos[1]] == 0:
            continue

        to_explore = [pos]
        isSub = True
        while len(to_explore) > 0:
            location = to_explore.pop(0)
            grid2[location[0]][location[1]] = 0

            for direction in directions:
                x = location[0] + direction[0]
                y = location[1] + direction[1]

                if x >= 0 and x < row_num \
                    and y >= 0 and y < col_num:
                    if grid2[x][y] == 1:
                        isSub = False
                        to_explore += [[x,y]]
                    elif grid2[x][y] == 2:
                        to_explore += [[x,y]]
                    grid2[x][y] = 0
        
        if isSub:
            subCount += 1
    return subCount
           
# grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(countSubIslands(grid1, grid2))