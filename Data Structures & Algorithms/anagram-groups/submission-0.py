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
    return "".join(sorted(s))