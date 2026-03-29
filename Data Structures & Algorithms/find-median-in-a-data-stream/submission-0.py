# class MedianFinder:

#     def __init__(self):
#         self.left = []
#         self.right = []

#     def addNum(self, num: int) -> None:
#         if len(self.left) == 0:
#             self.left.append(num)
#             continue

        

#     def findMedian(self) -> float:
        
        

class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        return (self.data[n // 2] if (n & 1) else
                (self.data[n // 2] + self.data[n // 2 - 1]) / 2)