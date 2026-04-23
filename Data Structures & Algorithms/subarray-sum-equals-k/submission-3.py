class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = [0 for _ in range(len(nums))]
        prefixes[0] = nums[0]
        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] + nums[i]

        counter = Counter(prefixes)
        res = counter[k]
        for i in range(len(prefixes)):
            counter[prefixes[i]] -= 1
            res += counter[prefixes[i]+k]
        return res
