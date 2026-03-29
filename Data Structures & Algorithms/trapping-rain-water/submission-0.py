class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        prefix = [0] * len(height)
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i-1])
        suffix = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i+1])

        for i in range(1, len(height)-1):
            water = min(prefix[i], suffix[i]) - height[i]
            if water < 0:
                water = 0 
            totalWater += water
        return totalWater
        