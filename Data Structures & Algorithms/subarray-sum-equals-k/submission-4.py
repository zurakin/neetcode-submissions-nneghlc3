class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = [0 for _ in range(len(nums))]
        prefixes[0] = nums[0]
        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] + nums[i]
        
        occurences = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            res += occurences[prefixes[i]-k]
            occurences[prefixes[i]] += 1
        res += occurences[k]
        return res
            

