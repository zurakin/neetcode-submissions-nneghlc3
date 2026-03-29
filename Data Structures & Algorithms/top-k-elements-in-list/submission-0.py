class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for n in nums:
            if n in frequencies:
                frequencies[n] += 1
            else:
                frequencies[n] = 1
        inversedFrequencies = {}
        for n in frequencies:
            if frequencies[n] in inversedFrequencies:
                inversedFrequencies[frequencies[n]].append(n)
            else:
                inversedFrequencies[frequencies[n]] = [n]
        res = []
        for f in range(len(nums), -1, -1):
            if f in inversedFrequencies:
                res.extend(inversedFrequencies[f])
            if len(res) >= k:
                return res 

