class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n not in visited:
            visited.append(n)
            digits = [int(d)**2 for d in list(str(n))]
            n = sum(digits)
            if n == 1:
                return True
        return False
        