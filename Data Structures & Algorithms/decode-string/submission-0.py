class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        lastDigit = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                lastDigit += s[i]
            elif s[i] == '[':
                openBrackets = 1
                j = i + 1
                while openBrackets > 0:
                    if s[j] == ']':
                        openBrackets -= 1
                    elif s[j] == '[':
                        openBrackets += 1
                    j += 1
                subString = self.decodeString(s[i+1: j-1])
                res += int(lastDigit) * subString
                i = j-1
                lastDigit = ""
            else:
                res += s[i]
                lastDigit = ""
            i += 1
        return res