class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return getDict(s) == getDict(t)

def getDict(s):
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic
        
        