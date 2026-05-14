class FreqStack:

    def __init__(self):
        self.heap = []
        self.frequencies = defaultdict(int)
        self.counter = 0
        

    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        self.counter += 1
        heapq.heappush(self.heap, (-self.frequencies[val], -self.counter, val))
        

    def pop(self) -> int:
        val = heapq.heappop(self.heap)[2]
        self.frequencies[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()