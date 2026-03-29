class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            j = 0
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                j += 1
            j -= 1
            if 2*j+1 > len(longest):
                longest = s[i-j: i+j+1]
            
            j = i
            k = i+1
            l = 0
            while j >= 0 and k < len(s) and s[j] == s[k]:
                l += 2
                j -= 1
                k += 1
            j += 1
            k -= 1
            if l > len(longest):
                longest = s[j: k+1]
        
        return longest
