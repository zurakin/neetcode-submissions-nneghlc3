class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        beg = 0 
        end = len(heights) - 1
        while beg < end:
            area = (end-beg) * min(heights[beg], heights[end])
            res = max(area, res)
            if heights[beg] > heights[end]:
                end -= 1
            else:
                beg += 1
        return res
