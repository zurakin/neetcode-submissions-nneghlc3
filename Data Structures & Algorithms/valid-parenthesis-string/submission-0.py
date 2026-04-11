class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0
        maxOpen = 0
        for c in s:
            if c == '(':
                minOpen += 1
                maxOpen += 1
            elif c == ')':
                minOpen = max(0, minOpen-1)
                if maxOpen <= 0:
                    return False
                maxOpen -= 1
            else:
                minOpen = max(0, minOpen-1)
                maxOpen += 1
        return minOpen == 0
