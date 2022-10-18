intervals = [[0,30],[15,20],[5,10],[5,7]]

def getMinRooms(intervals):
    intervals.sort(key=lambda x:(x[0],x[1]))
    roomList = []
    for interval in intervals:
        index = -1
        for i,room in enumerate(roomList):
            lastRoom = room[-1]
            # print(i, "lastRoom ->", lastRoom)
            if interval[0] >= lastRoom[1]:
                index = i
                break
        if index != -1:
            roomList[index] += [interval]
        else:
            roomList += [[interval]]

    return len(roomList)

print(getMinRooms(intervals))