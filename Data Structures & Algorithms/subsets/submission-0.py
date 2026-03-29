class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        for i in range(2**N):
            l = []
            for j in range(N):
                if i&(1<<j):
                    l.append(nums[j])
            res.append(l)
        return res
