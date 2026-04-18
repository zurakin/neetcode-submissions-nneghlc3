class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [-1, -1, -1]
        for triplet in triplets:
            if all([triplet[i] <= target[i] for i in range(3)]):
                merged = [max(merged[i], triplet[i]) for i in range(3)]
        return merged == target
                