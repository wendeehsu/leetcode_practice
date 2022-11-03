n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

def dfs(visited, edgeDic, parent, priorList):
    visited[parent] = 1
    priorList += [parent]
    for child in edgeDic[parent]:
        if len(priorList) >=2 and child == priorList[-2]:
            continue
        if visited[child] == 1:
            return False
        if visited[child] == 0:
            if dfs(visited,edgeDic,child, priorList) == False:
                return False
    visited[parent] = 2
    priorList.pop()
    return True

def traverse(n, edges):
    edgeDic = {}
    visited = [0] * n
    for i in range(n):
        edgeDic[i] = []
    
    for edge in edges:
        edgeDic[edge[0]] += [edge[1]]
        edgeDic[edge[1]] += [edge[0]]
    
    counter = 0
    for i in range(n):
        if visited[i] == 0: # not visited
            if counter > 0:
                return False

            if dfs(visited, edgeDic, i, []) == False:
                return False
            counter += 1

    return True

print(traverse(n, edges))