n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

def dfs(visited, edgeDic, current, parent):
    visited[current] = 1
    for child in edgeDic[current]:
        if child == parent:
            continue
        if visited[child] == 1:
            return False
        if visited[child] == 0:
            if dfs(visited,edgeDic,child, current) == False:
                return False
    return True

def traverse(n, edges):
    if len(edges) != n-1:
        return False
        
    edgeDic = {}
    visited = [0] * n
    for i in range(n):
        edgeDic[i] = []
    
    for edge in edges:
        edgeDic[edge[0]] += [edge[1]]
        edgeDic[edge[1]] += [edge[0]]
    
    # counter = 0
    # for i in range(n):
    #     if visited[i] == 0: # not visited
    #         if counter > 0:
    #             return False

    #         if dfs(visited, edgeDic, i, -1) == False:
    #             return False
    #         counter += 1

    return dfs(visited, edgeDic, 0, -1) and sum(visited) == len(visited)

print(traverse(n, edges))