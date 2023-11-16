from typing import List

def minReorder(n: int, connections: List[List[int]]) -> int:
    # setup tree
    treeDic = {}
    isExplored = [0] * n
    for i in range(n):
        treeDic[i] = {}
        treeDic[i]["from"] = []
        treeDic[i]["to"] = []
    
    for conn in connections:
        treeDic[conn[0]]["to"] += [conn[1]]
        treeDic[conn[1]]["from"] += [conn[0]]

    toExplore = [0]
    isExplored[0] = 1
    ans = 0
    while len(toExplore) > 0:
        start = toExplore.pop(0)
        isExplored[start] = 1
        
        for i in treeDic[start]["from"]:
            if isExplored[i] == 0:
                toExplore += [i]
        
        for i in treeDic[start]["to"]:
            if isExplored[i] == 0:
                toExplore += [i]
                ans += 1
    
    return ans

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(n, connections))