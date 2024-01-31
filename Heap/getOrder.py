from typing import List
import heapq

def getOrder(tasks: List[List[int]]) -> List[int]:
    allList = [] # (startTime, process, index)
    available = [] # (process, index)
    heapq.heapify(allList)
    heapq.heapify(available)
    for i, e in enumerate(tasks):
        heapq.heappush(allList, e+[i])
    
    ans = []
    time = 0
    while len(allList) > 0 or len(available) > 0:
        """
        steps:
        1. update available
            - if no available -> update time
            - place qualified tasks into available
        2. get next to process
        """

        if len(available) == 0:
            task = heapq.heappop(allList)
            time = max(time,task[0])
            heapq.heappush(available, [task[1], task[2]])
        
        while len(allList) > 0 and allList[0][0] <= time:
            task = heapq.heappop(allList)
            heapq.heappush(available, [task[1], task[2]])
            
        nextTask = heapq.heappop(available)
        time += nextTask[0]
        print("processed:", nextTask, "time ->", time)
        ans.append(nextTask[1])
    
    return ans
        
    
tasks = [[1,2],[2,4],[2,4],[3,2],[4,1]]
print(getOrder(tasks))