class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Histogram = [0] * 26
        for c in s1:
            s1Histogram[ord(c)-ord('a')] += 1

        window = [0] * 26
        for i in range(len(s1)):
            c = s2[i]
            window[ord(c)-ord('a')] += 1
        if s1Histogram == window:
            return True

        for i in range(1, len(s2)-len(s1)+1):
            removedChar = s2[i-1]
            window[ord(removedChar)-ord('a')] -= 1
            addedChar = s2[i+len(s1)-1]
            window[ord(addedChar)-ord('a')] += 1
            if s1Histogram == window:
                return True

        return False
