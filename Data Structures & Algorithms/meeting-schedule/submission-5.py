"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import bisect
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = []
        for interval in intervals:
            start, end = interval.start, interval.end
            if end <= start:
                continue
            pos = bisect.bisect_right(meetings, (start, end))
            print(pos)
            if pos > 0 and start < meetings[pos-1][1]:
                return False 

            if pos < len(meetings) and end > meetings[pos][0]:
                return False
            meetings.insert(pos, (start, end))
        return True


    