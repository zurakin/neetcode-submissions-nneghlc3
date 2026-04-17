class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        mem = {}
        def maxCoinsInInterval(i, j):
            if i > j:
                return 0

            if (i, j) in mem:
                return mem[(i, j)]
            
            res = 0
            for k in range(i, j+1):
                res = max(res, maxCoinsInInterval(i, k-1) + maxCoinsInInterval(k+1, j) + nums[i-1] * nums[k] * nums[j+1])
            
            mem[(i, j)] = res
            return res

        return maxCoinsInInterval(1, len(nums)-2)