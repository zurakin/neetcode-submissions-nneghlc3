import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def dist(e):
            return abs(x-e)

        if len(arr) == 0 or k == 0:
            return []

        idx = bisect.bisect_left(arr, x)
        if idx == len(arr):
            idx -= 1
        if idx-1 >= 0 and dist(arr[idx-1]) < dist(arr[idx]):
            idx -= 1

        i, j = idx, idx
        while j-i+1 < k:
            if j == len(arr)-1:
                i -= 1
            elif i == 0:
                j += 1
            elif dist(arr[i-1]) <= dist(arr[j+1]):
                i -= 1
            else:
                j += 1
        return arr[i:j+1]
            
