"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted([(interval.start, interval.end) for interval in intervals])
        res = 0 
        heap = []
        for interval in intervals:
            while heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            res = max(res, len(heap))
        return res
            