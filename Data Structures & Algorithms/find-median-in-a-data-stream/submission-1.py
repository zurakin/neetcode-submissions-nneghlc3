class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == 0:
            self.left.append(-num)
            return
        if num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        self.balance()

    def balance(self):
        while len(self.left) > (len(self.right)+1):
            n = -heapq.heappop(self.left)
            heapq.heappush(self.right, n)
        while len(self.right) > len(self.left):
            n = heapq.heappop(self.right)
            heapq.heappush(self.left, -n)

    def findMedian(self) -> float:
        if len(self.right) == 0: # left only has 1 element
            return -self.left[0]
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]

        
        