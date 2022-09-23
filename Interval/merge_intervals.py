intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]

def solution(intervals):
    class interval:
        def __init__(self,start,end):
            self.start = start
            self.end = end
        
        def toList(self):
            return [self.start, self.end]

    intervals = sorted(intervals, key=lambda x: x[0])

    if len(intervals) < 2:
        return intervals
    
    # turn into interval class
    for index, item in enumerate(intervals):
        intervals[index] = interval(item[0], item[1])
    
    startIndex = 0
    endIndex = 1
    
    while endIndex < len(intervals):
        startInterval = intervals[startIndex]
        endInterval = intervals[endIndex]

        """
        cases:
        1. no overlap: startIndex++ endIndex++
        2. merge
        """
        if startInterval.end < endInterval.start:
            startIndex += 1
            endIndex += 1
        else:
            # to merge
            intervals.pop(endIndex)
            intervals[startIndex] = interval(min(startInterval.start,endInterval.start), max(startInterval.end,endInterval.end))

    for i in range(len(intervals)):
        intervals[i] = intervals[i].toList()

    return intervals


print("solution ->", solution(intervals))