class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements = {}
        for n in nums:
            if n in elements:
                elements[n] += 1
            elif len(elements) < 3:
                elements[n] = 1
            else:
                keys = list(elements.keys())
                for k in keys:
                    elements[k] -= 1
                    if elements[k] == 0:
                        del elements[k]
        return [e for e in list(elements.keys()) if nums.count(e) > len(nums)/3]