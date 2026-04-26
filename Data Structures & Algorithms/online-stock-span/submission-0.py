class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        res = 1
        current = len(self.arr)-1
        while current >= 0 and self.arr[current][0] <= price:
            res += self.arr[current][1]
            current -= self.arr[current][1]
        self.arr.append((price, res))
        return res 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)