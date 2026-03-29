class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        boundries = []
        for interval in intervals:
            boundries.append((interval[0], False)) # False represents the opening of an interval
            boundries.append((interval[1], True)) # True represents the closing of an interval
        boundries.sort()

        print(boundries)

        openInterval = 0
        openIntervalsCount = 0
        
        res = []
        for boundry in boundries:
            if boundry[1]:
                openIntervalsCount -= 1
                if openIntervalsCount == 0:
                    res.append([openInterval, boundry[0]])
            else:
                openIntervalsCount += 1
                if openIntervalsCount == 1:
                    openInterval = boundry[0]
        return res


    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
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
                