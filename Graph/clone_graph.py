class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

adjList = [[2,4],[1,3],[2,4],[1,3]]

# create graph
graph = []
for index, sublist in enumerate(adjList):
    graph += [Node(index+1, None)]

for index, sublist in enumerate(adjList):
    node_list = []
    for sub_node in sublist:
        node_list += [graph[sub_node-1]]
    graph[index].neighbors = node_list


visited = {} # {val: Node}

def copyNode(currentNode):
    if currentNode == None:
        return None
    
    # if val not in visited -> create new node
    # else get node
    if currentNode.val not in visited:
        visited[currentNode.val] = Node(currentNode.val,[])
        neighborList = []
        for neighbor in currentNode.neighbors:
            neighborList += [copyNode(neighbor)]
        visited[currentNode.val].neighbors = neighborList
    return visited[currentNode.val]

node = graph[0]
startNode = copyNode(node)

# traverse graph
newAdjList = {}
def printGraph(currentNode):
    if currentNode != None:
        if currentNode.val not in newAdjList:
            newAdjList[currentNode.val] = []
            for neighbor in currentNode.neighbors:
                newAdjList[currentNode.val] += [neighbor.val]
                print("currentNode.val:", currentNode.val, newAdjList)
                printGraph(neighbor)
    # return None
printGraph(startNode)
print("newAdjList ->", newAdjList)