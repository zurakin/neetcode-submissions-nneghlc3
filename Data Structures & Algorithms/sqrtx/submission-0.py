class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid 
            if sqr == x:
                return mid 
            elif sqr < x:
                low = mid + 1
            else: 
                high = mid - 1
        return high