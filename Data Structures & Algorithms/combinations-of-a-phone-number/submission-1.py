class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.digits = [int(c) for c in digits]
        self.dic = {
            2: "abc",
            3: "def",
            4: "ghi", 
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        self.res = []
        self.backtrack([], 0)
        return self.res

    def backtrack(self, letters, i):
        if i >= len(self.digits):
            self.res.append("".join(letters))
            return
        for l in self.dic[self.digits[i]]:
            letters.append(l)
            self.backtrack(letters, i+1)
            letters.pop()
        
