import heapq

intervals = [[0,30],[15,20],[5,10],[5,7]]

def getMinRooms(intervals):
    intervals.sort(key=lambda x:x[0])
    if len(intervals) == 0:
        return 0
    
    # add end to the heap
    roomList = [intervals[0][1]]
    heapq.heapify(roomList)
    for interval in intervals[1:]:
        if interval[0] >= roomList[0]:
            heapq.heappop(roomList)
        heapq.heappush(roomList, interval[1])
    
    print(roomList)
    return len(roomList)

print(getMinRooms(intervals))