class Solution:
    def myPow(self, x: float, n: int) -> float:
        positive = n >= 0
        n = abs(n)
        if n == 0:
            return 1
        if n == 1:
            res = x
        else:
            res = self.myPow(x, n//2)
            res = res * res 
            if n % 2 == 1:
                res *= x
        if positive: 
            return res 
        return 1 / res
            
        
        