class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        totalCounter = Counter(s)
        size = 0
        res = []
        counter = {}
        for i in range(len(s)):
            size += 1
            if s[i] not in counter:
                remaining = totalCounter[s[i]]
                counter[s[i]] = remaining - 1
            else: 
                counter[s[i]] -= 1
            if counter[s[i]] == 0:
                del counter[s[i]]
            if len(counter) == 0:
                res.append(size)
                size = 0
        return res