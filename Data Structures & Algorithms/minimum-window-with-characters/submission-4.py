class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = {}
        for c in t:
            if c in missing:
                missing[c] += 1
            else:
                missing[c] = 1

        bestWindow = ""
        bestWindowSize = float("inf")
        left = 0
        right = 0
        while True:
            while max(missing.values()) > 0 and right < len(s):
                if s[right] in missing:
                    missing[s[right]] -= 1
                right += 1
            while left < len(s) and s[left] not in missing:
                left += 1
            if max(missing.values()) <= 0 and right-left < bestWindowSize:
                bestWindowSize = right-left
                bestWindow = s[left:right]
            if left >= len(s):
                return bestWindow
            missing[s[left]] += 1
            left += 1        