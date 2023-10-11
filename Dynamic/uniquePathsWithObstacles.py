from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    # update obstacles
    # update by column
    global_obs = -1
    for i in range(len(obstacleGrid)):
        if global_obs != -1:
            for j in range(global_obs):
                obstacleGrid[i][j] = 1

        if obstacleGrid[i][0] == 1:
            # find max
            local_obs = 0
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    local_obs += 1
                else:
                    break
            if local_obs > global_obs:
                global_obs = local_obs

    # update by row
    global_obs = -1
    for j in range(len(obstacleGrid[0])):
        if global_obs != -1:
            for i in range(global_obs):
                obstacleGrid[i][j] = 1

        if obstacleGrid[0][j] == 1:
            # find max
            local_obs = 0
            for i in range(len(obstacleGrid)):
                if obstacleGrid[i][j] == 1:
                    local_obs += 1
                else:
                    break
            if local_obs > global_obs:
                global_obs = local_obs

    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[i])):
            obstacleGrid[i][j] *= -1

    if obstacleGrid[0][0] == -1 or \
        obstacleGrid[-1][-1] == -1:
        return 0
    
    obstacleGrid[0][0] = 1

    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[i])):
            if i == 0 and j == 0:
                continue

            if obstacleGrid[i][j] == -1:
                continue

            path = 0
            if obstacleGrid[i-1][j] != -1:
                path += obstacleGrid[i-1][j]
            if obstacleGrid[i][j-1] != -1:
                path += obstacleGrid[i][j-1]
            obstacleGrid[i][j] = path
    
    return obstacleGrid[-1][-1]

g = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]] 
print(uniquePathsWithObstacles(g))