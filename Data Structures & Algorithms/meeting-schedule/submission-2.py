"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted([(interval.start, interval.end) for interval in intervals])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


        # meetings = []
        # for interval in intervals:
        #     start, end = interval.start, interval.end
        #     pos = bisect.bisect_right(meetings, (start, end))
        #     if pos >0 and start < meetings[pos-1][1]:
        #         return False 
        #     bisect.insort(meetings, (start, end))
        # return True