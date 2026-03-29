class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        if len(intervals) == 0:
            return []
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            previousInterval = res[-1]
            if interval[0] <= previousInterval[1] or interval[1] <= previousInterval[0]:
                res.pop()
                mergedInterval = [min(previousInterval[0], interval[0]), max(previousInterval[1], interval[1])]
                res.append(mergedInterval)
            else:
                res.append(interval)
        return res
                