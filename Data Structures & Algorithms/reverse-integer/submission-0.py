class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10 
        res = 0
        for i in range(len(digits)):
            res += digits[len(digits) - 1 - i] * 10**i
        if (res >> 31) > 0:
            return 0
        return sign * res