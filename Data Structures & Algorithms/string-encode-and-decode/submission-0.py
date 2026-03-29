class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        current = 0
        while current < len(s):
            i = current+1
            while s[i] != ":":
                i+=1
            length = int(s[current:i])
            res.append(s[i+1:i+length+1])
            current = i + length + 1
        return res
            

