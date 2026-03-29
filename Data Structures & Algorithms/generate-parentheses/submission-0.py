class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.backtrack([], 0, n, n)
        return self.res
        
    def backtrack(self, currentParenthesis, nbOpenParenthesis, remainingOpen, remainingClose):
        if remainingOpen == 0 and remainingClose == 0:
            self.res.append("".join(currentParenthesis))
        if nbOpenParenthesis > 0 and remainingClose > 0:
            currentParenthesis.append(')')
            self.backtrack(currentParenthesis, nbOpenParenthesis-1, remainingOpen, remainingClose-1)
            currentParenthesis.pop()
        if remainingOpen > 0:
            currentParenthesis.append('(')
            self.backtrack(currentParenthesis, nbOpenParenthesis+1, remainingOpen-1, remainingClose)
            currentParenthesis.pop()