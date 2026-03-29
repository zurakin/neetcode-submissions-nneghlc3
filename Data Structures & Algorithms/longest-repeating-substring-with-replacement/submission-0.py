class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        window = {s[0]: 1}
        largestWindow = 1
        while right < len(s):
            c = s[right]
            if c not in window:
                window[c] = 1
            else: 
                window[c] += 1
            while right-left+1-max(window.values()) > k:
                # print(left, right)
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            largestWindow = max(largestWindow, right-left+1)
            right += 1
        return largestWindow
                