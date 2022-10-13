intervals = [[0,3],[15,20],[5,10]]

def canAttendMeetings(intervals):
    intervals = sorted(intervals,key=lambda x:x[0])
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

print(canAttendMeetings(intervals))