class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) == 0:
            return 0
        prevEnd = intervals[0][1]
        erased = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                erased += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        return erased


    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        erased = 0
        previousIntervals = set()
        previousIntervals.add(0)

        def inConflict(i, j): # i, j must be in order
            return intervals[j][0] < intervals[i][1]

        for j in range(1, len(intervals)):
            nextPreviousIntervals = set()
            nextPreviousIntervals.add(j)
            foundSolution = False
            for i in previousIntervals:
                if not inConflict(i, j):
                    foundSolution = True
                    break
                else:
                    nextPreviousIntervals.add(i)
            if foundSolution:
                previousIntervals = set([j])
            else:
                erased += 1
                previousIntervals = nextPreviousIntervals
        return erased
            