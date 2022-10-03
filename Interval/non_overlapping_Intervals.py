intervals = [[1,2],[1,2],[1,2]]

def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0
    
    intervals.sort(key=lambda x: x[0])
    startIndex = 0
    endIndex = 1
    popTimes = 0

    while endIndex < len(intervals):
        if intervals[endIndex][0] < intervals[startIndex][1]:
            # overlap
            poped = None
            if intervals[endIndex][1] >= intervals[startIndex][1]:
                poped = intervals.pop(endIndex)
            else:
                poped = intervals.pop(startIndex)
            popTimes += 1
            print("poped ->", poped)

        else:
            startIndex += 1
            endIndex += 1
    print(intervals)
    return popTimes

print(eraseOverlapIntervals(intervals))