class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = []
        merge = []
        after = []
        beg, end = newInterval
        for i, (begI, endI) in enumerate(intervals):
            if endI < beg:
                before.append(i)
            elif begI > end:
                after.append(i)
            else:
                merge.append(i)

        mergeInf = min(beg, intervals[merge[0]][0]) if merge else beg
        mergeSup = max(end, intervals[merge[-1]][1]) if merge else end
        res = [intervals[i] for i in before] + [[mergeInf, mergeSup]] + [intervals[i] for i in after]
        return res