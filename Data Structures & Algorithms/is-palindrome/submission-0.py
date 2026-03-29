class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = [c.lower() for c in s if c.isalnum()]
        return stripped[::-1] == stripped