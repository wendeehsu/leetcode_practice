from typing import List

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # init network
    treeDic = {}
    isExplore = [-1]*n
    for i in range(1,1+n):
        treeDic[i] = []
    
    for pair in times:
        treeDic[pair[0]] += [pair[1:]]

    # print("tree ->", treeDic)

    toExplore = [k]
    isExplore[k-1] = 0
    while len(toExplore) > 0:
        startIndex = toExplore.pop(0)
        for child in treeDic[startIndex]:
            distance = isExplore[startIndex-1] + child[1]
            if isExplore[child[0]-1] == -1:
                isExplore[child[0]-1] = distance
                toExplore += [child[0]]
            else:
                if distance < isExplore[child[0]-1]:
                    isExplore[child[0]-1] = distance
                    toExplore += [child[0]]

        # print(startIndex, ":", isExplore)


    localMax = -1
    for i in isExplore:
        if i == -1:
            return -1
        elif localMax == -1:
            localMax = i
        else:
            localMax = max(localMax, i)
    return localMax    


times = [[1,2,1]]
n = 2
k = 1
print(networkDelayTime(times, n, k))