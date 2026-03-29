class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prefix = self.getPrefix(heights)
        suffix = self.getPrefix(heights[::-1])[::-1]
        
        largestArea = 0
        for i in range(len(heights)):
            area = heights[i] * (1 + prefix[i] + suffix[i])
            largestArea = max(area, largestArea)
        return largestArea

    def getPrefix(self, heights: List[int]):
        prefix = []
        stack = []
        for i, h in enumerate(heights):
            while len(stack) > 0 and heights[stack[-1]] >= h:
                stack.pop()
            pre = i
            if len(stack) > 0:
                pre -= (stack[-1]+1)
            stack.append(i)
            prefix.append(pre)
        return prefix