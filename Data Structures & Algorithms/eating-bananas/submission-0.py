class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minRate = right
        while left <= right:
            mid = (left + right) // 2
            s = score(piles, mid)
            if s <= h:
                minRate = mid
                right = mid - 1
            else:
                left = mid + 1
        return minRate

def score(piles, rate):
    res = 0
    for p in piles:
        res += math.ceil(p/rate)
    return res