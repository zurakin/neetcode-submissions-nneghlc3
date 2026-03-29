class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        window = set([s[0]])
        largestWindow = 1 
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                largestWindow = max(largestWindow, len(window))
                right += 1
            else: 
                window.remove(s[left])
                left += 1
        return largestWindow

        