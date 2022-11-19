n = 5
edges = [[0,1],[1,2],[3,4]]

def traverse(parent, current, visited, graph):
    visited[current] = 1
    for child in graph[current]:
        if child != parent and visited[child] == 0:
            traverse(current, child, visited, graph)

def getConnect(n, edges):
    # create connected graph
    graph = {}
    for i in range(n):
        graph[i] = []
    
    for pair in edges:
        graph[pair[0]] += [pair[1]]
        graph[pair[1]] += [pair[0]]

    # traverse graph
    component = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            component += 1
            visited[i] = 1
            # start traverse ans mark visited
            for child in graph[i]:
                traverse(i, child, visited, graph)
            # print(i, "->", visited)

    return component

print(getConnect(n, edges))