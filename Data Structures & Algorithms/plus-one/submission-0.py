class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        residue = 1
        for i in range(len(digits)-1, -1, -1):
            print(residue)
            digits[i] += residue
            residue = 0
            if digits[i] >= 10:
                digits[i] -= 10
                residue = 1
        if residue:
            digits.insert(0, 1)
        return digits

        