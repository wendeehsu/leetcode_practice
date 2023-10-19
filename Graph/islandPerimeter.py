from typing import List

def printG(grid: List[List[int]]):
    for i in grid:
        print(i)

def islandPerimeter(grid: List[List[int]]) -> int:
     
    # Find the first land
    p = 0
    row_num = len(grid)
    col_num = len(grid[0])
    to_explore = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                to_explore += [[i,j]]
                grid[i][j] = 3
                p = 4
                break
        if len(to_explore) > 0:
            break
    
    directions = [[0,1], [1,0], [0, -1], [-1,0]]
    printG(grid)
    while len(to_explore) > 0:
        location = to_explore.pop(0)
        # explore
        for direction in directions:
            x = location[0] + direction[0]
            y = location[1] + direction[1]
            if  x >= 0 and x < row_num and \
                y >= 0 and y < col_num:
                if grid[x][y] == 1:
                    to_explore += [[x,y]]
                    grid[x][y] = 3
                    p += 2
                elif grid[x][y] == 3:
                    p -= 2

        # mark done
        grid[location[0]][location[1]] = 2
        printG(grid)

    return p


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))