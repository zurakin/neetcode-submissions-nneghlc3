class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        compsMapping = {}
        for s in strs:
            comp = getComposition(s)
            if comp in compsMapping:
                compsMapping[comp].append(s)
            else:
                compsMapping[comp] = [s]
        return list(compsMapping.values())
        
def getComposition(s):
    composition = [0] * (ord('z')-ord('a')+1)
    for c in s:
        composition[ord(c)-ord('a')] += 1
    return tuple(composition)