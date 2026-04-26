class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        currentSize = 0
        prevSign = None
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff == 0:
                currentSize = 0
                prevSign = None
                continue
            sign = 1 if diff > 0 else -1
            if sign != prevSign:
                currentSize += 1
                res = max(res, currentSize)
                prevSign = sign
            else:
                currentSize = 1
                prevSign = sign
        
        return res+1

