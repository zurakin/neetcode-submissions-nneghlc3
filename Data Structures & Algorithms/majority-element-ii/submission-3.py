class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements = {}
        for n in nums:
            if n in elements:
                elements[n] += 1
            elif len(elements) < 2:
                elements[n] = 1
            else:
                keys = list(elements.keys())
                for k in keys:
                    elements[k] -= 1
                    if elements[k] == 0:
                        del elements[k]

        survivors = set(elements.keys())
        occurences = defaultdict(int)
        
        for e in nums:
            if e in survivors:
                occurences[e] += 1
        # print(occurences)

        return [e for e in survivors if occurences[e] > len(nums)/3]