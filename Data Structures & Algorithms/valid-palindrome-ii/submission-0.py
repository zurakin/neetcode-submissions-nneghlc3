class Solution:
    def validPalindrome(self, s: str) -> bool:
        deletedChar = False
        
        def palindrome(i, j):
            nonlocal deletedChar
            if i >= j:
                return True
            if s[i] == s[j]:
                return palindrome(i+1, j-1)
            if not deletedChar:
                deletedChar = True
                return palindrome(i, j-1) or palindrome(i+1, j)
            return False

        return palindrome(0, len(s)-1)