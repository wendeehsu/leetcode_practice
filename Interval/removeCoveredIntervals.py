from typing import List

def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    if len(intervals) == 1:
        return 1
    
    intervals = sorted(intervals, key= lambda x: (x[0], x[1]))
    left = 0
    right = 1

    while right < len(intervals):
        if intervals[left][0] <= intervals[right][0] and \
            intervals[left][1] >= intervals[right][1]:
            print("pop",intervals.pop(right))
        elif intervals[left][0] == intervals[right][0] and \
            intervals[left][1] <= intervals[right][1]:
            print("pop",intervals.pop(left))
        else:
            left += 1
            right += 1
    return len(intervals)


intervals = [[1,2],[1,4],[3,4]]
print(removeCoveredIntervals(intervals))