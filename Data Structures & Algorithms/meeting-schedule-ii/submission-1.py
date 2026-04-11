"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class TreeNode:
    def __init__(self, interval: Interval, count=0):
        self.interval = interval
        self.children = [] # 0 children -> leaf
        self.count = count
    
    def merge(self, interval): 
        if len(self.children)==0 and self.interval.start == interval.start and self.interval.end == interval.end:
            self.count += 1 
            return self.count
        if len(self.children) == 0:
            self.children = []
            previousCount = self.count
            if self.interval.start < interval.start:
                self.children.append(TreeNode(Interval(self.interval.start, interval.start), previousCount))
            if interval.start < interval.end:
                self.count += 1
                self.children.append(TreeNode(Interval(interval.start, interval.end), previousCount+1))
            if interval.end < self.interval.end:
                self.children.append(TreeNode(Interval(interval.end, self.interval.end), previousCount))
            return self.count
            
        # Otherwise interval is a subinterval of self.interval -> we need to insert it in children
        for child in self.children:
            childInterval = child.interval
            intersection = Interval(max(childInterval.start, interval.start), min(childInterval.end, interval.end))
            if intersection.start < intersection.end:
                self.count = max(self.count, child.merge(intersection))
        return self.count 
    
    def toString(self):
        return f"({self.interval.start}, {self.interval.end}): {self.count}: {[child.toString() for child in self.children]}"


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        root = TreeNode(Interval(float('-inf'), float('inf')))
        for interval in intervals:
            root.merge(interval)
        # print(root.toString())
        return root.count
        